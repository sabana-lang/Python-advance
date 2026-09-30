class InvalidPasswordError(Exception):
  pass
try:
  n=input("Enter the password:")
  if (len(n))<8:
   raise InvalidPasswordError("Password should be 8 characters")
  else:
    print(n)
except InvalidPasswordError as e:
   print(e)