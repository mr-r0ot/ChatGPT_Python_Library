def ChatGPT(query,log=False):
    import os;libs=['selenium','requests']
    for l in libs:
        try:exec(f'import {l}')
        except:
            os.system(f'pip install {l}')
            try:exec(f'import {l}')
            except:print(f'Please Install {l}');sysexit()
    from selenium import webdriver;from selenium.webdriver.common.by import By;from time import sleep;from sys import exit as sysexit
    if log==True:print(' [ LOG + ]   Importing librarys')
    from selenium.webdriver.firefox.options import Options as firefox_option_driver;firefox_option = firefox_option_driver();firefox_option.add_argument("--headless");from selenium.webdriver.edge.options import Options as edge_option_driver;edge_option = edge_option_driver();edge_option.add_argument("--headless");from selenium.webdriver.ie.options import Options as ie_option_driver;ie_option = ie_option_driver();ie_option.add_argument("--headless");from selenium.webdriver.chrome.options import Options as chrome_option_driver;chrome_option = chrome_option_driver();chrome_option.add_argument("--headless")
    if log==True:print(' [ LOG + ]   Creatting Options')
    try:
        driver = webdriver.Firefox(firefox_option)
        if log==True:print(' [ LOG + ]   Running firefox driver')
    except:
        try:
            driver = webdriver.Edge(edge_option)
            if log==True:print(' [ LOG + ]   Running edge driver')
        except:
            try:
                driver = webdriver.Chrome(chrome_option)
                if log==True:print(' [ LOG + ]   Running chrome driver')
            except:
                try:
                    driver = webdriver.Safari()
                    if log==True:print(' [ LOG + ]   Running safari driver')
                except:
                    try:
                        driver = webdriver.Ie(ie_option)
                        if log==True:print(' [ LOG + ]   Running ie driver')
                    except:
                        if log==True:print(f"""
    [ - ] Error: Webdriver File Not Find!
    Please Download Chrome Or ... WebDriver File On Move To Path App""")
                        sysexit() 
    def wait_full_xpath(xp):
        while True:
            try:driver.find_element(By.XPATH,xp);break
            except:sleep(3)
    sleep(0.5)
    try:
        if log==True:print(' [ LOG + ]   connecting to server')
        driver.get("https://chatgpt4online.org/chatgpt-free-online/#chat")
    except:return 'NetWork Error!'
    if log==True:print(' [ LOG + ]   connected')
    if log==True:print(' [ LOG + ]   Sending data to server..')
    wait_full_xpath('/html/body/div[1]/div/div/div/main/div/article/div/div/div/div/div[6]/div/div[1]/div/div[1]/div/div/div/div/div[2]/div/textarea');driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/main/div/article/div/div/div/div/div[6]/div/div[1]/div/div[1]/div/div/div/div/div[2]/div/textarea').send_keys(query);sleep(1);driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/main/div/article/div/div/div/div/div[6]/div/div[1]/div/div[1]/div/div/div/div/div[2]/button').click();sleep(1)
    if log==True:print(' [ LOG + ]   Getting Output')
    wait_full_xpath('/html/body/div[1]/div/div/div/main/div/article/div/div/div/div/div[6]/div/div[1]/div/div[1]/div/div/div/div/div[1]/div[3]/span[2]/span/span');output=(driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/main/div/article/div/div/div/div/div[6]/div/div[1]/div/div[1]/div/div/div/div/div[1]/div[3]/span[2]/span/span').text);driver.quit()
    if log==True:print(' [ LOG + ]   Quittng from driver')
    return output
