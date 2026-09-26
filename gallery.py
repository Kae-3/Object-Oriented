class ArtGallery:
    def __init__(self, gallery_name):
        self.gallery_name = gallery_name
        self.artworks = []  # Empty artwork list by default

    def add_artwork(self, title, artist, year):
        artwork = {"title": title, "artist": artist, "year": year}
        self.artworks.append(artwork)
        print(f"'{title}' by {artist} added to {self.gallery_name}!")

    def view_artworks(self):
        if not self.artworks:
            print(f"\nNo artworks currently in {self.gallery_name}.")
            return

        print(f"\n--- {self.gallery_name} Collection ---")
        for idx, art in enumerate(self.artworks, start=1):
            print(f"{idx}. '{art['title']}' by {art['artist']} ({art['year']})")

    def remove_artwork(self, title):
        for art in self.artworks:
            if art['title'].lower() == title.lower():
                self.artworks.remove(art)
                print(f"'{title}' has been removed from the collection.")
                return
        print(f"Artwork '{title}' not found in the collection.")

    # Destructor method to show object cleanup
    def __del__(self):
        print(f"\n[System] ArtGallery object for '{self.gallery_name}' has been closed and deleted.")


# Menu-driven interface
def main():
    gallery_name = input("Enter the name of your Art Gallery: ")
    gallery = ArtGallery(gallery_name)

    while True:
        print("\n=== ART GALLERY MENU ===")
        print("1. Add Artwork")
        print("2. View Artworks")
        print("3. Remove Artwork")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            title = input("Enter artwork title: ")
            artist = input("Enter artist name: ")
            year = input("Enter year of creation: ")
            gallery.add_artwork(title, artist, year)
        elif choice == "2":
            gallery.view_artworks()
        elif choice == "3":
            title = input("Enter artwork title to remove: ")
            gallery.remove_artwork(title)
        elif choice == "4":
            print("Exiting Art Gallery Collection Manager...")
            del gallery  # Triggers the destructor (__del__)
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()