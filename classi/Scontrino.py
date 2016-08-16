
class Scontrino:    
    
    def __init__(self):
        pass
    
    def __init__(self, carrello):
        self.carrello = carrello
    
    def stampaScontrino(self):
        testo = "pyMarket \n\n Lista prodotti: \n"        
        testo += self.carrello.__str__()        
        testo += "\n\n Arrivederci e grazie "
        
        file = open("scontrino.txt","w")
        file.write(testo)
        file.close()
        
        print("Stampa scontrino effettuata")