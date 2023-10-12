import requests

# TODO write proper comments
def get_token(client_id, client_secret):
    token_url = "https://accounts.spotify.com/api/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }

    response = requests.post(url=token_url, headers=headers, data=data)
    token = response.json().get("access_token", None)
    return f"Bearer {token}"


# TODO add recommendation by genres
# TODO optional: input songs are not limited to 5, send separate requests and merge them
def get_recommendation(token, song):
    search_result_list = search(token, song)
    track_id = search_result_list[0]["id"]
    url = "https://api.spotify.com/v1/recommendations"

    headers = {
        "Authorization": token,
    }

    params = {"limit": 5, "seed_tracks": track_id}

    response = requests.get(url=url, params=params, headers=headers)

    recommendation_list = []

    if response.status_code == 200:
        data = response.json()
        for track in data["tracks"]:
            track_name = track["name"]
            artists = [artist["name"] for artist in track["artists"]]
            external_url = track["external_urls"]["spotify"]
            images = track["album"]["images"]
            recommendation_list.append(
                {
                    "name": track_name,
                    "artists": artists,
                    "external_url": external_url,
                    "images": images,
                }
            )
        # FIXME handle other status code errors
    return recommendation_list


def search(token, query, search_type="track", limit=5):
    url = "https://api.spotify.com/v1/search"
    headers = {
        "Authorization": token,
    }

    params = {"q": query, "type": search_type, "limit": limit}

    response = requests.get(url=url, params=params, headers=headers)

    search_results = []

    if response.status_code == 200:
        data = response.json()
        # TODO extract this as a method to be reusable
        for track in data["tracks"]["items"]:
            track_name = track["name"]
            artists = [artist["name"] for artist in track["artists"]]
            external_url = track["external_urls"]["spotify"]
            images = track["album"]["images"]
            id = track["id"]
            search_results.append(
                {
                    "name": track_name,
                    "artists": artists,
                    "external_url": external_url,
                    "id": id,
                    "images": images,
                }
            )
        # FIXME handle other status code errors
    return search_results

# TODO implement the method to get all the available genres