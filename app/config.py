import os
from dotenv import load_dotenv

load_dotenv()

db_connection = os.environ.get('DB_CONNECTION')
documentation_url = os.environ.get('DOCS_URL', None)
cors_origins = os.environ.get('CORS_ORIGINS', "*")
openapi_key = os.environ.get('OPENWEATHER_API_KEY', None)

