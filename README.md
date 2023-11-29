# API Documentation

The Personal Music Recommendation API provides endpoints for retrieving music recommendations and searching for tracks. To access the API, you need a valid function key.

## Base URL

Base URL: https://pmrapim.azure-api.net/personal-music-recommendation

## Endpoints

### Get Music Recommendations

- **Endpoint**: `/recommendation`
- **Description**: Get music recommendations based on a given song name.
- **HTTP Method**: GET

#### Query Parameters:

- `song` (required if genre is not set) - The name of the song for which you want recommendations.
- `genre` (required if song is not set) - The genre of the song for which you want recommendations.
- `limit` (optional) - The maximum number of recommendation results (default: 5).
  

**Request Example:**

```http
GET https://pmrapim.azure-api.net/personal-music-recommendation/recommendation?song=hello
```
**Response Example:**

```json
[
  {
      "name": "Firework",
      "artists": ["Katy Perry"],
      "external_url": "https://open.spotify.com/track/4r6eNCsrZnQWJzzvFh4nlg",
      "images": [
          {
              "height": 640,
              "url": "https://i.scdn.co/image/ab67616d0000b273d20c38f295039520d688a888",
              "width": 640
          },
          // Additional image details...
      ]
  },
  // Additional recommended tracks...
]
```
### Search

- **Endpoint**: `/search`
- **Description**: Search for tracks based on a query.
- **HTTP Method**: GET

#### Query Parameters:

- `q` (required) - The search query.
- `limit` (optional) - The maximum number of search results (default: 5).

**Request Example:**

```http
GET https://pmrapim.azure-api.net/personal-music-recommendation/search?q=hello&type=track&limit=10
```
**Response Example:**

```json
[
  {
      "name": "Firework",
      "artists": ["Katy Perry"],
      "external_url": "https://open.spotify.com/track/4r6eNCsrZnQWJzzvFh4nlg",
      "id": "62PaSfnXSMyLshYJrlTuL3",
      "images": [
          {
              "height": 640,
              "url": "https://i.scdn.co/image/ab67616d0000b273d20c38f295039520d688a888",
              "width": 640
          },
          // Additional image details...
      ]
  },
  // Additional recommended tracks...
]
```
### Available Genre
- **Endpoint**: `/genre`
- **Description**: `Retrieve a list of available genres seed parameter values for recommendations.`
- **HTTP Method**: GET


**Request Example**

```http
GET https://pmrapim.azure-api.net/personal-music-recommendation/genre
```

**RESPONSE SAMPLE**

```json
  ["acoustic", "afrobeat", "alt-rock", "alternative", "ambient", "anime", "black-metal", "bluegrass", "blues", "bossanova", "brazil", "breakbeat", "british", "cantopop", "chicago-house", "children", "chill", "classical", "club", "comedy", "country", "dance", "dancehall", "death-metal", "deep-house", "detroit-techno", "disco", "disney", "drum-and-bass", "dub", "dubstep", "edm", "electro", "electronic", "emo", "folk", "forro", "french", "funk", "garage", "german", "gospel", "goth", "grindcore", "groove", "grunge", "guitar", "happy", "hard-rock", "hardcore", "hardstyle", "heavy-metal", "hip-hop", "holidays", "honky-tonk", "house", "idm", "indian", "indie", "indie-pop", "industrial", "iranian", "j-dance", "j-idol", "j-pop", "j-rock", "jazz", "k-pop", "kids", "latin", "latino", "malay", "mandopop", "metal", "metal-misc", "metalcore", "minimal-techno", "movies", "mpb", "new-age", "new-release", "opera", "pagode", "party", "philippines-opm", "piano", "pop", "pop-film", "post-dubstep", "power-pop", "progressive-house", "psych-rock", "punk", "punk-rock", "r-n-b", "rainy-day", "reggae", "reggaeton", "road-trip", "rock", "rock-n-roll", "rockabilly", "romance", "sad", "salsa", "samba", "sertanejo", "show-tunes", "singer-songwriter", "ska", "sleep", "songwriter", "soul", "soundtracks", "spanish", "study", "summer", "swedish", "synth-pop", "tango", "techno", "trance", "trip-hop", "turkish", "work-out", "world-music"]
```
