import azure.functions as func
import json
import os
from Spotify_API import get_recommendation, search, get_token, genre

bp = func.Blueprint()

client_id = os.environ.get("Client_ID")
client_secret = os.environ.get("Client_Secret")


# TODO Token Management and Caching
# TODO Centralizing Error Handling and Response Generation


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

    token = get_token(client_id, client_secret)

    if song and genre:
        recommendation_list = get_recommendation(
            token=token, song=song, genre=genre, limit=limit
        )
    elif song:
        recommendation_list = get_recommendation(token=token, song=song, limit=limit)
    elif genre:
        recommendation_list = get_recommendation(token=token, genre=genre, limit=limit)
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
    limit = req.params.get("limit", 5)
    try:
        limit = int(limit)
        if not 1 <= limit <= 100:
            raise ValueError("Limit out of range")
    except (TypeError, ValueError):
        limit = 5

    token = get_token(client_id, client_secret)
    if not query:
        error_response = {"error": "Missing query parameter", "status_code": 400}
        return func.HttpResponse(
            json.dumps(error_response), mimetype="application/json", status_code=400
        )

    search_results = search(token, query, limit)

    return func.HttpResponse(json.dumps(search_results), mimetype="application/json")


@bp.route(route="genre")
def available_genre(req: func.HttpRequest) -> func.HttpResponse:
    token = get_token(client_id, client_secret)
    available_genre_list_result = genre(token)
    return func.HttpResponse(
        json.dumps(available_genre_list_result), mimetype="application/json"
    )
