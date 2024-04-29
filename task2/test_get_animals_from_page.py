from bs4 import BeautifulSoup
from beasts import get_animals_from_page


def test_get_animals_from_page():
    soup = BeautifulSoup("""
                            <div class="mw-category mw-category-columns">
                                <ul>
                                    <li><a href="/wiki/Lion">Lion</a></li>
                                    <li><a href="/wiki/Elephant">Elephant</a></li>
                                    <li><a href="/wiki/Giraffe">Giraffe</a></li>
                                </ul>
                            </div>
                            """, 'html.parser')

    animals = get_animals_from_page(soup)
    assert animals == ['Lion', 'Elephant', 'Giraffe']


def test_get_animals_from_page_empty_list():
    soup = BeautifulSoup("", 'html.parser')

    animals = get_animals_from_page(soup)
    assert animals == []


def test_get_animals_from_page_no_class():
    soup = BeautifulSoup("<div><a href='/wiki/Lion'>Lion</a></div>", 'html.parser')

    animals = get_animals_from_page(soup)
    assert animals == []