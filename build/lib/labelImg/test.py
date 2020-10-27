import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    def __init__(self, parent=None):
        super(FirstMainWin, self).__init__(parent)

        self.setWindowTitle('1')

        self.resize(400, 300)

        self.status = self.statusBar()

        self.status.showMessage('only 5s', 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = FirstMainWin()
    main.show()

    sys.exit(app.exec_())