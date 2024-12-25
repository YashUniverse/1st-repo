import qrcode

data = "https://www.youtube.com/"

qr = qrcode.QRCode(
    version=2,  
    error_correction=qrcode.constants.ERROR_CORRECT_L,  
    box_size=10,  
    border=4, 
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")


img.save("qrcode1.png")

print("QR Code generated and saved as 'qrcode.png'")
