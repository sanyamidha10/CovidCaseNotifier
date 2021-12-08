# import modules
from bs4 import BeautifulSoup
import requests
from plyer import notification

# website
url = "https://www.worldometers.info/coronavirus/country/india/"

# parsing
req = requests.get(url)
htmlcontent = (req.content)
soup = BeautifulSoup(htmlcontent, 'html.parser')


# data collection

new_cases = soup.find('div', class_="maincounter-number").span.get_text()
print(new_cases)

for recovered_cases in soup.find_all('div', class_="maincounter-number"):
    output = recovered_cases.get_text()
print(output)


for death_cases in soup.find_all('span', class_="number-table"):
    deaths = death_cases.get_text()
print(deaths)



# notifier
title = "Covid Update"
message = "corona cases-" + str(new_cases) +  "\ndeaths-" + str(deaths) + "Recovered cases-" + str(output)

notification.notify(title = title, message = message, timeout = 10, app_icon = r"C:\Users\DELL\Downloads\covid.ico",)
