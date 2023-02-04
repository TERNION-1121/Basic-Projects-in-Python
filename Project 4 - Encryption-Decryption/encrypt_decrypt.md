# Encryption-Decryption

This program consists of an **Encryption** and **Decryption** algorithm, namely `encrypt()` and `decrypt()` respectively. 

## Functioning

The `encrypt()` function is an encryption algorithm which given a string `text` and an integer `n`, concatenates all the odd-indexed characters
of `text` with all the even-indexed characters of `text`, this process repeats 'n' times.

<br>
Following demonstrates the method through which the encryption logic is implemented :-

``` py
for times in range(n):
        odd = even = ''
        for i in range(1, len(encrypted), 2):
            odd+=encrypted[i]
        for i in range(0, len(encrypted), 2):
            even+=encrypted[i]
        encrypted = odd + even
```

<br>

The `decrypt()` function is an decryption algorithm which reverses the process.

```py
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
```

> If the string `text` is an empty value or the integer `n` is not positive, it return the first argument without changes.
