import os

def run_os_commands():
  os.system('pwd -L')
  os.system('echo $PWD')
  os.system('ls -lah')
  os.system(f'ping -c 4 google.com')
  # Get file size
  file_size = os.path.getsize('./files_to_encrypt/encryptme.txt')
  print(file_size)
  # It is better to use keys than these kinds of symmetric encryption
  # Encrypt a file (symmetric)
  os.system('openssl aes-256-cfb1 -pbkdf2 -iter 100000 < ./files_to_encrypt/encryptme.txt > ./files_to_encrypt/encryptme.txt.aes-256-cfb1')
  encrypt_file_size = os.path.getsize('./files_to_encrypt/encryptme.txt.aes-256-cfb1')
  print(encrypt_file_size)
  # Unencrypt a file
  os.system('openssl aes-256-cfb1 -pbkdf2 -iter 100000 -d < ./files_to_encrypt/encryptme.txt.aes-256-cfb1 > ./files_to_encrypt/encryptme.txt.decrypted')
  unencrypt_file_size = os.path.getsize('./files_to_encrypt/encryptme.txt.decrypted')
  print(unencrypt_file_size)
  # Zip and pw protect a zipfilewith zipfile (symmetric)
  os.system('zip -r --encrypt ./files_to_encrypt/folder_to_encrypt.zip ./files_to_encrypt/folder_to_encrypt/')

if __name__ == "__main__": 
    run_os_commands() 