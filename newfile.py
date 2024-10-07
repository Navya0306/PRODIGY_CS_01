def caesar_cipher_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_message += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_message += char
    return encrypted_message

def caesar_cipher_decrypt(message, shift):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_message += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_message += char
    return decrypted_message

def main():
    choice = input("Would you like to (E)ncrypt or (D)ecrypt? ").upper()
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'E':
        print("Encrypted message:", caesar_cipher_encrypt(message, shift))
    elif choice == 'D':
        print("Decrypted message:", caesar_cipher_decrypt(message, shift))
    else:
        print("Invalid choice! Please select 'E' for encryption or 'D' for decryption.")

if __name__ == "__main__":
    main()