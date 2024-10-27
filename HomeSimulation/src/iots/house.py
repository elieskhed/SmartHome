import device

class house:
    def __init__(self):
        self.appareils = []

    def ajouter_appareil(self, appareil):
        self.appareils.append(appareil)
    
    def retirer_appareil(self, appareil):
        self.appareils.remove(appareil)

    def afficher_etat(self):
        for appareil in self.appareils:
            print(appareil)