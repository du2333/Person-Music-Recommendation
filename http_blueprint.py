import azure.functions as func
import json
import os
from Spotify_API import Spotify

bp = func.Blueprint()

client_id = os.environ.get("Client_ID")
client_secret = os.environ.get("Client_Secret")


spotify = Spotify(client_id, client_secret)


@bp.route(route="recommendation")
def recommendation_function(req: func.HttpRequest) -> func.HttpResponse:
    song = req.params.get("song")
    genre = req.params.get("genre")
    limit = req.params.get("limit")
    try:
        limit = int(limit)
        if not 1 <= limit <= 100:
            raise ValueError("Limit out of range")
    except (TypeError, ValueError):
        limit = 5

    if song and genre:
        recommendation_list = spotify.get_recommendation(
            song=song, genre=genre, limit=limit
        )
    elif song:
        recommendation_list = spotify.get_recommendation(song=song, limit=limit)
    elif genre:
        recommendation_list = spotify.get_recommendation(genre=genre, limit=limit)
    else:
        error_response = {
            "error": "Please provide either a 'genre' or a 'song' parameter, or both",
            "status_code": 400,
        }

        return func.HttpResponse(
            json.dumps(error_response), mimetype="application/json", status_code=400
        )

    if recommendation_list:
        return func.HttpResponse(
            json.dumps(recommendation_list), mimetype="application/json"
        )
    else:
        error_response = {"error": "No recommendations found", "status_code": 404}
        return func.HttpResponse(
            json.dumps(error_response), mimetype="application/json", status_code=404
        )


@bp.route(route="search")
def search_function(req: func.HttpRequest) -> func.HttpResponse:
    query = req.params.get("q")
    limit = req.params.get("limit")
    try:
        limit = int(limit)
        if not 1 <= limit <= 100:
            raise ValueError("Limit out of range")
    except (TypeError, ValueError):
        limit = 5

    if not query:
        error_response = {"error": "Missing query parameter", "status_code": 400}
        return func.HttpResponse(
            json.dumps(error_response), mimetype="application/json", status_code=400
        )

    search_results = spotify.search(query=query, limit=limit)

    return func.HttpResponse(json.dumps(search_results), mimetype="application/json")


@bp.route(route="genre")
def available_genres(req: func.HttpRequest) -> func.HttpResponse:
    available_genre_list_result = spotify.genres()
    return func.HttpResponse(
        json.dumps(available_genre_list_result), mimetype="application/json"
    )
