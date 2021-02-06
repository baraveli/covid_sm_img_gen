from PIL import Image
from ImageGenerator import ImageGenerator
import json


#load template file
with open('templates.json') as f:
    templates = json.load(f)


def genVaccineImages(vaccine_data,templates=templates):
    generator = ImageGenerator(templates)
    #strip values for ig image
    vaccine_data_ig = vaccine_data.copy()
    vaccine_data_ig.pop("vacc_cen_male")
    vaccine_data_ig.pop("vacc_cen_atoll")
    #gen images
    gen_sm = generator.genImg("vaccine_sm",vaccine_data)
    gen_ig = generator.genImg("vaccine_ig",vaccine_data_ig)

    if gen_sm != None and gen_ig != None:
        return (gen_sm,gen_ig)

    return None