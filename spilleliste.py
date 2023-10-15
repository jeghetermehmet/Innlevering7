from sang import Sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn
    def les_fra_fil(self):
        data = open(self._navn + ".txt", "r")
        for linje in data:
            sanger =linje.strip().split(";")
            tittel, artist = sanger[0], sanger[1]
            sang = Sang(tittel, artist)
            self._sanger.append(sang)
        data.close()
    def legg_til_sang(self, ny_sang):
        self._sanger.append(ny_sang)
    def fjern_sang(self, sang):
        self._sanger.remove(sang)
    def spill_alle(self):
        for sang in self._sanger:
            sang.spill()
    def finn_sang_tittel(self, tittel):
        for sang in self._sanger:
            if sang.sjekk_tittel(tittel):
                return sang
        return None
    def hent_artist_utvalg(self, artistnavn):
        artister = []
        for artist in self._sanger:
            if artist.sjekk_artist(artistnavn):
                artister.append(artist)
        return artister
    def skriv_til_fil(self):
        with open(f"{self._navn}.txt", "w") as fil:
            for sang in self._sanger:
                fil.write(f"{sang.streng_til_fil()}")
        
                



    
    
