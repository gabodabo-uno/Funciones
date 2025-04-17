
# -*- coding: utf-8 -*-
# Check webpage for ChromeDriver version:
#https://googlechromelabs.github.io/chrome-for-testing/#stable
#

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import numpy as np
import pandas as pd

save_path = './Salidas_Code/Archivos'


options = webdriver.ChromeOptions()
browser = webdriver.Chrome()
# Para lo actual
browser.get('https://www.etoro.com/people/fyanezn/portfolio')
time.sleep(10)
# Para las comparas
# browser.get('https://www.etoro.com/people/fyanezn/portfolio/history')



xpath_main = '/html/body/app-root/et-layout-main/div/div[2]/div[2]/div[2]/div/ui-layout/ng-view/et-user/div/div[4]/et-public-portfolio/et-public-portfolio-overview/et-public-portfolio-overview-list/et-table/div[2]'
# Content
xpath_main2 = '//et-public-portfolio-overview-list/et-table/div[2]'
tab_cont2 = browser.find_elements(By.XPATH,
                                xpath_main2+'/*')

# Sale 15, [0] es la fecha de actualización [-1] es vacío. En total hay 13 assets

n_assets2 = len(tab_cont2)
print(n_assets2)
col_names = ['ticker', 'nombre', 'direction', 'invested_ptj', 'prof_loss_ptj', 'value_ptj', 'na1', 'sell','na2', 'buy']
df_save = pd.DataFrame(columns=col_names)
for x in range(2, n_assets2):
    # el_ticker = browser.find_element(By.XPATH,xpath_main2+f'/div[{x}]/div/div[1]/div/div/div[1]').text
    el_ticker = browser.find_element(By.XPATH,xpath_main2+f'/div[{x}]/div[1]').text
    print(el_ticker)
    valores = el_ticker.replace(' ', '_').split()
    df_tmp = pd.DataFrame(np.array(valores).reshape(1,-1), index=[0], columns=col_names)
    df_save = pd.concat([df_save, df_tmp])
df_save.to_excel('./Salidas_Code/Archivos/df_save.xlsx', index=False)
#     el_detail = browser.find_element(By.XPATH,xpath_main+f'/div[{x}]/div/div[2]')

# tab_cont[0].get_attribute('class')
# tab_cont[1].get_attribute('class')el_ticker

# tab_cont[1].click()
