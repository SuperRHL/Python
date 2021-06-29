username = input('What is your username? ')
password = input('What is your password? ')
password_length = len(password)
print(f'Hello {username}, your password, {"*"*password_length} is  {password_length} letters long!')