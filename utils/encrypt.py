import hashlib
import time


def pwd_encrypt(pwd_str: str):
    hash_obj = hashlib.sha3_256(pwd_str.encode("utf-8"))
    salt = str(time.time()).replace('.', '')
    hash_obj.update(salt.encode("utf-8"))
    return hash_obj.hexdigest()


if __name__ == '__main__':
    print(pwd_encrypt("123456"))
