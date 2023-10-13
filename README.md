# API Documentation

The Personal Music Recommendation API provides endpoints for retrieving music recommendations and searching for tracks. To access the API, you need a valid function key.

## Base URL

Base URL: [https://personal-music-recommendation.azurewebsites.net/api](https://personal-music-recommendation.azurewebsites.net/api)

## Authentication

All endpoints require authentication using a function key. The function key is included as a query parameter in the request URL.

### Search Function Key

- **Query Parameter**: `code`
- **Value**: `dkS5_6Zm8E-ElF4KzKlwPwZTDm-0_5d2_Q-Re5afhl-yAzFu-Ak5rg==`

### Recommendation Function Key

- **Query Parameter**: `code`
- **Value**: `BiLtlWfdvS4NmIH_Y9_xDnCT1Cs5rOLoLWvenK88PQW8AzFuDX25TA==`

## Endpoints

### Get Music Recommendations

- **Endpoint**: `/recommendation`
- **Description**: Get music recommendations based on a given song name.
- **HTTP Method**: GET

#### Query Parameters:

- `song` (required) - The name of the song for which you want recommendations.

**Request Example:**

```http
GET https://personal-music-recommendation.azurewebsites.net/api/recommendation?code=your_function_key&song=hello
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
- `type` (optional) - The type of search (default: "track").
- `limit` (optional) - The maximum number of search results (default: 5).

**Request Example:**

```http
GET https://personal-music-recommendation.azurewebsites.net/api/search?code=your_function_key&q=hello&type=track&limit=10
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