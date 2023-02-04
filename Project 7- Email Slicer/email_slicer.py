def emailSlicer(email):
    username = email.split('@')[0]
    domain = email.split('@')[1]
    return username, domain
emailID = 'ternion205stylo@gmail.com'
print(emailSlicer(emailID))