from PIL import Image,ImageDraw,ImageFont
from util.imgutil import textbox

class card:
    #色選択
    title_color = (38,255,223)
    text_color = (255,255,255)
    black=(3,3,3)
    red = (255,138,52)
    blue = (80,80,255)

    #フォント選択
    font_owner = ImageFont.truetype("./font/Teko-Regular.ttf",75)
    font_time = ImageFont.truetype("./font/Teko-Regular.ttf",50)
    font_prev = ImageFont.truetype("./font/OpenSans-Bold.ttf",30)
    font_next = ImageFont.truetype("./font/OpenSans-Bold.ttf",25)
    font_title = ImageFont.truetype("./font/Teko-Regular.ttf",90)

    #設定用の仮置き
    card_width = 0
    card_height = 0
    owner_anchor = ""
    owner = (0,0)
    time = (0,0)
    gen = (0,0)
    card_prev = ""
    card_next = ""
    

    def generate_to_events(self,payload):
        #単体カード用設定
        self.card_width = 800
        #高さをオフセット含めて調節
        self.card_height = 350
        self.owner_anchor = "lb"
        self.owner = (40,330)
        self.time  = (320,350)
        self.gen = (565,295)
        self.card_prev = "./base/titlecard_orange_alt.png"
        self.card_next = "./base/titlecard_blue_alt.png"
        im = self._generate(payload)
        im = im.resize((600,300))
        return im
    
    def generate(self,payload):
        #単体カード用設定
        self.card_width = 800
        self.card_height = 600
        self.owner_anchor = "rb"
        self.owner = (770,480)
        self.time  = (320,550)
        self.gen = (565,495)
        self.card_prev = "./base/titlecard_orange.png"
        self.card_next = "./base/titlecard_blue.png"
        
        #生成
        im = self._generate(payload)
        im.save("./cache/card.png")

    def _generate(self,payload):
        #世代変更用コード,ベースを選択する
        if(payload["Gen"]):
            card = self.card_prev
        else:
            card = self.card_next
        im = Image.open(card)
        draw = ImageDraw.Draw(im)
        
        #記入文字列
        server_name = payload["info"]["name"]
        owner = payload["owner"]
        time = "{}-{}".format(payload["time"]["start"],payload["time"]["end"])
        
        #タイトルの整形
        title = textbox().card_title(server_name)
        
        #文字列の描画
        draw.text(self.owner,owner,font=self.font_owner,fill=self.text_color,anchor=self.owner_anchor)
        draw.text(self.time,time,font=self.font_time,fill=self.black)

        #センタリングの実装
        bbox = draw.multiline_textbbox((0, 0), title, font=self.font_title)
        title_x = (self.card_width // 2) - ((bbox[2] - bbox[0])//2)
        title_y = (self.card_height // 2) - ((bbox [3] - bbox[1])//2)  
        #タイトル描画
        draw.text((title_x,title_y),title,font=self.font_title,fill=self.title_color)
        
        if(payload["Gen"]):
            draw.text(self.gen,"PC/PS5/Xbox X,S",font=self.font_next,fill=self.black)
        else:
            draw.text(self.gen,"PS4/Xbox One",font=self.font_prev,fill=self.black)
        
        return im



