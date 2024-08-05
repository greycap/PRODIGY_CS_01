class CaesarCipher:
    def __init__(self, shift: int):
        self.shift = shift

    def _shift_char(self, char: str, shift_amount: int) -> str:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            shifted = (ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset
            return chr(shifted)
        return char

    def encrypt(self, message: str) -> str:
        return ''.join(self._shift_char(char, self.shift) for char in message)

    def decrypt(self, encrypted_message: str) -> str:
        return ''.join(self._shift_char(char, -self.shift) for char in encrypted_message)

def main():
    print("Welcome to the Caesar Cipher Program!")
    while True:
        try:
            shift = int(input("Enter the shift value (1-25): "))
            if 1 <= shift <= 25:
                break
            print("Please enter a valid shift value.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    cipher = CaesarCipher(shift)

    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
        if choice in ['e', 'd']:
            message = input("Enter your message: ")
            if choice == 'e':
                print("Encrypted message:", cipher.encrypt(message))
            else:
                print("Decrypted message:", cipher.decrypt(message))
            break
        else:
            print("Invalid choice! Please enter 'e' or 'd'.")

if __name__ == "__main__":
    main()