import cv2

# Load encrypted image
img = cv2.imread("encryptedImage.png")  # Use PNG to prevent compression issues
if img is None:
    print("Error: Encrypted image not found!")
    exit()

# Read the stored password
try:
    with open("password.txt", "r") as f:
        stored_password = f.read().strip()
except FileNotFoundError:
    print("Error: Password file not found!")
    exit()

# Ask for the decryption passcode
pas = input("Enter passcode for Decryption: ")
if pas != stored_password:
    print("YOU ARE NOT AUTHORIZED!")
    exit()

message = ""
n, m, z = 0, 0, 0

height, width, _ = img.shape

# Extract message from the image
while True:
    char = chr(int(img[n, m, z]))  # Ensure correct ASCII retrieval
    if char == "#":  # Stop at termination character
        break
    message += char
    z += 1
    if z == 3:
        z = 0
        m += 1
        if m == width:
            m = 0
            n += 1

print("\nDecryption successful! Secret message:", message)
