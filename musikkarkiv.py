from sang import Sang
from spilleliste import Spilleliste
def hovedprogram():
    print("Starting the program...")
    mine_spillelister = {}
    musikk = Spilleliste("musikk")
    musikk.les_fra_fil()
    mine_spillelister["musikk"] = musikk
    queen = Spilleliste("Queen")
    queen.legg_til_sang(musikk.hent_artist_utvalg("Queen"))
    mine_spillelister["queen"] = queen
    favoritt_spilleliste = Spilleliste("Favoritt")
    favoritt_spilleliste.legg_til_sang(Sang("Money", "Pink Floyd"))
    favoritt_spilleliste.legg_til_sang(Sang("Mercedes Benz", "Janis Joplin"))
    favoritt_spilleliste.legg_til_sang(Sang("Help", "The Beatles"))
    mine_spillelister["favoritt"] = favoritt_spilleliste
    mine_spillelister["favoritt"].spill_alle()
    print("Program finished.")

hovedprogram()