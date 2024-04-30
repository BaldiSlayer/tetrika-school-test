import csv
import math
from typing import Optional
import requests
from bs4 import BeautifulSoup


BASE_URL = "https://ru.wikipedia.org"
FIRST_URL = "/wiki/Категория:Животные_по_алфавиту"
NEXT_PAGE_SIGN = "Следующая страница"
NON_BREAKING_SPACE = '\u00A0'
BEASTS_ON_PAGE = 200


def save_result_to_csv(data: dict[str, int], filename: str = "beasts.csv") -> None:
    with open(filename, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        for item in data.items():
            writer.writerow(item)


def page_to_bs_object(url: str) -> Optional[BeautifulSoup]:
    response = requests.get(url)

    if response.status_code != 200:
        return None

    page_content = response.text
    return BeautifulSoup(page_content, "html.parser")


def get_animals_from_page(soup: BeautifulSoup) -> list[str]:
    columns = soup.find_all("div", {"class": "mw-category mw-category-columns"})
    links = []
    for column in columns:
        links += column.findAll("a")
    return [animal.get_text() for animal in links]


def get_next_page_url(soup: BeautifulSoup) -> Optional[str]:
    link = soup.find("a", string=NEXT_PAGE_SIGN)

    if not link:
        return None

    return link.get("href")


def get_pages_count(soup: BeautifulSoup) -> Optional[int]:
    """
    Gets the total number of animal records from the page and calculates the total number of animal pages based on them.
    Needed for logs
    """
    mw_pages_div = soup.find('div', {'id': 'mw-pages'})

    if not mw_pages_div:
        return None

    paragraph = mw_pages_div.find("p")

    if not paragraph:
        return None

    paragraph_text = paragraph.text

    # taking out a number, it is located between the word "из " and the symbol ","
    count = int(paragraph_text[paragraph_text.find('из ') + 3:paragraph_text.find(',')].replace(NON_BREAKING_SPACE, ''))

    return math.ceil(count / BEASTS_ON_PAGE)


def beasts_parser(start_url: str, debug: bool = True) -> dict[str, int]:
    """
    Gets the number of animals for each of the letters of the alphabet

    Parameters:
    start_url (str): the link from which the parsing will begin
    debug (bool): enabling/disabling logs

    Return value:
    dict[str, int]: A dictionary of the number of animals for each letter of the alphabet
    """
    data = {}
    current_url = start_url
    page_number = 0

    while True:
        page = page_to_bs_object(BASE_URL + current_url)

        if not page:
            print(f'Error occurred while fetching page: {BASE_URL + current_url}')
            break

        animals = get_animals_from_page(page)

        for animal in animals:
            first_letter = animal[0].upper()
            data[first_letter] = data.get(first_letter, 0) + 1

        current_url = get_next_page_url(page)
        if not current_url:
            break

        if debug:
            pages_count = get_pages_count(page)

            if not pages_count:
                print(f'Error occurred while trying to get pages count')

            page_number += 1
            print(f'Parsed {page_number}/{pages_count} pages')

    if debug:
        print(f'Parsed {page_number+1}/{page_number+1} pages')
        print(data)

    return data


if __name__ == "__main__":
    save_result_to_csv(beasts_parser(FIRST_URL), "beasts.csv")
