import hashlib
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

# --------------- encrypt -------------------------------------
def applyHashing(val):
  m = hashlib.new("sha256", val)
  return m.digest()
  
def encryptData(data):
  global f
  token = f.encrypt(data)
  return token

def decryptData_s(data):
  global f
  token = f.decrypt(data).decode()
#   print(token)
  return token
def decryptData(data):
  global f
  token = f.decrypt(data)
  return token