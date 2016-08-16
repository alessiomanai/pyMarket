
from .Prodotto import Prodotto

class Carrello:
    
    listaOggetti = []
    
    def __init__(self):
        self.listaOggetti = [Prodotto()]
        
    def __init__(self, listaOggetti):
        self.listaOggetti = listaOggetti
        
    def aggiungiOggetto(self, oggetto):
        self.listaOggetti.append(oggetto) #a[len(a):] = [x]
        
    def rimuoviOggetto(self, nome):
        self.listaOggetti.remove(nome)
        
    def rimuoviOggettoDaIndice(self, indice):
        del self.listaOggetti[indice]
        
    def stampaCarrello(self):
        print(self.__str__())
        
    def totaleCarrello(self):
        totale = 0
        numero = len(self.listaOggetti)
        i = 0
        while i < numero:
            totale += self.listaOggetti[i].getPrezzo()
            i += 1
        return totale
        
    def __str__(self):
        numero = len(self.listaOggetti)
        i = 0
        stringa = ""
        while i < numero:
            stringa = stringa + self.listaOggetti[i].__str__() + "\n" 
            i += 1
        
        stringa += "\nTotale: " + str(self.totaleCarrello()) + " Euro"     
        
        return stringa