import azure.functions as func
from http_blueprint import bp

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

app.register_blueprint(bp)