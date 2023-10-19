import requests


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


# TODO optional recommendation by multiple songs/genre
# TODO add limit parameter
def get_recommendation(token, song=None, genre=None):
    params = {"limit": 5}

    if song is not None:
        # Handle the case where song is provided
        search_result_list = search(token, song)
        track_id = search_result_list[0]["id"]
        params["seed_tracks"] = track_id

    if genre is not None:
        # Handle the case where genre is provided
        params["seed_genres"] = genre

    if not params:
        # Handle the case where neither song nor genre is provided
        return []

    # Rest of the code for making the recommendation request

    url = "https://api.spotify.com/v1/recommendations"
    headers = {
        "Authorization": token,
    }

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
    return search_results


def genre(token):
    url = "https://api.spotify.com/v1/recommendations/available-genre-seeds"

    headers = {
        "Authorization": token,
    }
    available_genre_list = []

    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        available_genre_list = data.get("genres", [])
    return available_genre_list
