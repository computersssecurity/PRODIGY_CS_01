def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - base - shift) % 26 + base)
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

def main():
    try:
        ciphertext = input("Enter the encrypted message: ")
        shift = int(input("Enter the shift value (positive integer): "))

        decrypted_message = caesar_decrypt(ciphertext, shift)
        print("Decrypted message:", decrypted_message)

    except ValueError:
        print("Invalid input. Please enter a valid shift value (positive integer).")

if __name__ == "__main__":
    main()
