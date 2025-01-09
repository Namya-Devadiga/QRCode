import qrcode as qr
from PIL import Image

# Create a QRCode object with corrected parameters
qrc = qr.QRCode(
    version=1,
    error_correction=qr.constants.ERROR_CORRECT_H,
    box_size=10,  # Corrected here
    border=4,
)

# Add data to the QR code
qrc.add_data("https://www.linkedin.com/in/namyadp/")

# Make the QR code fit the data
qrc.make(fit=True)

# Create an image from the QR code
img = qrc.make_image(fill_color="red", back_color="white")

# Save the image
img.save("namya_linkedin.png")
