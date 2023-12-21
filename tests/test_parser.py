import pytest
import requests
from app.Parser import parser


url_list = [('https://www.antutu.com/en/ranking/rank1.htm'),
            ('https://www.antutu.com/en/ranking/ios1.htm'),
            ('https://www.antutu.com/en/ranking/ai1.htm')]


@pytest.mark.parametrize('url', url_list)
def test_access_url(url):
    page = requests.get(url)
    assert page.status_code == 200


@pytest.mark.parametrize('url', url_list)
def test_parse_text_data(url):
    headers = parser.parse_text(url)
    assert type(headers) == list
    assert len(headers) != 0


@pytest.mark.parametrize('url', url_list)
def test_get_column_name_list(url):
    column_name_list = parser.get_column_name_list(parser.parse_text(url)[1])
    assert type(column_name_list) == list
    assert len(column_name_list) != 0


@pytest.mark.parametrize('url', url_list)
def test_get_table_row_list(url):
    table_row_list = parser.get_table_row_list(1, parser.parse_text(url)[2])
    assert type(table_row_list) == list
    assert len(table_row_list) != 0


@pytest.mark.parametrize('url, platform', [('https://www.antutu.com/en/ranking/rank1.htm', 'Android'),
                                           ('https://www.antutu.com/en/ranking/ios1.htm', 'IOS'),
                                           ('https://www.antutu.com/en/ranking/ai1.htm', 'AI')])
def test_get_data(url, platform):
    table = parser.get_data(parser.parse_text(url), platform)
    assert type(table) == list
    assert len(table) != 0