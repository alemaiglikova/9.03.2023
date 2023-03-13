class Cipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, text):
        result = ''
        for char in text:
            if char.isalpha():
                char_code = ord(char.lower()) - 97
                new_char_code = (char_code + self.key) % 26
                new_char = chr(new_char_code + 97)
                result += new_char.upper() if char.isupper() else new_char
            else:
                result += char
        return result

    def decrypt(self, text):
        result = ''
        for char in text:
            if char.isalpha():
                char_code = ord(char.lower()) - 97
                new_char_code = (char_code - self.key) % 26
                new_char = chr(new_char_code + 97)
                result += new_char.upper() if char.isupper() else new_char
            else:
                result += char
        return result