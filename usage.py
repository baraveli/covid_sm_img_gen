from HeocTools import genVaccineImages



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
