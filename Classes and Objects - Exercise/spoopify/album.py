from project.song import Song


class Album:

    def __init__(self, name: str, *new_songs):
        self.name = name
        self.published = False
        self.songs = []
        if new_songs:
            for song in new_songs:
                self.add_song(song)

    def add_song(self, song: Song) -> str:
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return f"Cannot add songs. Album is published."
        if song in self.songs:
            return f"Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        for i in range(len(self.songs) - 1, - 1, - 1):
            if self.songs[i].name == song_name:
                if self.published:
                    return "Cannot remove songs. Album is published."
                self.songs.pop(i)
                return f"Removed song {song_name} from album {self.name}."
        return f"Song is not in the album."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."
        return f"Album {self.name} is already published."

    def details(self):
        result = [f"Album {self.name}"]
        for song in self.songs:
            result.append(f"== {song.get_info()}")
        return '\n'.join(result)
