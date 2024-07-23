<h1> Random Password Generator</h1> 
This is a simple Python script to generate random passwords based on user preferences. The script allows you to specify the length of the password and whether to include special characters and numbers.

<h3>Features</h3>
Customizable Length: Specify the desired length of your password.
Special Characters: Choose whether to include special characters.
Numbers: Choose whether to include numbers.
Simple and Easy to Use: User-friendly input prompts to guide you through the process.
<h5>Usage</h5>
1. Clone the repository:

```sh
git clone https://github.com/injamul2k24/password_generator.git
```

2. Navigate to the project directory:
    ```sh
    cd password_generator
    ```

3. Run the script:
    ```sh
    python password_generator.py
    ```

4. Follow the prompts to generate your password.
<h5>Example</h5>

 ```sh
 $ python password_generator.py
How long password do you want to generate? 12
Include special characters? Yes/No: Yes
Include numbers? Yes/No: Yes

Generated Password: aB!9zL@3xN2p
```
<h5>Code</h5>
 <p>Here is the code for the password generator:</p>

  ```sh
 import random

string_char = 'abcdefghijklmnopqrstuvwxyz'
string_num = '0123456789'
special_char = '~!@#$%^&*()'

def GeneratePassword(length, use_special_chars, use_numbers):
    """Generates a random password based on user preferences."""
    password = ''
    
    for _ in range(length-2):
        password += random.choice(string_char)
        
    if use_numbers:
        password += random.choice(string_num)
    else:
        password += random.choice(string_char)

    if use_special_chars:
        password += random.choice(special_char)
    else:
        password += random.choice(string_char)

    return password

length = int(input("How long password do you want to generate? "))
use_special_chars = input("Include special characters? Yes/No: ").lower() == 'yes'
use_numbers = input("Include numbers? Yes/No: ").lower() == 'yes'

generated_password = GeneratePassword(length, use_special_chars, use_numbers)
print("\nGenerated Password:", generated_password)
```
<big>Feel free to contribute to this project by making suggestions or adding new features. Your feedback is welcome!</big>
