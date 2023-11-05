# XOR Cipher Program

## Description
This is a Python program for encrypting and decrypting files using the XOR cipher. The XOR cipher is a simple encryption technique that uses bitwise XOR operations to scramble the data. Please note that this encryption method is not suitable for secure applications and should be used for educational purposes only.

## Usage
1. Save the code into a Python file, e.g., "cipher.py."

2. Open a terminal or command prompt and navigate to the directory where you saved the Python file.

3. Run the program using the command: `python cipher.py`

4. The program will prompt you to choose between 'encrypt' and 'decrypt' actions. Follow the prompts for the chosen action:

   - If you choose 'encrypt':
     - Enter the input file location (the file you want to encrypt).
     - Enter the output file location (where the encrypted data will be saved).
     - A random key will be generated and used for encryption. The key will also be saved to a file named "OTP_key.bin."

   - If you choose 'decrypt':
     - Enter the input file location (the file you want to decrypt).
     - Enter the output file location (where the decrypted data will be saved).
     - You will be prompted to provide the key file location ("OTP_key.bin") generated during encryption.

5. The program will perform the selected action and provide feedback such as "File encrypted" or "File decrypted."

## Security Note
The XOR cipher is a basic encryption method and should not be used for security-critical applications. Ensure that the encryption key ("OTP_key.bin") is kept secure, as it is required for decryption. Losing the key will result in the inability to decrypt the file.

## Disclaimer
This program is intended for educational purposes and not for secure data protection. It's important to use established encryption methods for securing sensitive information.
