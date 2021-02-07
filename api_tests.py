

from HeocTools import genVaccineImages,genCovidStatusImages,getLatestCovidStatus,genCovidImagesFromApi



data = getLatestCovidStatus()
print(data)

gen_img = genCovidImagesFromApi()
gen_img.show()