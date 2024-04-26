from cryptography.fernet import Fernet
class Endec():
    def __init__(self,file_path):
        self.file_path = file_path
    
    def encrypting(self):
        key =  Fernet.generate_key()
        with open("Thekey.key","wb") as Thekey:
            Thekey.write(key)
        with open(self.file_path,"rb") as file:
            file = file.read()
            encrypted_file = Fernet(key).encrypt(file)
        with open(self.file_path,"wb") as file:
            file.write(encrypted_file)
        return key
    def decrypting(self,de_key):
        with open(self.file_path,"rb") as file:
            file = file.read()
            decrypted_file = Fernet(de_key).decrypt(file)
        with open(self.file_path,"wb") as file:
            file.write(decrypted_file)
