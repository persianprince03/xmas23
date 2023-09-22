import qrcode

img = qrcode.make('http://linkedin.com/in/parsa-divanbeigi/')

img.save('MyQRCode1.png')
