from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome(r"D:\Programs\Python\chromedriver.exe")
driver.get("https://www.worldometers.info/coronavirus/")


#/html/body/div[2]/div[3]/div/div[6]/div[1]/div/table/tbody[1]/tr[2]/td[2]/a 	india
#/html/body/div[3]/div[3]/div/div[6]/div[1]/div/table/tbody[1]/tr[3]/td[2]/a 	turakey
#/html/body/div[3]/div[3]/div/div[6]/div[1]/div/table/tbody[1]/tr[5]/td[14]/a 	pop
#/html/body/div[3]/div[3]/div/div[6]/div[1]/div/table/tbody[1]/tr[5]/td[5]		total deaths
#/html/body/div[3]/div[3]/div/div[6]/div[1]/div/table/tbody[1]/tr[1]/td[3]	 	total case 

asia_list = ["Japan", "Malaysia", "Myanmar", "S. Korea", "Thailand", "Singapore", "Cambodia", "Hong Kong", "Taiwan", "Laos"]
covid_list = []
for i in range(250):
	try :
		country = driver.find_element_by_xpath(f"/html/body/div[3]/div[3]/div/div[6]/div[1]/div/table/tbody[1]/tr[{i}]/td[2]").text
		total_case = driver.find_element_by_xpath(f"/html/body/div[3]/div[3]/div/div[6]/div[1]/div/table/tbody[1]/tr[{i}]/td[3]").text
		total_deaths = driver.find_element_by_xpath(f"/html/body/div[3]/div[3]/div/div[6]/div[1]/div/table/tbody[1]/tr[{i}]/td[5]").text
		popu = driver.find_element_by_xpath(f"/html/body/div[3]/div[3]/div/div[6]/div[1]/div/table/tbody[1]/tr[{i}]/td[14]").text

		total_case = int(total_case.replace(',',''))
		total_deaths = int(total_deaths.replace(',',''))
		popu = int(popu.replace(',',''))
		covid_list.append([country, total_case, total_deaths, popu])
	except:
		pass



df_covid = pd.DataFrame(covid_list, columns=["Country", "Total_case", "Total_deaths", "Populations"])
df_asia = df_covid[df_covid["Country"].isin(asia_list)]


df_asia["Death_per_1M"] = df_asia['Total_deaths'] / df_asia['Populations'] * 1000000
df_asia_srt = df_asia.sort_values("Country", ascending = True)
print(df_asia_srt)

df_asia_dead = df_asia[ df_asia["Death_per_1M"] > 50 ]
#print(df_asia_dead)



