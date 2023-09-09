from http import HTTPStatus

import requests
from bs4 import BeautifulSoup


def request_get(url: str):
    response = requests.get(url=url)
    return response, response.status_code


def is_empty_quotes_page(soup: BeautifulSoup):
    not_found_text = "No quotes found"
    return not_found_text in soup.decode()


def main():
    current_page = 1
    parse_url = "http://quotes.toscrape.com"

    parsing_result_message = "Not running"
    while True:
        quotes_page_url = parse_url + f"/page/{current_page}/"
        response, code = request_get(url=quotes_page_url)

        if code != HTTPStatus.OK:
            parsing_result_message = f"Status code != 200. Status code: {code}"
            break

        soup = BeautifulSoup(response.content, "html.parser")
        if is_empty_quotes_page(soup=soup):
            parsing_result_message = "Not quotes on page. Parsing is finished!"
            break

        quotes = soup.select(".quote")

        for quote_block in quotes:
            quote_text_block = quote_block.select_one(".text")
            if quote_block:
                quote_text = quote_text_block.text
            else:
                quote_text = "-"

            author_block = quote_block.select_one(".author")
            if author_block:
                author = author_block.text
            else:
                author = "-"

            print(quote_text, author)

        break

    print(f"Parsing result: {parsing_result_message}")


if __name__ == "__main__":
    main()
