import requests
from bs4 import BeautifulSoup

url = "http://pythonjobs.github.io/"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='container')
# print(results.prettify())

job_list = results.find('section', class_='job_list').find_all('div', class_='job')
for job in job_list:
    title_element = job.find('h1')
    props_element = job.find_all('span', class_='info')
    company_element, location_element, date_element = None, None, None
    for prop in props_element:
        if prop.find('i', class_='i-company'):
            company_element = prop
        elif prop.find('i', class_='i-globe'):
            location_element = prop
        elif prop.find('i', class_='i-calendar'):
            date_element = prop

    if None not in (title_element, location_element, company_element, date_element):
        print(title_element.text.strip())
        print(company_element.text.strip())
        print(location_element.text.strip())
        print(date_element.text.strip())
        print()
