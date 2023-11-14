import requests
from bs4 import BeautifulSoup
from .data import Data


def parse_text(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    table = soup.find('div', 'm_l fl')
    headers = []
    for i in table.find_all('ul'):
        headers.append(i.text)
    return headers


def get_data(headers, platform):
    data = Data()
    data.platform = platform
    data.get_column_name_list(headers[1])
    for i in range(2, len(headers)):
        data.get_table_row_list((i - 1), headers[i])
    return data
