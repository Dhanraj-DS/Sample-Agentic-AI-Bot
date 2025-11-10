from livekit import api

# Replace these with your credentials
API_KEY = "API3oAwCf2oejzX"
API_SECRET = "l3GIsOwYGXKxqhCfuhk0s0c00Z6Mtn0mNLVzYMpShb"

# Create a token that allows joining a specific room
token = api.AccessToken(API_KEY, API_SECRET)
token.identity = "Dhanraj-DS"  # who the user is
token.add_grant(api.VideoGrants(room_join=True, room="jarvis-room"))

# Print the JWT token
print(token.to_jwt())