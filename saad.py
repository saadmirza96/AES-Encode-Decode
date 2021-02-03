############################################################################
####                Muhammad Saad (21-10342) Info security              ####
############################################################################

from cryptography.fernet import Fernet

def write_any_key():
    """
    This functon will generates a key and save it into a file key.key
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as k_file:
        k_file.write(key)


def load_pre_key():
    """
    Loads the key from the current directory named `key.key` and decrypt that key
    """
    return open("key.key", "rb").read()

# I am writing running method of code below

# First you have to install crytography by using below command on terminal
#   pip3 install cryptography
# Now write commands on IDLE shell by using your own variables

# write_any_key()
# key = load_pre_key()
# UserMsg = "I am a human".encode()
# print(UserMsg)

# encodeMsg = Fernet (key)
# encryptMsg =encodeMsg.encrypt(UserMsg)
# print(encryptMsg)
# upper command also print encrypted code on shell
# Now you have to convert key.key file in key.txt to see ecrypted code
# decryptMsg = encodeMsg.decrypt (encryptMsg)
# print(decryptMsg)
# Upper command again convert in decrypted form

