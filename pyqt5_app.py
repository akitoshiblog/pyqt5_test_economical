import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QApplication, QLabel, QGridLayout)



class App(QWidget):
    def __init__(self):
        super().__init__()
        with open("text.txt") as f: 
            self.text = f.read()
        self.initUI()
        
    def initUI(self):
        title = QLabel("Explanation : ")
        labelReading = QLabel(self.text)
        quitButton= QPushButton("quit")
        quitButton.clicked.connect(self.quit)
        cancelButton = QPushButton("Cancel")

        grid = QGridLayout()
        grid.addWidget(title,0,0,1,1) 
        grid.addWidget(labelReading,0,1,1,1) 
        grid.addWidget(quitButton,1,1,1,1) 
        grid.addWidget(cancelButton,1,2,1,1) 
        
        self.setLayout(grid)    
        
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('sample app')
        self.show()
        
    def quit(self):
        QApplication.instance().quit()
        
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

