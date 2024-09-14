import qrcode

txt = input("Enter the text you want to encrypt: ")
save_as = input("Save as: ")
directory = "complete\\"
code = qrcode.make(txt)

code.save(
    directory+save_as+".png")


print("saved successfully!")
