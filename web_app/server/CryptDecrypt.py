import hashlib
from cryptography.fernet import Fernet

# --------------- encrypt -------------------------------------
def applyHashing(val):
  m = hashlib.sha256(val)
  return m.hexdigest()
  
def encryptData(data, key):
  f = Fernet(key)
  token = f.encrypt(data)
  return token

def decryptData_s(data, key):
  f = Fernet(key)
  token = f.decrypt(data).decode()
#   print(token)
  return token

valor = "un texto"
print(applyHashing(valor.encode()))
print(type(applyHashing(valor.encode())))