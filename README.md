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

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Random Password Generator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }
        .container {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .input-group {
            margin: 10px 0;
        }
        .input-group label {
            display: block;
            margin-bottom: 5px;
        }
        .input-group input {
            width: 100%;
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .button {
            background-color: #28a745;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .button:hover {
            background-color: #218838;
        }
        .output {
            margin-top: 20px;
            font-size: 1.2em;
            word-break: break-all;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Random Password Generator</h1>
    <div class="input-group">
        <label for="length">Password Length:</label>
        <input type="number" id="length" min="1" max="50">
    </div>
    <div class="input-group">
        <label for="specialChars">Include Special Characters:</label>
        <input type="checkbox" id="specialChars">
    </div>
    <div class="input-group">
        <label for="numbers">Include Numbers:</label>
        <input type="checkbox" id="numbers">
    </div>
    <button class="button" onclick="generatePassword()">Generate Password</button>
    <div class="output" id="output"></div>
</div>

<script>
    function generatePassword() {
        const stringChar = 'abcdefghijklmnopqrstuvwxyz';
        const stringNum = '0123456789';
        const specialChar = '~!@#$%^&*()';

        const length = parseInt(document.getElementById('length').value);
        const useSpecialChars = document.getElementById('specialChars').checked;
        const useNumbers = document.getElementById('numbers').checked;

        let password = '';
        
        for (let i = 0; i < length - 2; i++) {
            password += stringChar.charAt(Math.floor(Math.random() * stringChar.length));
        }
        
        if (useNumbers) {
            password += stringNum.charAt(Math.floor(Math.random() * stringNum.length));
        } else {
            password += stringChar.charAt(Math.floor(Math.random() * stringChar.length));
        }

        if (useSpecialChars) {
            password += specialChar.charAt(Math.floor(Math.random() * specialChar.length));
        } else {
            password += stringChar.charAt(Math.floor(Math.random() * stringChar.length));
        }

        document.getElementById('output').innerText = password;
    }
</script>

</body>
</html>


