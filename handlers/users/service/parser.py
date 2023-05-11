import requests
from bs4 import BeautifulSoup


def get_soup_data_by_link(link):
    html = requests.get(link).content

    return BeautifulSoup(html, "html5lib")


def get_main_up_links_data(link):
    soup_data = get_soup_data_by_link(link)
    links_data = soup_data.select('.article_header > a')

    return links_data


def get_links_data(link):
    soup_data = get_soup_data_by_link(link)
    links_data = soup_data.select('.article__title > a')

    return links_data


def get_four_headers_and_links(link):
    links_data = get_links_data(link)

    links = []
    headers = []
    for i in links_data[:4]:
        domain = link[:-6]
        full_link = convert_link_to_absolute(i.get('href'), domain)
        links.append(full_link)
        headers.append(i.text)

    return headers, links


def get_all_links_from_page(link):
    links_data = get_main_up_links_data(link)

    links = []
    for i in links_data:
        domain = link[:-6]
        full_link = convert_link_to_absolute(i.get('href'), domain)
        links.append(full_link)

    return links


def convert_link_to_absolute(link, domain):
    if link[:5] != 'https':
        link = f'{domain}{link}'
    return link


def convert_article_to_single_string(soup_data):
    post_text = soup_data.select('.post__text > p, .article > p, .post_text > p')
    article_body = []
    for article in post_text:
        article_body.append(article.text + '\n')
    article_text = ''.join(article_body)
    return article_text


def get_article_by_its_link(link):
    article = requests.get(link).content
    soup_data = BeautifulSoup(article, "html5lib")

    return convert_article_to_single_string(soup_data)

