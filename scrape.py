import re
from typing import Text
import requests
from bs4 import BeautifulSoup
import json

# req = requests.get(
#     'https://www.countries-ofthe-world.com/flags-of-africa.html')
# print(req.status_code)
# res = req.text
# soup = BeautifulSoup(res, 'html.parser')
# print(soup.prettify())


def getAfricanCountry():
    african = requests.get('http://listofafricancountries.com/')
    soup = BeautifulSoup(african.text, 'html.parser')
    names = soup.find_all('div', id='name')
    # print(names[0].text)
    # print(soup.title.text)
    allCountries = []
    for i in range(len(names)):
        allCountries.append(names[i].text.strip())


countries = '''Flag of Algeria	Algeria
Flag of Angola	Angola
Flag of Benin	Benin
Flag of Botswana	Botswana
Flag of Burkina Faso	Burkina Faso
Flag of Burundi	Burundi
Flag of Cabo Verde	Cabo Verde
Flag of Cameroon	Cameroon
Flag of Central African Republic	Central African Republic
Flag of Chad	Chad
Flag of Comoros	Comoros
Flag of the Democratic Republic of Congo	Congo, Democratic Republic of the
Flag of the Republic of Congo	Congo, Republic of the
Flag of Cote d'Ivoire	Cote d'Ivoire
Flag of Djibouti	Djibouti
Flag of Egypt	Egypt
Flag of Equatorial Guinea	Equatorial Guinea
Flag of Eritrea	Eritrea
Flag of Eswatini	Eswatini (formerly Swaziland)
Flag of Ethiopia	Ethiopia
Flag of Gabon	Gabon
Flag of Gambia	Gambia
Flag of Ghana	Ghana
Flag of Guinea	Guinea
Flag of Guinea-Bissau	Guinea-Bissau
Flag of Kenya	Kenya
Flag of Lesotho	Lesotho
Flag of Liberia	Liberia
Flag of Libya	Libya
Flag of Madagascar	Madagascar
Flag of Malawi	Malawi
Flag of Mali	Mali
Flag of Mauritania	Mauritania
Flag of Mauritius	Mauritius
Flag of Morocco	Morocco
Flag of Mozambique	Mozambique
Flag of Namibia	Namibia
Flag of Niger	Niger
Flag of Nigeria	Nigeria
Flag of Rwanda	Rwanda
Flag of Sao Tome and Principe	Sao Tome and Principe
Flag of Senegal	Senegal
Flag of Seychelles	Seychelles
Flag of Sierra Leone	Sierra Leone
Flag of Somalia	Somalia
Flag of South Africa	South Africa
Flag of South Sudan	South Sudan
Flag of Sudan	Sudan
Flag of Tanzania	Tanzania
Flag of Togo	Togo
Flag of Tunisia	Tunisia
Flag of Uganda	Uganda
Flag of Zambia	Zambia
Flag of Zimbabwe Zimbabwe'''

allCountries = []
for item in countries.split('\n'):
    allCountries.append(item.split('\t').pop())

print(allCountries)
