import qrcode # uses pillow library in background

image = qrcode.make("https://127.0.0.1:8000")
image.save("qr.png")