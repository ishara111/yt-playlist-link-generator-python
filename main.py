import sys
from pytube import Playlist

playlistUrl = input("Enter youtube playlist URL: ")
p = Playlist(playlistUrl)
print()
print(f"Playlist Title: {p.title}")
print()

original_stdout = sys.stdout
rep = True
while rep==True:
    fileType = input("Enter file type csv or txt: ")
    if fileType =="txt":
        with open('playlist_links.txt', 'w') as f:
            sys.stdout = f # Change the standard output to the file we created.
            for url in p.video_urls:
                print(url)
            sys.stdout = original_stdout # Reset the standard output to its original value
            break
    elif fileType =="csv":
        with open('playlist_links.csv', 'w') as f:
            sys.stdout = f # Change the standard output to the file we created.
            for url in p.video_urls:
                print(url)
            sys.stdout = original_stdout # Reset the standard output to its original value
            break
    else:
        print("incorrect filetype")

print("Done")