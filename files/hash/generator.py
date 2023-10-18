import hashlib

password = "test123!#"

with open("hash.txt", "w") as file:
    file.write(hashlib.sha256(password.encode()).hexdigest())