from bs4 import BeautifulSoup
from beasts import get_pages_count


def test_get_count_from_page():
    soup = BeautifulSoup("""
                        <div id="mw-pages">
                            <p>
                                Показано 200 страниц из 45&nbsp;351, находящейся в данной категории. <a href="/wiki/blahblah" title="Википедия:Категоризация/FAQ">Список ниже может не отражать последних изменений.</a>
                            </p>
                        </div>
                        """, 'html.parser')

    animals = get_pages_count(soup)
    assert animals == 227


def test_get_count_from_page_without_div():
    soup = BeautifulSoup("<div><p>Lion</p></div>", 'html.parser')

    animals = get_pages_count(soup)
    assert animals is None


def test_get_count_from_page_without_p():
    soup = BeautifulSoup('<div id="mw-pages"><h1>Lion</h1></div>', 'html.parser')

    animals = get_pages_count(soup)
    assert animals is None
