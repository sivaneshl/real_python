import argparse
import requests
from bs4 import BeautifulSoup


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-location', type=str)
    parser.add_argument('-keyword', type=str)
    args = parser.parse_args()

    location, keyword = args.location, args.keyword
    location_string = "All Locations" if location is None else location
    keyword_string = "" if keyword is None else "with keyword={}".format(keyword)
    print('Searching for Software Developer jobs in {} {}'.format(location_string, keyword_string))

    if location:
        url = f"https://www.monster.com/jobs/search/?q=Software-Developer&where={location}"
    else:
        url = f"https://www.monster.com/jobs/search/?q=Software-Developer"

    page = requests.get(url)
    # print(page.content)

    soup = BeautifulSoup(page.content, 'html.parser')

    # the element you’re looking for is a <div> with an id attribute that has the value "ResultsContainer"
    results = soup.find(id='ResultsContainer')
    # print(results.prettify())

    # every job posting is wrapped in a <section> element with the class card-content
    job_elements = results.find_all('section', class_='card-content')
    # .find_all() returns an iterable containing all the HTML for all the job listings displayed on that page
    for job_element in job_elements:
        # print(job_element,  end='\n'*2)
        # Each job_element is a new BeautifulSoup object.

        # Filter by keyword
        # if job_element.find('h2') is not None and job_element.find('h2', string=lambda text: keyword in text.lower()):

        if keyword:
            title_element = job_element.find('h2', string=lambda text: keyword in text.lower(), class_='title')
        else:
            title_element = job_element.find('h2', class_='title')
        company_element = job_element.find('div', class_='company')
        location_element = job_element.find('div', class_='location')
        a_tag = job_element.find('a')
        if a_tag is not None:
            link = job_element.find('a')['href']
        # skip nulls
        if None in (title_element, company_element, location_element):
            continue
        print(title_element.text.strip())
        print(company_element.text.strip())
        print(location_element.text.strip())
        print(f"Apply here: {link}")
        print()


# Usage = py scape_monster_site.py -location=india -keyword=python
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Aborted')