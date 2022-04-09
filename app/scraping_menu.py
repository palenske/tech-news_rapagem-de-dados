import sys
from scripts.analyzer.scraper import get_tech_news
from scripts.analyzer.search_engine import SearchEngine
from scripts.analyzer.ratings import top_5_news, top_5_categories

SE = SearchEngine()


def save_news_in_db():
    amount = int(input("Digite quantas notícias serão buscadas: "))
    get_tech_news(amount)
    return "Dados salvos no banco!"


def news_by_title():
    title = input("Digite o título: ")
    result = SE.search_by_title(title)
    for title, link in result:
        print(f"Título: {title}\n Link: {link}\n")


def news_by_data():
    date = input("Digite a data no formato aaaa-mm-dd: ")
    result = SE.search_by_date(date)
    for title, link in result:
        print(f"Título: {title}\n Link: {link}\n")


def news_by_source():
    source = input("Digite a fonte: ")
    result = SE.search_by_source(source)
    for title, link in result:
        print(f"Título: {title}\n Link: {link}\n")


def news_by_category():
    category = input("Digite a categoria: ")
    result = SE.search_by_category(category)
    for title, link in result:
        print(f"Título: {title}\n Link: {link}\n")


def top_news():
    result = top_5_news()
    for title, link in result:
        print(f"Título: {title}\n Link: {link}\n")


def top_category():
    result = top_5_categories()
    for category in result:
        print(category)


def exit_program():
    print("Encerrando script")
    return SystemExit()


def analyzer_menu():
    call_func = {
        0: save_news_in_db,
        1: news_by_title,
        2: news_by_data,
        3: news_by_source,
        4: news_by_category,
        5: top_news,
        6: top_category,
        7: exit_program,
    }

    select = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por fonte;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair.\n: "
    )

    if not select.isdigit() or 7 < int(select) > 0:
        sys.stderr.write("Opção inválida\n")
    else:
        return call_func[int(select)]()
