import hashlib

def compare(password: str, hash: str) -> bool:
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return True if hashed_password == hash else False