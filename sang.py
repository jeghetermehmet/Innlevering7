class Sang:
    def __init__(self, tittel, artist):
        self._tittel = tittel
        self._artist = artist
    def spill(self):
        print("Nå spilles", self._tittel, "med", self._artist)
    def sjekk_artist(self, navn):
        navn = navn.lower().split()
        artist_words = self._artist.lower().split()
        for word in artist_words:
            if word in navn:
                return True
        return False
    def sjekk_tittel(self, tittel):
        return self._tittel.lower() == tittel.lower()
    def sjekk_artist_og_tittel(self, artist, tittel):
        return (self.sjekk_artist(artist) and self.sjekk_tittel(tittel))
    def streng_til_fil(self):
        return f"{self._tittel};{self._artist}\n"



    
     