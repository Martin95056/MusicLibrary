from datetime import time


class Song:
    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self._length = length

    def __str__(self):
        return '{} - {} from {} - {}'.format(self.artist, self.title, self.album, self._length)

    def __eq__(self, other):
        return self.title == other.title and self.artist == other.artist and self.album == other.album and self._length == other._length

    def __hash__(self):
        return self.__str__()

    def set_length(self):
        t = self._length.split(":")
        if len(t) == 3:
            return time(int(t[0]), int(t[1]), int(t[2]))
        elif len(t) == 2:
            return time(minute=int(t[0]), second=int(t[1]))

    def length(self, seconds=False, minutes=False, hours=False):
        if seconds:
            return int(self.set_length().hour * 3600 + self.set_length().minute * 60 + self.set_length().second)
        elif minutes:
            return int(self.set_length().hour * 60 + self.set_length().minute)
        elif hours:
            return int(self.set_length().hour)
        else:
            return self.set_length().strftime("%h:%M:%S")

    def song_to_dict(self):
        dic = {
            "title": self.title,
            "artist": self.artist,
            "album": self.album,
            "length": self._length
        }

        return dic
