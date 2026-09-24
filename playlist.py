
class Playlist:

    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.songs = []  # Default attribute

    def add_song(self, song):
        self.songs.append(song)
        print(f"'{song}' added to {self.name}.")


    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"'{song}' removed from {self.name}.")
        else:
            print(f"'{song}' is not in the playlist.")

    def display(self):
        print(f"\n--- Playlist: {self.name} ({self.genre}) ---")
        if not self.songs:
            print("No songs in playlist.")
        else:
            for index, song in enumerate(self.songs, start=1):
                print(f"{index}. {song}")
        print("-----------------------------------")

    # Step 6: Add __del__ destructor
    def __del__(self):
        print(f"Playlist '{self.name}' has been deleted. Goodbye!")


my_playlist = Playlist("Road Trip Mix", "Pop")

while True:
    print("\n--- Music Playlist Manager ---")
    print("1. Add Song")
    print("2. Remove Song")
    print("3. View Playlist")
    print("4. Exit & Delete Playlist")

    choice = input("Enter option (1-4): ")

    if choice == "1":
        song_title = input("Enter song title to add: ")
        my_playlist.add_song(song_title)
    elif choice == "2":
        song_title = input("Enter song title to remove: ")
        my_playlist.remove_song(song_title)
    elif choice == "3":
        my_playlist.display()
    elif choice == "4":
        del my_playlist  # Fires __del__
        break
    else:
        print("Invalid option. Please enter a number from 1 to 4.")