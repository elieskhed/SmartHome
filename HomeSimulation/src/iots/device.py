class device:
    def __init__(self, nom):
        self.__nom = nom

    def get_nom(self):
        return self.__nom


    def __str__(self):
        return f"{self.nom} - Etat inconnu"