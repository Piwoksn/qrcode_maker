import qrcode

txt = input("Enter the text you want to encrypt: ")
save_as = input("Save as: ")

code = qrcode.make(txt)

save = code.save(
    "C:\\Users\\ADMIN\\Desktop\\QRCode Maker\\complete\\"+save_as+".png")


print("saved successfully!")
