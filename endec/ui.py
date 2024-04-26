from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton,QFileDialog,QInputDialog
import endec

class EncryptWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Encrypt')
        self.resize(1000, 750)
        mainLayout = QVBoxLayout()
        self.btnOpenFile = QPushButton('Choose File')
        self.btnOpenFile.clicked.connect(self.openFileDialog)
        mainLayout.addWidget(self.btnOpenFile)
        self.setLayout(mainLayout)
        self.btnEncrypt = QPushButton('Encrypt')
        self.btnEncrypt.clicked.connect(self.encrypt)
        mainLayout.addWidget(self.btnEncrypt)
    
    def openFileDialog(self):
        options = QFileDialog.Options()
        self.fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*);;Python Files (*.py)", options=options)
    def encrypt(self):
        try:
            en = endec.Endec(self.fileName)
            self.key = en.encrypting()
            print("This is key that can be used for decrypting:\n",self.key)
        except AttributeError:
            print("Please Choose File")

class DecryptWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Decrypt')
        self.resize(1000, 750)
        mainLayout = QVBoxLayout()
        self.btnOpenFile = QPushButton('Choose File')
        self.btnOpenFile.clicked.connect(self.openFileDialog)
        mainLayout.addWidget(self.btnOpenFile)
        self.btnGetText = QPushButton('Write The Key')
        self.btnGetText.clicked.connect(self.getText)
        mainLayout.addWidget(self.btnGetText)
        self.btnDecrypt = QPushButton('Decrypt')
        self.btnDecrypt.clicked.connect(self.decrypt)
        mainLayout.addWidget(self.btnDecrypt)
        self.setLayout(mainLayout)
    
    def openFileDialog(self):
        options = QFileDialog.Options()
        self.fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*);;Python Files (*.py)", options=options)
    def getText(self):
        self.key, self.ok = QInputDialog.getText(self, 'KEY ', 'Write Key:')
    def decrypt(self):
        try:
            if self.ok:
                try:
                    en = endec.Endec(self.fileName)
                    en.decrypting(self.key)
                except AttributeError:
                    print("Please Choose File")
        except AttributeError:
            print("Please write the key")



class AppDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1000 ,750)

        mainLayout = QVBoxLayout()

        self.btnEncrypt = QPushButton('Encrypt')
        self.btnEncrypt.clicked.connect(self.encrypt_window)
        mainLayout.addWidget(self.btnEncrypt)

        self.btnDecrypt = QPushButton('Decrypt')
        self.btnDecrypt.clicked.connect(self.decrypt_window)
        mainLayout.addWidget(self.btnDecrypt)

        self.setLayout(mainLayout)

    def encrypt_window(self):
        self.newWindow = EncryptWindow()
        self.newWindow.show()

    def decrypt_window(self):
        self.newWindow = DecryptWindow()
        self.newWindow.show()
