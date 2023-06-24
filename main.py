"""
LING HACKS V - June 24th to 25th

Idea: Translate images of Sign Language to text
Description: Takes images of hands and returns. 

Coders: Jason Xie, Subhash Srinivasa, Komal Tummala
"""

from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton
import tensorflow as ts
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("LingHacks V Project")

        button = QPushButton("My simple app.")
        button.pressed.connect(self.close)

        self.setCentralWidget(button)
        self.show()

app = QApplication(sys.argv)
w = MainWindow()
app.exec()

