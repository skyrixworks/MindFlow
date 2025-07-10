from PySide6.QtWidgets import QMainWindow, QTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MindFlow')
        self.setMinimumSize(800, 600)
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)