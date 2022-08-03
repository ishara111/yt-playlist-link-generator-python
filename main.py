from pytube import Playlist

playlistUrl = input("Enter youtube playlist URL: ")
p = Playlist(playlistUrl)
print()
print(f"Playlist Title: {p.title}")
print()

for url in p.video_urls:
    print(url)
