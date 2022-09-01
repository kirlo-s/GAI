from PIL import Image,ImageDraw,ImageFont

def placeholder(payload):
    text = 'PLACEHOLDER'             # 画像に追加する文字列を指定
    img = Image.new("RGB",(800,600),(22,22,22)) # 入力ファイルを指定

    imagesize = img.size        # img.size[0]は幅、img.size[1]は高さを表す
    draw = ImageDraw.Draw(img)  # ImageDrawオブジェクトを作成

    font = ImageFont.truetype("./font/Roboto-Regular.ttf", 64)  # フォントを指定、64はサイズでピクセル単位
    log = ImageFont.truetype("./font/Roboto-Regular.ttf",20)
    size = font.getsize(text)

    # 画像右下に'Sampleと表示' #FFFは文字色（白）
    draw.text((400,300), text, font=font,anchor="mm" ,fill='#26FFDF')
    draw.text((10,350), str(payload),font=log)
    # ファイルを保存
    return img
    
