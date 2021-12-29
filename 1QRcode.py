# you can generate a qr code using this code.
import qrcode
import image
var1=input("Enter any text here: ")
img= qrcode.make(var1)
img.save("1.jpg")
