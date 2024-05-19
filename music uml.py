class User:
    def _init_(self, id, username):
        self.id = id
        self.username = username
        self.playlists = []
        self.ratings = []

    def create_audio(self, url, name):
        audio = Audio(url, name)
        return audio

    def create_playlist(self, name, genre):
        playlist = Playlist(name, genre)
        self.playlists.append(playlist)
        return playlist

    def search_audio(self, name):
        matching_audios = []
        for playlist in self.playlists:
            matching_audios.extend(playlist.search_audio(name))
        return matching_audios

    def search_playlist(self, name):
        matching_playlists = []
        for playlist in self.playlists:
            if playlist.name == name:
                matching_playlists.append(playlist)
        return matching_playlists

    def rate_playlist(self, playlist, rating):
        playlist.add_rating(rating)
        self.ratings.append(rating)

    def rate_audio(self, audio, rating):
        audio.add_rating(rating)
        self.ratings.append(rating)


class Audio:
    def _init_(self, url, name):
        self.url = url
        self.name = name
        self.ratings = []

    def add_rating(self, rating):
        self.ratings.append(rating)


class Playlist:
    def _init_(self, name, genre):
        self.name = name
        self.genre = genre
        self.audios = []
        self.ratings = []

    def add_audio(self, audio):
        self.audios.append(audio)

    def search_audio(self, name):
        matching_audios = []
        for audio in self.audios:
            if audio.name == name:
                matching_audios.append(audio)
        return matching_audios

    def add_rating(self, rating):
        self.ratings.append(rating)


class Rating:
    def _init_(self, value):
        self.value = value


class Search:
    @staticmethod
    def search_audio_by_name(playlists, name):
        matching_audios = []
        for playlist in playlists:
            matching_audios.extend(playlist.search_audio(name))
        return matching_audios

    @staticmethod
    def search_playlist_by_name(playlists, name):
        matching_playlists = []
        for playlist in playlists:
            if playlist.name == name:
                matching_playlists.append(playlist)
        return matching_playlists
