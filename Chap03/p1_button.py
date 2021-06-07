import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class ButtonWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 200, 150)
        self.setWindowTitle('QPushButton Widget')
        self.displayButton()

        self.show()

    def displayButton(self):
        name_label = QLabel(self)
        name_label.setText("Don't push the button.")
        name_label.move(60, 30)  # ! .move() to arrange position of the widget

        button = QPushButton('Push Me', self)
        button.clicked.connect(self.buttonClicked)
        button.move(80, 70)

    def buttonClicked(self):
        print('The window has been closed.')
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ButtonWindow()
    sys.exit(app.exec_())
