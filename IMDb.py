#name
#/html/body/div[4]/div/div[2]/div[3]/div/div[1]/div/span/div/div/div[3]/table/tbody/tr[1]/td[2]/a
#/html/body/div[4]/div/div[2]/div[3]/div/div[1]/div/span/div/div/div[3]/table/tbody/tr[1]/td[2]/a
#/html/body/div[4]/div/div[2]/div[3]/div/div[1]/div/span/div/div/div[3]/table/tbody/tr[2]/td[2]/a
#/html/body/div[4]/div/div[2]/div[3]/div/div[1]/div/span/div/div/div[3]/table/tbody/tr[3]/td[2]/a

#rating
#/html/body/div[4]/div/div[2]/div[3]/div/div[1]/div/span/div/div/div[3]/table/tbody/tr[1]/td[3]/strong
#/html/body/div[4]/div/div[2]/div[3]/div/div[1]/div/span/div/div/div[3]/table/tbody/tr[2]/td[3]/strong
#/html/body/div[4]/div/div[2]/div[3]/div/div[1]/div/span/div/div/div[3]/table/tbody/tr[3]/td[3]/strong


#url




from selenium import webdriver
import pandas as pd
#import pyautogui as pg


driver = webdriver.Chrome(r"D:\Programs\Python\chromedriver.exe")
driver.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")

movie_list = []
for i in range(20):
	try:
		movie 	= driver.find_element_by_xpath(f"/html/body/div[4]/div/div[2]/div[3]/div/div[1]/div/span/div/div/div[3]/table/tbody/tr[{i}]/td[2]/a").text
		rating 	= driver.find_element_by_xpath(f"/html/body/div[4]/div/div[2]/div[3]/div/div[1]/div/span/div/div/div[3]/table/tbody/tr[{i}]/td[3]/strong").text
		link 	= driver.find_element_by_xpath(f"/html/body/div[4]/div/div[2]/div[3]/div/div[1]/div/span/div/div/div[3]/table/tbody/tr[{i}]/td[2]/a")
		link_g 	= link.get_attribute('href')
		movie_list.append([movie, rating, link_g])
	except:
		pass

df_movie = pd.DataFrame(movie_list, columns=["Movies", "Rating", "Link"])
print(df_movie.head())



driver.quit()