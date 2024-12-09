import requests


def get_weather(city: str, param: dict[str]) -> str:
    url_template = "https://wttr.in/{}"
    url = url_template.format(city)
    response = requests.get(url, params=param)
    response.raise_for_status()
    return response.text


def main() -> None:
    param = {
        "lang": "ru",
        "M": "",
        "n": "",
        "q": "",
        "T": "",
    }

    input_city = input("Введите город: ")
    citys = [input_city] if input_city else [
        "Череповец",
        "Аэропорт Шереметьево",
        "Лондон",
        ]

    for city in citys:
        print(get_weather(city, param))


if __name__ == "__main__":
    main()
