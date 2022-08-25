import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import random

url = requests.get('https://en.m.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')
soup = BeautifulSoup(url.text, 'html.parser')

table_name = 'wikitable sortable plainrowheaders' 
soup_table = soup.find('table', {'class':table_name})
df = pd.read_html(str(soup_table))

pd.set_option("display.max_columns",1000)
pd.set_option("display.max_rows",1000)
pd.set_option("display.min_rows",1000)
pd.set_option("display.width",1000)
pd.set_option("expand_frame_repr",True)
print(df)

print("-" * 1000)

url_crop = requests.get('https://en.m.wikipedia.org/wiki/List_of_most_valuable_crops_and_livestock_products')
soup_crop = BeautifulSoup(url_crop.text, 'html.parser')

table_name_crop = 'wikitable sortable' 
soup_table_crop = soup_crop.find('table', {'class':table_name_crop})
df_crop = pd.read_html(str(soup_table_crop))

pd.set_option("display.max_columns",500)
pd.set_option("display.max_rows",500)
pd.set_option("display.min_rows",500)
pd.set_option("display.width",500)
pd.set_option("expand_frame_repr",True)
print(df_crop)


print("-" * 1000)

url_sunshine = requests.get("https://en.wikipedia.org/wiki/List_of_cities_by_sunshine_duration")
contentt = BeautifulSoup(url_sunshine.content, 'html.parser')


li = []
tables = contentt.find_all('table')
for table in tables:
    if len(table) > 1:
        rows = table.find_all('tr')
        for row in rows[1:]:
            cells = row.find_all('td')
            state = cells[1].text.strip()
            li.append(state)
        print(li)

li_1 = []
tables = contentt.find_all('table')
for table in tables:
    if len(table) > 1:
        rows = table.find_all('tr')
        for row in rows[1:]:
            cells = row.find_all('td')
            sun = cells[7].text.strip()
            li_1.append((int(float(sun))))
        print(li_1)



#Since lists were generated for each table on the Wikipedia page, which corresponded to different countries and therefore
#different sunshine durations, I manually copied and pasted the outputs into different lists to generate graphs using matplotlib

li_africa_sunshine = [118, 145, 128, 221, 221, 141, 193, 252, 146, 219, 150, 212, 146, 224, 165, 107, 112, 130, 156, 114, 177, 201, 261, 282, 309, 300, 271, 264, 272, 267, 258, 300, 270, 259, 276, 218, 261, 237, 266, 234, 233, 318, 306, 309, 321, 288, 315, 335, 357, 363, 366, 348, 390, 312, 327, 207, 159, 255, 297, 223, 225, 237, 231, 220, 303, 294, 230, 156, 153, 132, 136, 120, 295, 303, 284, 271, 175, 266, 249, 270, 224, 300, 260, 306, 276, 270, 288, 264, 267, 264, 237, 219, 165, 162, 206, 256, 282, 277, 240, 180, 216, 189, 186, 255, 153, 216, 210, 147, 69, 287, 309]
li_africa_cities = ['Gagnoa', 'Bouaké', 'Abidjan', 'Odienné', 'Ferké', 'Cotonou', 'Parakou', 'Kandi', 'Lomé', 'Mango', 'Accra', 'Tamale', 'Kumasi', 'Garoua', "N'Gaoundéré", 'Douala', 'Yaoundé', 'Libreville', 'Port-Gentil', 'Lagos', 'Makurdi', 'Jos', 'Kano', 'Sokoto', 'Port Sudan', 'Khartoum', 'Asmara', 'Ouagadougou', 'Ouahigouya', 'Niamey', "N'Djamena", 'Abéché', 'Banjul', 'Dakar', 'Thiès', 'Mogadishu', 'Buloburde', 'Djibouti City', 'Ségou', 'Timbuktu', 'Bamako', 'Algiers', 'Tamanrasset', 'Tunis', 'Gabes', 'Rabat', 'Marrakech', 'Ouarzazate', 'Alexandria', 'Cairo', 'Dakhla Oasis', 'Hurghada', 'Marsa Alam', 'Tripoli', 'Benghazi', 'Mombasa', 'Nairobi', 'Garissa', 'Lodwar', 'Luanda', 'Juba', 'Wau', 'Dar-es-Salaam', 'Zanzibar', 'Tabora', 'Dodoma', 'Mekelle', 'Addis Abeba', 'Brazaville', 'Pointe-Noire', 'Dolisie', 'Kinshasa', 'Lubumbashi', 'Nouadhibou', 'Nouakchott', 'Pretoria', 'Cape Town', 'Johannesburg', 'Bloemfontein', 'Upington', 'Durban', 'Maun', 'Gaborone', 'Ghanzi', 'Ndola', 'Lusaka', 'Livingstone', 'Harare', 'Bulawayo', 'Karonga', 'Blantyre', 'Mzuzu', 'Fianarantsoa', 'Toamasina', 'Antananarivo', 'Antsiranana', 'Mahajanga', 'Toliara', 'Maputo', 'Bangui', 'Birao', 'Kampala', 'Entebbe', 'Bujumbura', 'Conakry', 'Kankan', 'Bissau', 'Bata', 'Malabo', 'Keetmanshoop', 'Windhoek']
plt.rc('font', size=8) 
plt.bar(li_africa_cities, li_africa_sunshine)
plt.ylabel("Sunshine Duration Of Africa In June"), plt.xlabel("African Cities")
plt.title("Sunshine Duration Of African Cities In June")
plt.show()

li_asia_cities = ['Kabul', 'Baku', 'Dhaka', 'Beijing', 'Chongqing', 'Fuzhou', 'Guangzhou', 'Hong Kong', 'Lhasa', 'Macau', 'Nanjing', 'Ningbo', 'Qingdao', 'Shanghai', 'Tianjin', 'Ürümqi', 'Wuhan', 'Xiamen', 'Delhi', 'Kolkata', 'Mumbai', 'Bangalore', 'Chennai', 'Denpasar', 'Jakarta', 'Makassar', 'Medan', 'Bandar Abbas', 'Isfahan', 'Mashhad', 'Tabriz', 'Tehran', 'Baghdad', 'Tel Aviv', 'Sapporo', 'Sendai', 'Tokyo', 'Kanazawa', 'Nagoya', 'Almaty', 'Astana', 'Ulaanbaatar', 'Pyongyang', 'Muscat', 'Karachi', 'Lahore', 'Quetta', 'Manila', 'Dikson', 'Irkutsk', 'Omsk', 'Petropavlovsk-Kamchatsky', 'Vladivostok', 'Yakutsk', 'Abha', 'Riyadh', 'Singapore', 'Busan', 'Seoul', 'Kaohsiung', 'Taichung', 'Taipei', 'Bangkok', 'Chiang Mai', 'Hat Yai', 'Nakhon Ratchasima', 'Ankara', 'Dubai', 'Tashkent', 'Da Lat', 'Da Nang', 'Hanoi', 'Ho Chi Minh City']
li_asia_sunshine = [353, 294, 90, 261, 128, 141, 140, 146, 257, 155, 162, 147, 219, 130, 226, 282, 170, 163, 196, 123, 148, 137, 234, 228, 255, 241, 157, 302, 345, 343, 334, 328, 348, 357, 187, 133, 125, 152, 149, 280, 336, 269, 229, 325, 231, 269, 327, 162, 141, 264, 319, 192, 130, 333, 276, 328, 177, 179, 182, 199, 160, 121, 178, 156, 111, 114, 306, 342, 363, 147, 239, 172, 171]
plt.rc('font', size=8) 
plt.bar(li_asia_cities, li_asia_sunshine)
plt.ylabel("Sunshine Duration Of Asian Cities In June"), plt.xlabel("Asian Cities")
plt.title("Sunshine Duration Of Asian Cities In June")
plt.show()

li_europe_cities = ['Tirana', 'Yerevan', 'Vienna', 'Minsk', 'Brussels', 'Sarajevo', 'Sofia', 'Zagreb', 'Split', 'Prague', 'Nicosia', 'Aarhus', 'Copenhagen', 'Rønne', 'Tallinn', 'Vilsandi', 'Tórshavn', 'Helsinki', 'Lyon', 'Marseille', 'Paris', 'Tbilisi', 'Berlin', 'Frankfurt', 'Athens', 'Budapest', 'Reykjavik', 'Dublin', 'Cagliari', 'Milan', 'Naples', 'Rome', 'Riga', 'Vilnius', 'Luxembourg City', 'Valletta', 'Chișinău', 'Monaco', 'Podgorica', 'Amsterdam', 'Skopje', 'Bergen', 'Oslo', 'Tromsø', 'Warsaw', 'Faro', 'Lisbon', 'Porto', 'Bucharest', 'Moscow', 'Sochi', 'Belgrade', 'Niš', 'Bratislava', 'Ljubljana', 'Barcelona', 'Cádiz', 'Madrid', 'Seville', 'Valencia', 'Gothenburg', 'Stockholm', 'Zurich', 'Istanbul', 'Kyiv', 'Edinburgh', 'London']
li_europe_sunshine = [298, 297, 228, 267, 188, 207, 258, 244, 306, 218, 369, 251, 260, 315, 294, 314, 125, 297, 254, 326, 202, 249, 222, 219, 336, 250, 174, 179, 311, 243, 279, 285, 288, 246, 210, 337, 283, 281, 276, 206, 276, 189, 250, 221, 237, 332, 303, 274, 267, 299, 258, 261, 251, 270, 246, 287, 331, 310, 317, 276, 256, 292, 204, 300, 270, 166, 204]
plt.rc('font', size=8) 
plt.bar(li_europe_cities, li_europe_sunshine)
plt.ylabel("Sunshine Duration Of European Countries In June"), plt.xlabel("European Countries")
plt.title("Sunshine Duration Of European Cities In June")
plt.show()

li_america_cities = ['Calgary', 'Churchill', 'Edmonton', 'Iqaluit', 'Montreal', 'Toronto', 'Vancouver', 'Whitehorse', 'Winnipeg', 'La Ceiba', 'La Paz', 'Mexico City', 'Monterrey', 'Villahermosa', 'Managua', 'Panama City', 'San Juan', 'San Salvador', 'Saint-Pierre', 'Albuquerque', 'Anchorage', 'Atlanta', 'Austin', 'Baltimore', 'Boise', 'Boston', 'Charlotte', 'Chicago', 'Cleveland', 'Columbus', 'Dallas', 'Denver', 'Detroit', 'El Paso', 'Fresno', 'Honolulu', 'Houston', 'Indianapolis', 'Jacksonville', 'Kansas City', 'Las Vegas', 'Los Angeles', 'Louisville', 'Memphis', 'Miami', 'Milwaukee', 'Minneapolis', 'Nashville', 'New Orleans', 'New York City', 'Nome', 'OklahomaCity', 'Omaha', 'Philadelphia', 'Phoenix', 'Pittsburgh', 'Portland (OR)', 'Raleigh', 'Richmond (VA)', 'Sacramento', 'Salt Lake City', 'San Antonio', 'San Diego', 'San Francisco', 'Seattle', 'St. Louis', 'Tampa', 'Tucson', 'Tulsa', 'Virginia Beach', 'Washington,D.C.', 'Wichita', 'Yuma']
li_america_sunshine = [269, 243, 285, 200, 240, 259, 226, 266, 276, 192, 322, 183, 206, 217, 186, 116, 259, 174, 172, 359, 274, 284, 285, 277, 351, 286, 289, 311, 294, 258, 297, 315, 301, 384, 412, 286, 281, 287, 283, 305, 401, 275, 288, 320, 288, 304, 321, 277, 274, 257, 275, 326, 314, 271, 407, 242, 290, 267, 306, 419, 360, 275, 242, 311, 268, 291, 277, 396, 294, 280, 283, 305, 415]
plt.rc('font', size=8) 
plt.bar(li_america_cities, li_america_sunshine)
plt.ylabel("Sunshine Duration Of American Cities In June"), plt.xlabel("American Cities")
plt.title("Sunshine Duration Of American Cities In June")
plt.show()
        
li_south_am = ['Buenos Aires', 'Córdoba', 'La Plata', 'Mendoza', 'Salta', 'Ushuaia', 'La Paz', 'Belém', 'Belo Horizonte', 'Brasília', 'Curitiba', 'Fortaleza', 'Manaus', 'Porto Alegre', 'Rio de Janeiro', 'Recife', 'Salvador', 'São Paulo', 'Antofagasta', 'Calama', 'Concepción', 'Santiago', 'Valdivia', 'Barranquilla', 'Bogotá', 'Cali', 'Medellín', 'Guayaquil', 'Quito', 'Stanley', 'Cayenne', 'Georgetown', 'Asunción', 'Arequipa', 'Lima', 'Montevideo', 'Caracas', 'Maracaibo', 'Ciudad Bolivar']
li_south_am_sun = [132, 150, 120, 168, 120, 50, 240, 228, 229, 254, 141, 215, 186, 115, 202, 161, 147, 160, 207, 297, 114, 120, 45, 194, 94, 153, 173, 123, 189, 57, 148, 156, 165, 291, 50, 129, 183, 253, 201]
plt.rc('font', size=8) 
plt.bar(li_south_am, li_south_am_sun)
plt.ylabel("Sunshine Duration Of South American Cities In June"), plt.xlabel("South American Cities")
plt.title("Sunshine Duration Of South American Cities In June")
plt.show()
        
li_oceania = ['Adelaide', 'Alice Springs', 'Brisbane', 'Canberra', 'Darwin', 'Hobart', 'Melbourne', 'Perth', 'Sydney', 'Suva', 'Auckland', 'Christchurch', 'Wellington', 'Dunedin', 'Port Moresby', 'Honiara']
li_oceania_sun =[138, 252, 198, 156, 297, 117, 120, 180, 177, 141, 110, 117, 102, 95, 200, 198]
plt.rc('font', size=8) 
plt.bar(li_oceania, li_oceania_sun)
plt.ylabel("Sunshine Duration Of Oceania Cities In June"), plt.xlabel("Oceania Cities")
plt.title("Sunshine Duration Of Oceania Cities In June")
plt.show()


def make_table(a, b):
    z = 0
    s = '''<table>
            <thead>
                <tr>
                    <th>city</th>
                    <th>sunshine</th>
                </tr>
            </thead>
            <tbody>\n'''
    while z < len(a):
        for x in a:
            for y in b:
                s+= '<tr>\n'
                s+= '<td>' + str(x) + '</td>\n'
                s+= '<td>' + str(y) + '</td>\n'
                s+= '</tr>\n'
                z += 1 
        s+= '</tbody></table>'
    return s

print(make_table(li_oceania, li_oceania_sun))

def scrape_rand_wiki(url):
    li = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find(id="firstHeading")
    print(title.text)
    links = soup.find(id="bodyContent").find_all("a")
    random.shuffle(links)
    linkTo = 0
    for link in links:

        if link['href'].find("/wiki/") == -1:
            continue

        linkTo = link
        break

    scrape_rand_wiki("https://en.wikipedia.org" + linkTo['href'])

scrape_rand_wiki("https://en.wikipedia.org/wiki/List_of_cities_by_sunshine_duration")

