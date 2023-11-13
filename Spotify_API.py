import requests


class Spotify:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = self.__get_token(client_id, client_secret)

    def is_token_valid(self):
        url = "https://api.spotify.com/v1/me"
        headers = {
            "Authorization": self.token,
        }
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            return True
        else:
            return False

    def __get_token(self, client_id, client_secret):
        token_url = "https://accounts.spotify.com/api/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
        }

        response = requests.post(url=token_url, headers=headers, data=data)
        if response.status_code != 200:
            raise Exception("Unable to get token")

        token = response.json().get("access_token", None)
        return f"Bearer {token}"

    def __make_request(self, url, params=None):
        if not self.is_token_valid():
            self.token = self.__get_token(self.client_id, self.client_secret)

        headers = {
            "Authorization": self.token,
        }

        response = requests.get(url=url, params=params, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None

    # TODO optional recommendation by multiple songs/genre
    def get_recommendation(self, limit: int, song=None, genre=None):
        params = {"limit": limit}

        if song is not None:
            # Handle the case where song is provided
            search_result_list = self.search(query=song, limit=5)
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

        data = self.__make_request(url, params)

        if not data:
            return []

        recommendations = [self.__extract_track_info(track) for track in data["tracks"]]
        return recommendations

    def search(self, query, limit: int):
        url = "https://api.spotify.com/v1/search"

        params = {"q": query, "type": "track", "limit": limit}

        data = self.__make_request(url, params)

        if not data:
            return []

        search_results = [self.__extract_track_info(track) for track in data["tracks"]["items"]]
        return search_results

    def genres(self):
        url = "https://api.spotify.com/v1/recommendations/available-genre-seeds"

        data = self.__make_request(url)

        if not data:
            return []

        available_genre_list = []

        available_genre_list = data.get("genres", [])
        return available_genre_list

    def __extract_track_info(self, track):
        track_name = track["name"]
        artists = [artist["name"] for artist in track["artists"]]
        external_url = track["external_urls"]["spotify"]
        images = track["album"]["images"]
        id = track["id"]

        return {
            "name": track_name,
            "artists": artists,
            "external_url": external_url,
            "id": id,
            "images": images,
        }