import random

# Predefined genres and moods for auto-generated playlist names
GENRES = ["Pop", "Rock", "Hip-Hop", "Jazz", "Classical", "Electronic", "R&B"]
MOODS = ["Chill", "Workout", "Party", "Romantic", "Focus", "Relax"]

# Function to auto-generate a cool playlist name
def generate_playlist_name(selected_songs):
    genres = set(song["genre"] for song in selected_songs)
    moods = set(song["mood"] for song in selected_songs)
    genre_part = random.choice(list(genres)) if genres else random.choice(GENRES)
    mood_part = random.choice(list(moods)) if moods else random.choice(MOODS)
    return f"{mood_part} {genre_part} Vibes"

# Function to create a playlist
def create_playlist(selected_songs):
    suggested_name = generate_playlist_name(selected_songs)
    print(f"Suggested Playlist Name: {suggested_name}")

    custom_name = input("Enter a custom name for your playlist (press Enter to keep the suggested name): ").strip()
    playlist_name = custom_name if custom_name else suggested_name

    playlist = {
        "name": playlist_name,
        "songs": selected_songs,
    }
    print(f"Playlist '{playlist_name}' created successfully!")
    return playlist

# Sample song data (example input)
songs = [
    {"title": "Song A", "artist": "Artist 1", "genre": "Pop", "mood": "Chill"},
    {"title": "Song B", "artist": "Artist 2", "genre": "Rock", "mood": "Workout"},
    {"title": "Song C", "artist": "Artist 3", "genre": "Jazz", "mood": "Relax"},
]

# User selects songs for the playlist
print("Selected Songs:")
for i, song in enumerate(songs, 1):
    print(f"{i}. {song['title']} by {song['artist']} ({song['genre']}, {song['mood']})")

# Creating a playlist
playlist = create_playlist(songs)

# Display the playlist
print("\nYour Playlist:")
print(f"Name: {playlist['name']}")
print("Songs:")
for song in playlist["songs"]:
    print(f"- {song['title']} by {song['artist']} ({song['genre']}, {song['mood']})")
