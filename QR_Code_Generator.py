import qrcode
from PIL import Image
QR = qrcode.QRCode(version = 7,error_correction  = qrcode.constants.ERROR_CORRECT_Q, 
                   box_size = 7, border = 7)
QR.add_data("https://github.com/Sahilinsan186")
QR.make(fit = True)
img = QR.make_image(fill_color = "Black",back_color= "White")
img.save("QR_Code.png")