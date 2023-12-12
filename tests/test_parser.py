import pytest
import requests
from app.Parser import parser


@pytest.mark.parametrize('url', [('https://www.antutu.com/en/ranking/rank1.htm'),
                                 ('https://www.antutu.com/en/ranking/ios1.htm'),
                                 ('https://www.antutu.com/en/ranking/ai1.htm')])
def test_access_url(url):
    page = requests.get(url)
    assert page.status_code == 200


@pytest.mark.parametrize('url', [('https://www.antutu.com/en/ranking/rank1.htm'),
                                 ('https://www.antutu.com/en/ranking/ios1.htm'),
                                 ('https://www.antutu.com/en/ranking/ai1.htm')])
def test_parse_text_data(url):
    headers = parser.parse_text(url)
    assert type(headers) == list
    assert len(headers) != 0


@pytest.mark.parametrize('url', [('https://www.antutu.com/en/ranking/rank1.htm'),
                                 ('https://www.antutu.com/en/ranking/ios1.htm'),
                                 ('https://www.antutu.com/en/ranking/ai1.htm')])
def test_get_column_name_list(url):
    headers = parser.parse_text(url)
    col_name_list = parser.get_column_name_list(headers[1])
    assert col_name_list[0] == '№'


@pytest.mark.parametrize('url, platform', [('https://www.antutu.com/en/ranking/rank1.htm', 'Android'),
                                 ('https://www.antutu.com/en/ranking/ios1.htm', 'IOS'),
                                 ('https://www.antutu.com/en/ranking/ai1.htm', 'AI')])
def test_get_data(url, platform):
    headers = parser.parse_text(url)
    data = parser.get_data(headers, platform)
    assert len(data) != 0
