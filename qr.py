import qrcode
from PIL import Image 

qr=qrcode.QRCode(box_size=7,border=2)
qr.add_data("https://shop.mattel.com/pages/barbie")
qr.make(fit=True)
img=qr.make_image(fill_color="hotpink",back_color="black")
img.save("yy.png")