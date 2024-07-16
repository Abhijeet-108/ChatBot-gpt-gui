import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(610, 420)

        # Add chatArea widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 328)

        # Add InputArea widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 360, 480, 40)

        # Add Send button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 360, 100, 40)

        self.show()


class Chatbot:
    pass


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
