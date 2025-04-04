class Album:
    def __init__(self,album_name,number_of_songs,album_artist):
        self.album_name=album_name
        self.number_of_songs=number_of_songs
        self.album_artist=album_artist
    def __str__(self):
        return f"({self.album_name},{self.album_artist},{self.number_of_songs})"
    def __repr__(self):
        return self.__str__()
albums1=[
    Album("Thriller",9,"Michael Jackson"),
    Album("Back in Black",10,"AC/DC"),
    Album("The Bodyguard",12,"Whitney Houston"),
    Album("Bat Out of Hell",7,"Meat Loaf"),
    Album("Their Greatest Hits",14,"Eagles")]
print("Original albums1:")
print(albums1)
albums1.sort(key=lambda album:album.number_of_songs)
print("\nSorted by number of songs:")
print(albums1)
albums1[0],albums1[1]=albums1[1],albums1[0]
print("\nAfter swapping positions 0 and 1:")
print(albums1)
albums2=[
    Album("Rumours",11,"Fleetwood Mac"),
    Album("Saturday Night Fever",17,"Bee Gees"),
    Album("Come On Over",16,"Shania Twain"),
    Album("Led Zeppelin IV",8,"Led Zeppelin"),
    Album("Bad",10,"Michael Jackson")]
print("\nOriginal albums2:")
print(albums2)
albums2.extend(albums1)
albums2.append(Album("Dark Side of the Moon",9,"Pink Floyd"))
albums2.append(Album("Oops!... I Did It Again",16,"Britney Spears"))
albums2.sort(key=lambda album:album.album_name)
print("\nSorted albums2 by album name:")
print(albums2)
search_title="Dark Side of the Moon"
index=next((i for i,album in enumerate(albums2) if album.album_name==search_title),-1)
print(f"\nIndex of '{search_title}':{index}")