import requests
from bs4 import BeautifulSoup

data = []


def get_data():
    """ Get data from github repo."""
    global data
    response = requests.get('https://github.com/vinta/awesome-python')
    soup = BeautifulSoup(response.text, 'html.parser')
    readme_div = soup.find('div', attrs={'id': 'readme'})
    links = readme_div.find_all('a', href=True)
    for link in links:
        data.append({'name': link.text, 'href': link['href']})
    return data


def search_repos():
    """ Searches requested query in data. """
    global data
    query = input('Query? ')
    for d in data:
        if query == d['name']:
            return f"Output : {d['href']}"
    else:
        return f'No exact match found for "{query}", Try with different query.'


if __name__ == '__main__':
    get_data()
    print(search_repos())
