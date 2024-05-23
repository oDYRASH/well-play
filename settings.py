import os

# from dotenv import load_dotenv#remove pour push

# load_dotenv()#remove pour push

VALORANT_API_KEY = os.getenv("VALORANT_API_KEY")
CLIENT_ID = os.getenv('RIOT_CLIENT_ID')
CLIENT_SECRET = os.getenv('RIOT_CLIENT_SECRET')
REDIRECT_URI = 'http://localhost:5000/callback'#https://www.wellplaytournament.com/callback'
AUTHORIZATION_BASE_URL = 'https://auth.riotgames.com/oauth2/authorize'
TOKEN_URL = 'https://auth.riotgames.com/oauth2/token'