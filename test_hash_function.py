# test_hash_function.py
from werkzeug.security import generate_password_hash, check_password_hash

password = "1234"
hashed_password = generate_password_hash(password)
print(hashed_password)
print(check_password_hash(hashed_password, password))  # Should print True
print(check_password_hash(hashed_password, "wrong password"))  # Should print False
