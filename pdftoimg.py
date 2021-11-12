print("""
+-+-+-+ +-+-+ +-+-+-+ 
|P|D|F| |T|O| |I|M|G| 
+-+-+-+ +-+-+ +-+-+-+ V1.0 \

DEVELOPED BY YATHARTH 
IG : im.yatharth
GITHUB : yatharthgeek
YOUTUBE : Technical Know

""")


import os

while 1==1:
    
    bash = input("[CONVERTER] >> ")
    
    if bash =="start":
        imgformat=input("[IMAGE FORMAT] >> ")
        pdfpath=input("[PDF PATH] >> ")
        imgpath=input("[IMAGE PATH] >> ")
        
        code = "pdftoppm -"+imgformat+" "+pdfpath+" "+imgpath
        os.system(code)
    
    
    if bash=="help":
        print("Help will upload soon")
    
    
    
    
    
    if bash=="exit":
        break
    
        
    
    
