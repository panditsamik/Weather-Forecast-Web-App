import requests

API_KEY = "0018f5edeaa6234dc5d79b09d4bfec38"


def get_data(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    return filtered_data


if __name__ == "__main__":
    print(get_data("Kolkata"))
