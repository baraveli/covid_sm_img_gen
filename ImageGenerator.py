from PIL import Image, ImageDraw, ImageFont
import json

class ImageGenerator():

    def __init__(self,templates):
        self.template_data = templates



    #given data generate image
    def genImg(self,name,inpaint_data):
        #use the input and see if correct data is given
        input_as_set = set(inpaint_data.keys())
        #checks if correct data is provided
        if (name in self.template_data) and (input_as_set == set(self.template_data[name]["elements"])):
            print("raech")
            img = Image.open(self.template_data[name]["path"])
            #draw each element in template
            for e in self.template_data[name]["elements"]:
                #e_d is way to get elements in list to dict 
                e_d = self.template_data[name]["elements_data"][e]
                print(e_d)
                draw = ImageDraw.Draw(img)
                font = ImageFont.truetype(e_d["font"], e_d["font_size"])
                draw.text((e_d["cords"][0],e_d["cords"][1]),inpaint_data[e], font=font, fill =(e_d["fill"][0],e_d["fill"][1],e_d["fill"][2]))
            return img
        
        return None



