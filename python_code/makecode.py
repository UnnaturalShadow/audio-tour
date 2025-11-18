#simple python template to generate a qrcode for a given url.

import qrcode

# Data to encode in the QR code
data = "https://moa.byu.edu"

# Generate the QR code image
img = qrcode.make(data)

# Save the image to a file
img.save("my_qrcode.png")