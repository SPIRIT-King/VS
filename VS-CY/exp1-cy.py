def vigenere_encrypt(plaintext, key):  
    """
    使用维吉尼亚密码，使用给定的密钥对给定的明文进行加码，生成加密之后的明文
    :param plaintext:给定的明文
    :param key:给定的密钥
    :return ciphertext:使用维吉尼亚密码生成的密文
    """
    ciphertext = ""  
    key_index = 0  
    for char in plaintext:  
        char = char.upper() 
        key_char = key[key_index].upper()  
        encrypted_char = chr(((ord(char) - ord('A')) + (ord(key_char) - ord('A'))) % 26 + ord('A'))  
        ciphertext += encrypted_char
        key_index += 1
    return ciphertext  


plaintext = "ATTACKATDAWN" # 明文
key = "LEMONLEMONLE" # 密钥
ciphertext = vigenere_encrypt(plaintext, key)
print(f"密文: {ciphertext}")