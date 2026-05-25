from PyQt5.QtWidgets import QMainWindow,QApplication,QLayout,QWidget
import sys

def ConstructApp() -> QApplication:
    
    window = QMainWindow()
    
    window.setWindowTitle("CharTest")
    
    layout = QLayout()
    app = QApplication(sys.argv)
    
    mainwidget = QWidget()
    app
    
    return app

ConstructApp().exec()