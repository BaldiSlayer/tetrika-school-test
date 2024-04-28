from bs4 import BeautifulSoup
from solution import get_pages_count


def test_get_count_from_page():
    soup = BeautifulSoup("""
                        <div id="mw-pages">
                            <p>
                                Показано 200 страниц из 45&nbsp;351, находящейся в данной категории. <a href="/wiki/%D0%92%D0%B8%D0%BA%D0%B8%D0%BF%D0%B5%D0%B4%D0%B8%D1%8F:%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F/FAQ#Страница_категории_не_обновляется" title="Википедия:Категоризация/FAQ">Список ниже может не отражать последних изменений.</a>
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
