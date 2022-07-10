def encrypt(text, n):
    encrypted = text
    for times in range(n):
        odd = even = ''
        for i in range(1, len(encrypted), 2):
            odd+=encrypted[i]
        for i in range(0, len(encrypted), 2):
            even+=encrypted[i]
        encrypted = odd + even
    return encrypted

def decrypt(encrypted, n):
    if encrypted == "" or n < 1: return encrypted
    else:
        mid=int(len(encrypted)/2)
        decrypted = encrypted
        for times in range(n):
            encrypted = decrypted
            decrypted = ""
            set1, set2 = encrypted[:mid], encrypted[mid:]
            for i in range(0, mid):
                decrypted+=set2[i]+set1[i]
            if len(encrypted)%2 != 0:
                decrypted+=set2[mid]
        return decrypted

print(encrypt('123456', 4))
print(decrypt(encrypt('123456', 4), 4))