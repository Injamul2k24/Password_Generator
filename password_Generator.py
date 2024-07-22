import random

string_char = 'abdcegghijklmnporqstwvxyz'
string_num = '0123456789'
special_char = '~!@#$%^&*()'
 
def GeneratePassword(length, use_special_chars, use_numbers):
    """Generates a random password based on user preferences."""
    password = ''
    
    for _ in range(length-2):
        password += random.choice(string_char)
        
    if use_numbers:
        password = password + random.choice(string_num)
    else:
        password = password + random.choice(string_char)

    if use_special_chars:
        password = password + random.choice(special_char)
    else:
        password = password + random.choice(string_char)

    return password


length= int(input("how long password you want to generate "))
user_special_char = input("special character : Yes / no  :  ").lower()=='yes'
user_special_num= input("special number :yes/no ").lower() == 'yes'

password_Generate = GeneratePassword(length, user_special_char, user_special_num)
print("\nGenerate Password:", password_Generate)












