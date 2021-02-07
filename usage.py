from HeocTools import genVaccineImages,genCovidStatusImages

covid_data = {
    "date":"4/2/2021",
    "new_cases":"90",
    "samples":"3000",
    "in_hospitals":"789",
    "active_cases":"1498",
    "total_confirmed":"15,790",
    "total_samples":"9000",
    "total_recoveries":"8999",
    "total_deaths":"5876",
    "positive_deaths":"34",

}

vaccine_sm_data = {
    "date":"04/2/2021",
    "today":"120",
    "male_area":"134",
    "atoll":"456",
    "total":"899",
    "total_male":"990",
    "total_atolls":"890",
    "vacc_cen_male":"10",
    "vacc_cen_atoll":"100"
}


vacc_im = genVaccineImages(vaccine_sm_data)


vacc_im[0].save("vacc_sm.png")
vacc_im[1].save("vacc_im.png")

covid_im = genCovidStatusImages(covid_data)
covid_im.show()
