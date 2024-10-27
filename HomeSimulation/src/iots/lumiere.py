import device

class lumiere(device):
    def __init__(self, nom, etat=False):
        super().__init__(nom)
        self.__etat = etat

    def allumer(self):
        self.etat = True

    def eteindre(self):
        self.etat = False

    def __str__(self):
        return f"Lumière {self.nom} - {'Allumée' if self.etat else 'Éteinte'}"