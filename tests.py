from PIL import Image
from ImageGenerator import ImageGenerator
import json


#load template file
with open('templates.json') as f:
    templates = json.load(f)



generator = ImageGenerator(templates)


covid_data = {
    "date":"4/2/2021",
    "new_cases":"200",
    "samples":"3000",
    "in_hospitals":"789",
    "active_cases":"1498",
    "total_confirmed":"15,790",
    "total_samples":"9000",
    "total_recoveries":"8999",
    "total_deaths":"5876",
    "positive_deaths":"34",

}


gen_img = generator.genImg("covid_alert",covid_data) 
gen_img.show()
