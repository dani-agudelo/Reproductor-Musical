class Song():
    def __init__(self, code, artist, name, album, year):
        self.__code=code
        self.__name=name
        self.__artist=artist
        self.__album=album
        self.__year=year

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, c):
        self.__code=c

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n):
        self.__name=n

    @property
    def artist(self):
        return self.__artist

    @artist.setter
    def artist(self, a):
        self.__artist=a

    @property
    def album(self):
        return self.__album

    @album.setter
    def album(self, a):
        self.__album=a

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, y):
        self.__year=y

    def __str__(self):
        return str(self.code)+' '+str(self.name)+' '+str(self.artist)+' '+str(self.album)+' '+str(self.year)


