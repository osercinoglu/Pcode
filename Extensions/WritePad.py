from PyQt4 import QtCore, QtGui


class WritePad(QtGui.QMainWindow):

    def __init__(self, path, name, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        self.setWindowTitle(name + " - Notes")
        self.resize(500, 300)
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                 (screen.height() - size.height()) / 2)

        self.path = path

        self.noteSaveTimer = QtCore.QTimer()
        self.noteSaveTimer.setSingleShot(True)
        self.noteSaveTimer.setInterval(1000)
        self.noteSaveTimer.timeout.connect(self.saveNotes)

        self.writePad = QtGui.QPlainTextEdit()
        self.writePad.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.writePad.setFont(QtGui.QFont("Ms Reference Sans Serif", 10.9))
        self.setCentralWidget(self.writePad)

        # load notes
        try:
            file = open(self.path, "r")
            self.writePad.setPlainText(file.read())
            file.close()
        except:
            file = open(path, "w")
            file.close()

        self.writePad.textChanged.connect(self.noteSaveTimer.start)

    def saveNotes(self):
        file = open(self.path, "w")
        file.write(self.writePad.toPlainText())
        file.close()
