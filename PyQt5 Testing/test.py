import sys
import webbrowser

from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Test App")

        layout = QVBoxLayout()
        button = QPushButton(text="GitHub")
        button.clicked.connect(lambda:webbrowser.open("https://github.com/j-jagger"))
        label = QLabel(text="Hello, World..?")

        layout.addWidget(label)

        layout.addWidget(button)
        

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()