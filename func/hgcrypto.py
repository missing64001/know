from cryptography.fernet import Fernet
import hashlib
import json
import getpass
import re


def main():
    text = """
asdfdgdfs
agfsdgsg
<mmde>
    gdsfgfsdg敢死队风格 哈哈娃娃
<mm>
<mmde>
    missing
<mm>
<mmde>
    52guoxiaodancaiguai
<mm>
    """
    lst = re.findall(r'\n<mmen>\n([\w\W]+)\n<mm>\n',text)


    mmc = mmCrypto()
    mmc.set_password('我擦擦')

    mec = mmc.mEncrypt(text)

    print(111111111111111111111111)
    print(mec)
    print(111111111111111111111111)



    mde = mmc.mDecrypt(mec)

    print(222222222222222222222)
    print(mde)
    print(222222222222222222222)
    # b = a.encrypt(text)
    # print(b)

    # b = a.decrypt(b)
    # print(b)

    # print(text == b)


class HgCrypto(object):
    def __init__(self, arg = None):
        self.arg = arg
        if arg == None:
            self.arg = getpass.getpass("F_Please input your password:")
        self.set_password(self.arg)
        
    def encrypt(self,text):
        encrypted_text = self.cipher.encrypt(text.encode('utf-8'))
        return encrypted_text.decode('utf-8')

    def decrypt(self,encrypted_text):
        decrypted_text = self.cipher.decrypt(encrypted_text.encode('utf-8')).decode('utf-8')
        return decrypted_text

    def set_password(self,str_input = None):
        if str_input == None:
            str_input = input("s_Please input your password:")
        sha1 = hashlib.sha1()
        sha1.update(str_input.encode())
        cipher_key = b'hg_' + sha1.hexdigest().encode() + b'='
        self.cipher = Fernet(cipher_key)

class mmCrypto(HgCrypto):
    def __init__(self):
        self.haspwd = False

    def set_password(self,pwd = None):
        if not pwd:
            self.haspwd = False
            return
        self.haspwd = True
        super().set_password(pwd)

    def encrypt(self,text):
        if not self.haspwd:
            return text
        encrypted_text = self.cipher.encrypt(text.encode('utf-8'))
        return encrypted_text.decode('utf-8')

    def mEncrypt(self,text):
        lst = re.findall(r'<mmde>\n([\w\W]+?)\n<mm>',text)
        for s in lst:
            ens = self.encrypt(s)
            ens = '<mmen>\n%s\n<mm>' % ens
            s = '<mmde>\n%s\n<mm>' % s
            text = text.replace(s,ens)
        return text

    def mDecrypt(self,text):
        try:
            lst = re.findall(r'<mmen>\n([\w\W]+?)\n<mm>',text)
            for s in lst:
                des = self.decrypt(s)
                des = '<mmde>\n%s\n<mm>' % des
                s = '<mmen>\n%s\n<mm>' % s
                text = text.replace(s,des)
        except Exception:
            pass
        return text

    # def decrypt(self,text):
    #     if not self.haspwd:
    #         return text
    #     try:
    #         decrypted_text = self.cipher.decrypt(text.encode('utf-8')).decode('utf-8')
    #     except Exception as e:
    #         print(e)
    #         decrypted_text = text
    #     return decrypted_text









if __name__ == '__main__':
    main()


