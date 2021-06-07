# Import necessary modules
import sys
import typing

from PyQt5.QtWidgets import (QApplication, QWidget, QCheckBox, QLabel)
from PyQt5.QtCore import Qt


class CheckBoxWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 250, 250)
        self.setWindowTitle('QCheckBox Widget')
        self.displayCheckBoxes()
        self.show()

    def displayCheckBoxes(self):
        # Set up header
        header_label = QLabel(self)  # ? Is self important?
        header_label.setText(
            'Which shilfs can you work? (Please check all that apply)')
        header_label.setWordWrap(True)
        header_label.move(10, 10)
        header_label.resize(230, 60)

        # Set up checkboxes
        morning_checkbox = QCheckBox('Morning [8 AM - 2 PM]', self)
        morning_checkbox.move(20, 80)
        morning_checkbox.setChecked(False)
        morning_checkbox.stateChanged.connect(self.printToTerminal)

        after_checkbox = QCheckBox('After [1 PM - 8 PM]', self)
        after_checkbox.move(20, 100)
        after_checkbox.toggle()
        after_checkbox.stateChanged.connect(self.printToTerminal)

        night_checkbox = QCheckBox('Night [7 PM - 3 AM]', self)
        night_checkbox.move(20, 120)
        night_checkbox.toggle()
        night_checkbox.stateChanged.connect(self.printToTerminal)

    def printToTerminal(self, state):
        sender = self.sender()
        if state == Qt.Checked:
            print(f'{sender.text()} selected.')
        else:
            print(f'{sender.text()} deselected.')


# Run program
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CheckBoxWindow()
    sys.exit(app.exec_())
