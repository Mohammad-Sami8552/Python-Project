import qrcode as qr
qrCode=qr.QRCode(version=1, error_correction=qr.constants.ERROR_CORRECT_L, box_size=20,
                border=1 )
qrCode.add_data("https://www.youtube.com/watch?v=Il4xRZ66vmo")
qrCode.make(fit=True)
img=qrCode.make_image(fill='red', back_color='blue')
img.save("Tujhe Dekha To Ye Jana Sanam.png")
