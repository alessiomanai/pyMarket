
from classi.Prodotto import Prodotto
from classi.Carrello import Carrello
from classi.Scontrino import Scontrino

print("pyMarket")
print("A simple Python code example")


pomodoro = Prodotto("pomodoro", 1)
pasta = Prodotto("pasta", 0.99)
acqua = Prodotto("acqua", 0.3)

carrello = Carrello([pomodoro, acqua, pasta])

carrello.aggiungiOggetto(Prodotto("libro", 15))

print(carrello)

scontrino = Scontrino(carrello)

scontrino.stampaScontrino()