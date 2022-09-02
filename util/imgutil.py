from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import math
import textwrap

class textbox:
    def card_title(self,text):
        text = text.upper()
        l = text.split(" ")
        #文字列整形
        list = [""]
        n = 0
        i = 0
        while i < len(l):
            print(i)
            if len(list[n]) <= 15:
                list[n] += l[i] + " "
            else:
                list.append("")
                n +=1
                i -=1
            i +=1
        
        print(list)
        #段落作成
        formatted = ""
        indent = "   "
        for i in range(len(list)): 
            formatted += list[i] + "\n" + indent
            indent += indent
        return formatted
        