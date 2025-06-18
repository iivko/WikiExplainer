import requests


def wiki_fetcher(topic: str):
    """This function sends request to MediaWiki API for page operations,
    in our case we extract the main data and image URL"""

    # Main API URL
    url_api = "https://en.wikipedia.org/w/api.php"

    # Params
    params = {
        "action": "query",
        "prop": "extracts|pageimages",
        "exintro": True,
        "explaintext": True,
        "piprop": "original",
        "titles": topic,
        "format": "json",
        "formatversion": 2
    }

    # Sending the request with the params
    response = requests.get(
        url_api,
        params=params,
        timeout=3
    )

    # Creating the response dict
    response_data = {
        "success": False,
        "topic": "",
        "text": "",
        "image_url": ""
    }

    # Checking if the request was successfull
    if response.status_code == 200:
        data = response.json()

        page = data.get("query", {}).get("pages", [{}])[0]

        response_data["success"] = True
        response_data["topic"] = page.get("title", "No title")
        response_data["text"] = page.get("extract", "No intro text found.")
        response_data["image_url"] = page.get("original", {}).get("source", None)

        return response_data

    else:
        return response_data


