from PySide6.QtWidgets import QMainWindow, QTextEdit, QFileDialog
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MindFlow')
        self.setMinimumSize(800, 600)
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('File')
        new_action = QAction('New', self)
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)
        open_action = QAction('Open', self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
        save_action = QAction('Save', self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)


    def new_file(self):
        self.editor.clear()


    def open_file(self):
        pass


    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save file', '', 'Text files (*.txt);;All files (*)')
        if file_path:
            with open(file_path, 'w', encoding='utf-8') as file:
                text = self.editor.toPlainText()
                file.write(text)