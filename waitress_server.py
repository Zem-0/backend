from waitress import serve
from backend.wsgi import application
import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    serve(application, host="0.0.0.0", port=port)