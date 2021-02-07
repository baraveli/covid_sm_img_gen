from PIL import Image
from ImageGenerator import ImageGenerator
import json
import requests
import datetime


#load template file
with open('templates.json') as f:
    templates = json.load(f)


headers = {
    'authority': 'covid19.health.gov.mv',
    'cache-control': 'no-cache',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'image',
    'accept-language': 'en-US,en;q=0.9',
    'cookie': '__cfduid=d9236ffa50f8602e8e44dbb5e278465001612694245',
    'pragma': 'no-cache',
    'referer': 'https://covid19.health.gov.mv/data2.json',
}

covid_data = {
        "date":"",
        "new_cases":"",
        "samples":"",
        "in_hospitals":"",
        "active_cases":"",
        "total_confirmed":"",
        "total_samples":"",
        "total_recoveries":"",
        "total_deaths":"",
        "positive_deaths":"",
}






def getLatestCovidStatus(headers=headers,covid_data=covid_data):
    covid_data = covid_data.copy()


    req = requests.get("https://covid19.health.gov.mv/data2.json",headers=headers)
    json_data = json.loads(req.text)
    #handle dates
    fetched_date = json_data["updated_date"]
    date_time_obj = datetime.datetime.strptime(fetched_date,'%d %B %Y - %H:%M')
    #weeee safettly
    covid_data["date"] = date_time_obj.strftime("%m/%d/%Y")
    covid_data["new_cases"] = json_data["case_insert_count"]
    covid_data["samples"] = json_data["today_sample_tested"]
    covid_data["in_hospitals"] = ""
    covid_data["active_cases"] = json_data["display_cases_active"]
    covid_data["total_confirmed"] = json_data["cases_total"]
    covid_data["total_samples"] = json_data["total_sample_tested"]
    covid_data["total_recoveries"] = json_data["display_cases_recovered"]
    covid_data["total_deaths"] = json_data["display_cases_deaths"]
    covid_data["positive_deaths"] = ""



    return covid_data





def genCovidStatusImages(covid_data,templates=templates):
    generator = ImageGenerator(templates)
    #get new cases
    new_cases = int(covid_data["new_cases"])

    if new_cases > 100:
        gen_img = generator.genImg("covid_alert",covid_data)
        return gen_img

    #if cases less than 100 return normal img
    gen_img = generator.genImg("covid_normal",covid_data)
    return gen_img




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




def genCovidImagesFromApi():
    try:

        covid_data = getLatestCovidStatus()
        imgs = genCovidStatusImages(covid_data)

    except:
        return None

    return imgs
    
