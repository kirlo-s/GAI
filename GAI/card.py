from PIL import Image,ImageDraw,ImageFont

#色選択
title_color = (38,255,223)
text_color = (255,255,255)
black=(0,0,0)
red = (255,138,52)
blue = (80,80,255)

#フォント選択
font_title = ImageFont.truetype("./font/Teko-Regular.ttf",100)
font_owner = ImageFont.truetype("./font/Teko-Regular.ttf",75)
font_time = ImageFont.truetype("./font/Teko-Regular.ttf",50)
font_prev = ImageFont.truetype("./font/OpenSans-Bold.ttf",30)
font_next = ImageFont.truetype("./font/OpenSans-Bold.ttf",25)

def generate(payload):
    #世代変更用コード,ベースを選択する
    if(payload["Gen"]):
        card = "./base/titlecard_orange.png"
    else:
        card = "./base/titlecard_blue.png"
    im = Image.open(card)
    draw = ImageDraw.Draw(im)
    
    #記入文字列
    server_name = payload["info"]["name"]
    owner = payload["owner"]
    time = "{}-{}".format(payload["time"]["start"],payload["time"]["end"])
    server_name = server_name    

    #文字列の描画
    draw.text((770,480),owner,font=font_owner,fill=text_color,anchor='rb')
    draw.text((50,100),server_name,font=font_title,fill=title_color)
    draw.text((320,550),time,font=font_time,fill=black)
    
    if(payload["Gen"]):
        draw.text((565,495),"PC/PS5/Xbox X,S",font=font_next,fill=black)
    else:
        draw.text((565,495),"PS4/Xbox One",font=font_prev,fill=black)
    
    #保存
    im.save("./cache/card.png")



