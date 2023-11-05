"""Main module for the XOR cipher program."""
import os

def generate_random_key(file_size):
    """Generate a random key of the same size as the input file."""
    return os.urandom(file_size)

def xor_encrypt(input_file, output_file, key):
    """Encrypt the input file using the XOR cipher."""
    with open(input_file, 'rb') as file_in, open(output_file, 'wb') as file_out:
        data = file_in.read()
        encrypted_data = bytes(a ^ b for a, b in zip(data, key))
        file_out.write(encrypted_data)

def xor_decrypt(input_file, output_file, key):
    """Decrypt the input file using the XOR cipher."""
    with open(input_file, 'rb') as file_in, open(output_file, 'wb') as file_out:
        data = file_in.read()
        decrypted_data = bytes(a ^ b for a, b in zip(data, key))
        file_out.write(decrypted_data)

if __name__ == "__main__":

    action = input("Type 1 to encrypt, 2 to decrypt file: ").strip()
    input_file = input("Enter the input file location: ").strip()
    output_file = input("Enter the output file location: ").strip()

    if action == '1':
        # Generate a random key of the same size as the input file. 
        # It is a common practice in one-time pad (OTP) encryption
        # to have a key that is at least as long as the plaintext
        key = generate_random_key(os.path.getsize(input_file))
        # Encrypt the file and save the key to a file
        xor_encrypt(input_file, output_file, key)
        with open("OTP_key.bin", 'wb') as key_out:
            key_out.write(key)
        print("File encrypted and key saved to OTP_key.bin in output folder")

    elif action == '2':
        key_file = input("Enter the OTP key file location: ").strip()
        with open(key_file, 'rb') as key_in:
            key = key_in.read()
        xor_decrypt(input_file, output_file, key)
        print("File decrypted")
    else:
        print("Invalid action. Use '1' or '2'.")
