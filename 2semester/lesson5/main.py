import json

from bs4 import BeautifulSoup


def get_film_data(film_block_element):
    film_name_el = film_block_element.select_one(".film_name")
    film_name = ""
    if film_name_el is not None:
        film_name = film_name_el.text

    film_poster_el = film_block_element.select_one(".film_poster")
    film_poster_url = ""
    if film_poster_el is not None:
        film_poster_url = film_poster_el["src"]

    film_description_el = film_block_element.select_one(".film_description")
    film_description = ""
    if film_description_el is not None:
        film_description = film_description_el.text

    genre_block = film_block_element.select_one(".genre")
    genres = []
    if genre_block is not None:
        for genre in genre_block.find_all("li"):
            genres.append(genre.text)

    film_year_el = film_block_element.select_one(".film_year")
    film_year = ""
    if film_year_el is not None:
        film_year = int(film_year_el.text)

    film_view_link_el = film_block_element.select_one(".film_view_link")
    film_view_link = ""
    if film_view_link_el is not None:
        film_view_link = film_view_link_el["href"]

    return {
        "name": film_name,
        "poster": film_poster_url,
        "description": film_description,
        "genres": genres,
        "year": film_year,
        "view_link": film_view_link
    }


def main():
    with open("index.html", mode="r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    all_films = soup.select(".films > .film")

    films = []

    for film_block in all_films:
        films.append(get_film_data(film_block))

    data_to_json = {"films": films}

    with open("films.json", mode="w", encoding="utf-8") as file:
        json.dump(data_to_json, file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
