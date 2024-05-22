from comparator import compare

with open("rockyou.txt", "r", encoding='latin-1') as file:
    passwords = [line.replace('\n', '') for line in file.readlines()]

with open("hash.txt") as file:
    hash = file.read()

for password in passwords:
    if compare(password, hash):
        print(f"Cracked! -> '{password}'")
        break
else: print("Couldn't crack the password.")