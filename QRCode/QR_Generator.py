import qrcode as qr
from PIL import Image, ImageDraw, ImageFont

# Create a QRCode object with corrected parameters
qrc = qr.QRCode(
    version=1,
    error_correction=qr.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Add data to the QR code
qrc.add_data("https://www.linkedin.com/in/namyadp/")

# Make the QR code fit the data
qrc.make(fit=True)

# Create an image from the QR code with customized colors
img = qrc.make_image(fill_color="red", back_color="white").convert('RGB')

# Load an existing logo or watermark to embed in the center of the QR code (optional)
logo = Image.open(r'C:\Users\ASUS\Desktop\QRCode\logo.png')  # Replace with the correct path to your logo file
logo = logo.resize((100, 100))  # Resize the logo to fit inside the QR code

# Ensure the logo has an alpha channel for transparency
logo = logo.convert("RGBA")

# Calculate the position for the logo in the center
logo_position = (
    (img.size[0] - logo.size[0]) // 2,
    (img.size[1] - logo.size[1]) // 2
)

# Paste the logo onto the QR code image with transparency
img.paste(logo, logo_position, mask=logo)

# Add a title or description below the QR code (optional)
title = "Scan to Connect on LinkedIn"
font = ImageFont.truetype("arial.ttf", 18)  # Load a font of your choice
draw = ImageDraw.Draw(img)
# Calculate text size using textbbox to get bounding box dimensions
bbox = draw.textbbox((0, 0), title, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
text_position = ((img.size[0] - text_width) // 2, img.size[1] - text_height - 10)
draw.text(text_position, title, fill="black", font=font)

# Save the final image with the QR code, logo, and title
img.save("namya_linkedin_with_logo.png")

