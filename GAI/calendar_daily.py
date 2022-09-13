from datetime import datetime
from http import server
from PIL import Image,ImageDraw,ImageFont

#色設定
time_color = (38,255,223)
title_color = (16,16,16)

#フォント設定
font_time = ImageFont.truetype("./font/BF_Modernista-Regular.ttf",75)
font_title = ImageFont.truetype("./font/Teko-Regular.ttf",50)

class daily:
    def generate(self,payloads):
        base = "./base/daily.png"
        im = Image.open(base)
        draw = ImageDraw.Draw(im)
        
        #日付の取得
        date = datetime.strptime(payloads[0]["time"]["date"],"%Y-%m-%d")
        dstr = date.strftime("%y/%m/%d")
        
        #日付の書き込み
        draw.text((400,160),dstr,font=font_time,fill=time_color,anchor="mm")
        
        #カレンダー用座標
        event_x = [65,225,380,540,695,855,1010,1170,1325,1485,1640,1800,1940]
        event_y =[282,338,394,450,506,562,618,674,730]
        offset = 4
        
        for i in range(len(payloads)):
            start,end = self.hour_to_index(payloads[i])

            #世代ごとの色分け
            if(payloads[i]["Gen"]):
                color = (80,80,255)
            else:
                color = (255,138,52)
            
            #枠の描画    
            draw.rounded_rectangle((event_x[start],event_y[i],event_x[end],event_y[i+1]-offset), fill=color,radius=5)
            
            #サーバー名の書き込み
            servername = payloads[i]["info"]["name"]
            title = ""
            n = 0
            while(draw.multiline_textbbox((0, 0), title, font=font_title)[2] < (event_x[end]-event_x[start]) and n < len(servername)):
                title += servername[n]
                n += 1
            draw.text((event_x[start]+offset,event_y[i+1]-offset),title,font=font_title,fill=title_color,anchor="lb")        
            
        im.save("./cache/daily.png")
        
    
    def hour_to_index(self,payload):
        #時間をインデックスに変換する
        start = payload["time"]["start"]
        end = payload["time"]["end"]
        time_s = ["18:00","18:30","19:00","19:30","20:00","20:30","21:00","22:00","22:30","23:00","23:30","24:00"]
        start_n = time_s.index(start)
        end_n = time_s.index(end)
        return (start_n,end_n)