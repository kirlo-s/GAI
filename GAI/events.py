from time import strftime
from PIL import Image,ImageDraw,ImageFont
from util.imgutil import textbox
from GAI import card 
from datetime import datetime

#色選択
title_color = (38,255,223)
text_color = (255,255,255)
black=(3,3,3)
red = (255,138,52)
blue = (80,80,255)

#フォント選択
font_owner = ImageFont.truetype("./font/Teko-Regular.ttf",75)
font_time = ImageFont.truetype("./font/Teko-Regular.ttf",100)
font_prev = ImageFont.truetype("./font/OpenSans-Bold.ttf",30)
font_next = ImageFont.truetype("./font/OpenSans-Bold.ttf",25)
font_title = ImageFont.truetype("./font/BF_Modernista-Regular.ttf",130)


class events:
    def generate(self,payloads):
        #payloadsには同じ日付のエントリのリストを与える
        #最大8個まで
        base = "./base/events.png"
        im = Image.open(base)
        draw = ImageDraw.Draw(im)
        
        #日付の取得
        date = datetime.strptime(payloads[0]["time"]["date"],"%Y-%m-%d")
        dstr = date.strftime("%y/%m/%d")
        
        #イベントのタイトル部分
        x_offset = 50
        y_offset = 50
        draw.text((x_offset,y_offset),"EVENTS",font=font_title,fill=title_color)
        draw.text((x_offset+ 6, y_offset+150),dstr,font=font_time,fill=title_color)
        
        #カード位置
        cards_xy =[(672,30),(57,345),(672,345),(57,655),(672,655),(57,970),(672,970),(57,1285)]
        #マスク用画像
        mask = Image.open("./base/card_mask.png").convert("1")
        
        for i in range(len(payloads)):
            card_xy = cards_xy[i]
            c = card.card().generate_to_events(payloads[i])
            im.paste(c,card_xy,mask=mask)
            
        #リサイズ
        img_h = cards_xy[len(payloads)-1][1] + 330
        im = im.crop((0,0,1329,img_h))    
        #保存
        im.save("./cache/events.png")
    