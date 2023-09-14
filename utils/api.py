import requests


def get_data_from_url(url, headers={}, params={}) -> tuple:
    response = requests.get(url, headers=headers, params=params)
    if (status := response.status_code) == 200:
        data = response.json()
    else:
        data = "Failed"
    return status, data