import unittest
import os
import tempfile
from chiper import generate_random_key, xor_encrypt, xor_decrypt

class TestXORCipher(unittest.TestCase):
    def test_encryption_decryption_temp_files(self):
        plaintext = b"Hello, World!"
        key = os.urandom(len(plaintext))

        with tempfile.NamedTemporaryFile(delete=False) as input_file, \
             tempfile.NamedTemporaryFile(delete=False) as encrypted_file, \
             tempfile.NamedTemporaryFile(delete=False) as decrypted_file:

            input_file.write(plaintext)
            input_file.seek(0)

            # Encrypt the data
            xor_encrypt(input_file.name, encrypted_file.name, key)

            # Decrypt the data
            xor_decrypt(encrypted_file.name, decrypted_file.name, key)

            with open(decrypted_file.name, 'rb') as decrypted_data:
                decrypted_content = decrypted_data.read()
                self.assertEqual(plaintext, decrypted_content)

    def test_encryption_decryption(self):
        test_folder = 'test_files'
        output_folder = 'output'
        file_list = os.listdir(test_folder)

        # Create output directory if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # For each file in the test folder
        for file_name in file_list:
            file_path = os.path.join(test_folder, file_name)
            key = generate_random_key(os.path.getsize(file_path))

            encrypted_file_path = os.path.join(output_folder, f"encrypted_{file_name}")
            decrypted_file_path = os.path.join(output_folder, f"decrypted_{file_name}")
            key_file_path = os.path.join(output_folder, f"key_{file_name}")

            with open(file_path, 'rb') as input_file, \
                 open(encrypted_file_path, 'wb') as encrypted_file, \
                 open(decrypted_file_path, 'wb') as decrypted_file, \
                 open(key_file_path, 'wb') as key_file:

                # Encrypt the data
                xor_encrypt(input_file.name, encrypted_file.name, key)

                # Save the key
                key_file.write(key)

                # Decrypt the data with same key
                xor_decrypt(encrypted_file.name, decrypted_file.name, key)

                with open(decrypted_file.name, 'rb') as decrypted_data:
                    decrypted_content = decrypted_data.read()
                    input_data = input_file.read()
                    self.assertEqual(input_data, decrypted_content)

if __name__ == '__main__':
    unittest.main()
