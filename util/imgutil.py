from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import math
import textwrap

class textbox:
    def card_title(self,text):
        text = text.upper()
        list = textwrap.wrap(width=20,text=text)
        
        #段落作成
        formatted = ""
        indent = "   "
        for i in range(len(list)): 
            formatted += list[i] + "\n" + indent
            indent += indent
        return formatted
        