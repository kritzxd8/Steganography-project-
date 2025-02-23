import cv2
import os

# Load the image
img = cv2.imread("mypic.jpg")  # Ensure this path is correct
if img is None:
    print("Error: Image not found!")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Append a termination character to mark the end of the message
msg += "#"

height, width, _ = img.shape
max_chars = height * width * 3  # Maximum characters that can be stored

# Ensure message fits within the image
if len(msg) > max_chars:
    print("Message is too long for this image!")
    exit()

# Embed message into the image
n, m, z = 0, 0, 0
for char in msg:
    img[n, m, z] = ord(char)  # Convert character to ASCII
    z += 1
    if z == 3:
        z = 0
        m += 1
        if m == width:
            m = 0
            n += 1

# Save the encrypted image as PNG to prevent compression
cv2.imwrite("encryptedImage.png", img)
print("Message encrypted successfully!")

# Store the password in a file
with open("password.txt", "w") as f:
    f.write(password)

# Open the encrypted image (Windows)
os.system("start encryptedImage.png")
