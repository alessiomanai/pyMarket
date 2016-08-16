
class Prodotto:
    
    nome = ""
    prezzo = 0
    
    def __init__(self, nome, prezzo):
        self.setNome(nome)
        self.setPrezzo(prezzo)
        
    def getPrezzo(self):
        return self.prezzo
        
    def setPrezzo(self, prezzo):
        self.prezzo = prezzo
        
    def setNome(self, nome):
        self.nome = nome
        
    def getNome(self):
        return self.nome
        
    def __str__(self):
        return "Nome: " + self.nome + " - Prezzo: " + str(self.prezzo) + " Euro"