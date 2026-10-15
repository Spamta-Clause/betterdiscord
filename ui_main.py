import sys
from datetime import datetime
from pathlib import Path

from PySide6.QtCore import Qt, QTimer, QEvent
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QButtonGroup,
    QVBoxLayout, QHBoxLayout, QInputDialog, QDialog
)

# Compiles mainwindow.ui at startup. Path is relative to this file, not the terminal.
UI_PATH = str(Path(__file__).parent / "mainwindow.ui")
LOGIN_PATH = str(Path(__file__).parent / "login.ui")
Ui_LoginWindow, LoginClass = loadUiType(LOGIN_PATH)
Ui_MainWindow, BaseClass = loadUiType(UI_PATH)

import controller

class LoginWindow(LoginClass):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        self.ui.register_button.clicked.connect(self.register_user)
        self.ui.login_button.clicked.connect(self.login)
        self.user = None


    def register_user(self):
        username = self.ui.username.text()
        password = self.ui.password.text()

        try:
            self.user = controller.register_member(username, password)
            self.open_mainwindow()
        except controller.ExistingUser:
            self.ui.label.setText("Username already in use.")

    def login(self):
        username = self.ui.username.text()
        password = self.ui.password.text()

        try:
            self.user = controller.login(username, password)
            self.open_mainwindow()
        except controller.IncorrectPassword:
            self.ui.label.setText("Incorrect password entered")
        except controller.UnknownUser:
            self.ui.label.setText("User not found, consider registering.")

    def open_mainwindow(self):
        self.main_window = MainWindow(self.user)

        for gid, name in controller.get_groups(self.user.username):
            self.main_window.add_group_button(gid, name)
        self.main_window.show()
        self.close()


class MessageWidget(QWidget):
    def __init__(self, author, text, timestamp, parent=None):
        super().__init__(parent)
        name = QLabel(author)
        name.setStyleSheet("font-weight: bold;")
        name.setTextFormat(Qt.PlainText)

        time = QLabel(timestamp)
        time.setStyleSheet("color: gray;")
        time.setTextFormat(Qt.PlainText)

        body = QLabel(text)
        body.setWordWrap(True)
        body.setTextFormat(Qt.PlainText)  # stops users injecting HTML
        body.setTextInteractionFlags(Qt.TextSelectableByMouse)

        header = QHBoxLayout()
        header.addWidget(name)
        header.addWidget(time)
        header.addStretch()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(8, 4, 8, 4)
        layout.addLayout(header)
        layout.addWidget(body)


def get_layout(widget):
    """Use the layout set in Designer, or create one if it's missing."""
    layout = widget.layout()
    if layout is None:
        layout = QVBoxLayout(widget)
    return layout


def ensure_stretch(layout, at_start):
    """Add a spacer at the start or end, unless one is already there."""
    if layout.count():
        item = layout.itemAt(0 if at_start else layout.count() - 1)
        if item.spacerItem() is not None:
            return
    if at_start:
        layout.insertStretch(0)
    else:
        layout.addStretch()


class MainWindow(BaseClass):
    def __init__(self, user):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.current_group_id = None

        for area in (self.ui.messagesScroll, self.ui.groupsScroll):
            area.setWidgetResizable(True)
            area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Messages: spacer first, so short conversations sit at the bottom
        self.messages_layout = get_layout(self.ui.messagesContents)
        ensure_stretch(self.messages_layout, at_start=True)

        # Groups: spacer last, so everything is pushed to the top
        self.groups_layout = get_layout(self.ui.groupsContents)
        ensure_stretch(self.groups_layout, at_start=False)

        self.group_buttons = QButtonGroup(self)
        self.group_buttons.setExclusive(True)
        self.group_buttons.idClicked.connect(self.select_group)

        self.ui.send_button.clicked.connect(self.send_message)
        self.ui.new_group_button.clicked.connect(self.new_group)
        self.ui.sending_field.installEventFilter(self)

        self.user = user

        self.ui.invite_button.clicked.connect(self.invite)

    # ---------- messages ----------
    def add_message(self, author, text, timestamp):
        bar = self.ui.messagesScroll.verticalScrollBar()
        at_bottom = bar.value() >= bar.maximum() - 4
        self.messages_layout.addWidget(MessageWidget(author, text, timestamp))
        if at_bottom:  # only follow new messages if the user hasn't scrolled up
            QTimer.singleShot(0, lambda: bar.setValue(bar.maximum()))

    def clear_messages(self):
        while self.messages_layout.count() > 1:  # keep the spacer at index 0
            item = self.messages_layout.takeAt(1)
            if item.widget():
                item.widget().deleteLater()

    def fetch_messages(self, group_id):
        # TODO: replace with your datastore/backend call
        messages = controller.get_messages(group_id)
        print(messages)
        return messages
        return [("Alice", "Hello!", "10:01"), ("Bob", "Hey, how's it going?", "10:02")]

    def send_message(self):
        text = self.ui.sending_field.toPlainText().strip()
        if not text or self.current_group_id is None:
            return
        self.ui.sending_field.clear()
        # TODO: send `text` to your backend for self.current_group_id
        controller.send_message(self.user.username,text,self.current_group_id)
        self.clear_messages()
        for author, text, timestamp in self.fetch_messages(self.current_group_id):
            self.add_message(author, text, timestamp)

    def eventFilter(self, obj, event):
        # Enter sends, Shift+Enter inserts a new line
        if (obj is self.ui.sending_field
                and event.type() == QEvent.KeyPress
                and event.key() in (Qt.Key_Return, Qt.Key_Enter)
                and not event.modifiers() & Qt.ShiftModifier):
            self.send_message()
            return True  # swallow the key so no newline is inserted
        return super().eventFilter(obj, event)

    # ---------- groups ----------
    def add_group_button(self, group_id, name):
        btn = QPushButton(name)
        btn.setCheckable(True)
        self.group_buttons.addButton(btn, group_id)
        # insert just above the "new group" button
        index = self.groups_layout.indexOf(self.ui.new_group_button)
        self.groups_layout.insertWidget(index, btn)

    def select_group(self, group_id):
        self.current_group_id = group_id
        self.clear_messages()
        for author, text, timestamp in self.fetch_messages(group_id):
            self.add_message(author, text, timestamp)
    def invite(self):
        if self.current_group_id == None:
            return
        name, ok = QInputDialog.getText(self, "Invite user", "Username: ")
        name = name.strip()
        if not ok or not name:
            return
        controller.add_user_to_group(name, self.current_group_id)

    def new_group(self):
        name, ok = QInputDialog.getText(self, "New group", "Group name:")
        name = name.strip()
        if not ok or not name:
            return
        # TODO: create the group in your datastore and use the real id it returns
        group_id = controller.add_group(self.user.username, name)
        self.add_group_button(group_id, name)
        self.group_buttons.button(group_id).click()  # select it straight away


if __name__ == "__main__":
    app = QApplication(sys.argv)
    loginWindow = LoginWindow()
    loginWindow.show()
    # window = MainWindow()
    # # DEMO: replace with groups loaded from your datastore
    # for gid, name in [(1, "General"), (2, "Games"), (3, "Off-topic")]:
    #     window.add_group_button(gid, name)
    # window.show()
    sys.exit(app.exec())