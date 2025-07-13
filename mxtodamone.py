import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="Your Client ID",
    client_secret="Your Client Secret ID",
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-read-playback-state user-modify-playback-state user-read-currently-playing",
    cache_path="token_cache.txt"
))

try:
    while True:
        playback = sp.current_playback()

        if playback and playback["is_playing"]:
            track_name = playback["item"]["name"]
            artist_name = playback["item"]["artists"][0]["name"]
            progress = playback["progress_ms"]

            print("Currently playing:", track_name)
            print("Artist:", artist_name)
            print("Progress (ms):", progress)

            if track_name == "Creep" and artist_name == "Radiohead":
                sp.start_playback(uris=["spotify:track:28kObNFRLVjnB0sw4K4W8I"])
                print("Skipped Creep, enjoy this instead.")

            if track_name == "MX" and progress >= 285000 and progress < 1955000:
                sp.seek_track(1955000)
                print("Skipped to Damone!")
        else:
            print("Nothing is playing.")

        time.sleep(10)

except KeyboardInterrupt:
    print("\nStopped by user.")
