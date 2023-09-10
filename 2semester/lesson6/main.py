import json
from http import HTTPStatus

import requests
from bs4 import BeautifulSoup

RESULT_JSON_PATH = "./quotes.json"


def request_get(url: str):
    response = requests.get(url=url)
    return response, response.status_code


def _is_empty_quotes_page(soup: BeautifulSoup):
    not_found_text = "No quotes found"
    return not_found_text in soup.decode()


def is_ok_response_status(r):
    if r.status_code != HTTPStatus.OK:
        return False, f"Status code != 200. Status code: {r.status_code}"
    return True, "Success response"


def is_empty_quotes_page(soup: BeautifulSoup):
    if _is_empty_quotes_page(soup=soup):
        return True, "Not quotes on page. Parsing is finished!"

    return False, "Quotes is not empty"


def get_element_text(element):
    if element:
        return element.text
    else:
        return "-"


def get_quote_data(quote_block):
    quote_text_block = quote_block.select_one(".text")
    quote_text = get_element_text(quote_text_block)

    author_block = quote_block.select_one(".author")
    author = get_element_text(author_block)

    return {
        "text": quote_text,
        "author": author
    }


def write_quotes_to_file(data: dict, filepath=RESULT_JSON_PATH):
    with open(filepath, mode="w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def parse_quotes(quotes_blocks):
    _parsed_quotes = []
    for quote_block in quotes_blocks:
        quote_data = get_quote_data(quote_block)
        _parsed_quotes.append(quote_data)
    return _parsed_quotes


def can_parse_quotes(_response):
    response_ok, parsing_result_message = is_ok_response_status(_response)
    if not response_ok:
        return response_ok, parsing_result_message

    soup = BeautifulSoup(_response.content, "html.parser")
    is_empty_page, parsing_result_message = is_empty_quotes_page(soup)
    if is_empty_page:
        return False, parsing_result_message

    quotes_blocks = soup.select(".quote")
    if len(quotes_blocks) == 0:
        parsing_result_message = "Not quotes on page. Parsing is finished!"
        return False, parsing_result_message

    return True, "We can start parsing"


def start_parsing_page(page):
    parse_url = "http://quotes.toscrape.com"

    quotes_page_url = parse_url + f"/page/{page}/"
    response, _ = request_get(url=quotes_page_url)

    can_start_parsing, parsing_result_message = can_parse_quotes(response)

    if not can_start_parsing:
        return False, parsing_result_message, []

    soup = BeautifulSoup(response.content, "html.parser")
    quotes_blocks = soup.select(".quote")
    parsed_quotes = parse_quotes(quotes_blocks)
    parsing_result_message = "Parsing finished successfully"

    return True, parsing_result_message, parsed_quotes


def main():
    current_page = 1
    all_parsed_quotes = {}
    print(f"Start parse page: {current_page}")

    parsing_result_success, parsing_result_message, page_parsed_quotes = start_parsing_page(current_page)

    if len(page_parsed_quotes) > 0:
        all_parsed_quotes[current_page] = page_parsed_quotes

    write_quotes_to_file(all_parsed_quotes)
    print(f"Parsing result: {parsing_result_message}")


if __name__ == "__main__":
    main()
