import hashlib

password = "Fd7!"

with open("files\\hash\\hash.txt", "w") as file:
    file.write(hashlib.sha256(password.encode()).hexdigest())