import string

ALPHABET = string.ascii_uppercase


def generate_key(message: str, keyword: str) -> str:
    key = keyword
    remain_length = len(message) - len(keyword)
    for i in range(remain_length):
        key += keyword[i]
    return key

def encrypt(message: str, keyword: str) -> str:
    cipher_text = ''
    key = generate_key(message, keyword)
    
    for i, char in enumerate(message):
        message_index = ALPHABET.find(char)
        key_index = ALPHABET.find(key[i])
        cipher_index = (message_index + key_index) % 26
        cipher_text += ALPHABET[cipher_index]
    
    return cipher_text

def decrypt(cipher: str, keyword: str) -> str:
    plain_text = ''
    key = generate_key(cipher, keyword)

    for i, char in enumerate(cipher):
        cipher_index = ALPHABET.find(char)
        key_index = ALPHABET.find(key[i])
        plain_index = (cipher_index - key_index + 26) % 26
        plain_text += ALPHABET[plain_index]
    
    return plain_text

if __name__ == '__main__':
    message = 'ATTACK'
    keyword = 'CAT'
    # print(generate_key(message, keyword))
    cipher = encrypt(message, keyword)
    print(cipher)
    
    print(decrypt(cipher, keyword))