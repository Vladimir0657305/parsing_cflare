from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# import requests
# from bs4 import BeautifulSoup
import time

# cdc_adoQpoasnfa76pfcZLmcfl_Array
# cdc_adoQpoasnfa76pfcZLmcfl_Object
# cdc_adoQpoasnfa76pfcZLmcfl_Promise
# cdc_adoQpoasnfa76pfcZLmcfl_Proxy
# cdc_adoQpoasnfa76pfcZLmcfl_Symbol

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)

s = Service(executable_path='C:\\Program Files\\Pyton\\chromedriver')
driver = webdriver.Chrome(service=s)

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    'source': '''
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Object
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Proxy
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol
    '''
})

try:
    driver.maximize_window()
    driver.get('https://anycoindirect.eu')
    # driver.get('https://www.gmc-uk.org/doctors/4081362')
    time.sleep(15)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}
proxies = {
    'http': 'https://cors-anywhere.herokuapp.com/:443',
    'https': 'https://cors-anywhere.herokuapp.com/:443'
}

# def get_location(url):
#     response = requests.get(url=url, headers=headers)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     ip = soup.find('table', class_='ui celled striped table').find(
#         'thead').find('h2').text.strip()
#     location = soup.find('table', class_='ui celled striped table').find(
#         'tbody').find_all('tr')[2].find_all('td')[1].text.strip()

#     print(f'{ip}\nLocation: {location}')

# def main():
#     get_location(url='https://www.ukraine.com.ua/uk/info/tools/my-ip/')

# if __name__ =='__main__':
#     main()