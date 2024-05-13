import random


class Album:
    my_album = []

    def __init__(self, file):
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                name, duration, artist, year = line.strip().split(' - ')

                Album.my_album.append(Track(name, duration, artist, year))

    @classmethod
    def play(cls):
        print(f'Сейчас играет: {cls.my_album[0]}')
        beg_track = cls.my_album[0]
        cls.my_album.remove(beg_track)
        cls.my_album.append(beg_track)

    @classmethod
    def shuffle_album(cls):
        random.shuffle(cls.my_album)

    @classmethod
    def show_album(cls):
        for elem in cls.my_album:
            print(str(elem))
        print('\n')

    @classmethod
    def pause(cls):
        print('Пауза')
        end_track = cls.my_album[-1]
        cls.my_album.remove(end_track)
        cls.my_album.insert(0, end_track)

    @classmethod
    def continue_track(cls):
        cls.play()

    @staticmethod
    def stop_album():
        print('Проигрывание альбома остановлено')


class Track:
    def __init__(self, name, duration, artist, year):
        self.name = name
        self.duration = duration
        self.artist = artist
        self.year = year
        self.seconds_duration = int(duration.split(':')[0]) * 60 + int(duration.split(':')[1])

    def __str__(self):
        return f'{self.name} - {self.artist} [{self.year}] - {self.duration}'

    def __repr__(self):
        return [self.name, self.artist, self.seconds_duration, self.year]


new_album = Album('album.txt')
new_album.show_album()
new_album.shuffle_album()
new_album.show_album()
new_album.play()
new_album.play()
new_album.pause()
new_album.continue_track()
new_album.play()
new_album.stop_album()
