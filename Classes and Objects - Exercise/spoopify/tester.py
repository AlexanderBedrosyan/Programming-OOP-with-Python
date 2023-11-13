from project.song import Song
from project.album import Album
from project.band import Band


band = Band("Death")
album = Album("The Sound of Perseverance")
print(band.remove_album("The Sound of Perseverance"))
expected = "Album The Sound of Perseverance is not found."
#
#
# band = Band("Death")
# album = Album("The Sound of Perseverance")
# album.publish()
# band.add_album(album)
# message = band.remove_album("The Sound of Perseverance")
# expected = "Album has been published. It cannot be removed."



# if __name__ == '__main__':
#     unittest.main()