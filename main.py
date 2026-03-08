from encodings.punycode import selective_find


class employe:
    def __init__(self,nom,prenom):
        self.nom = nom
        self.prenom = prenom
        self.voiture = None
    def afficher_info(self):
        info = f"employe: {self.nom}, prenom: {self.prenom}"
        if self.voiture:
            info += f",voiture attribuee: {self.voiture.marque} {self.voiture.model} {self.voiture.imatriculation}"
        else:
            info += ",pas de voiture attribuee"
        print(info)
    def attribuer_voiture(self,voiture):
        if self.voiture:
            print(f"{self.nom} {self.prenom} a deja une voiture")
        elif voiture.employe:
            print (f"la voiture {voiture.marque} {voiture.model} est deja attribuee a {voiture.employe.nom} {voiture.employe.prenom}")
        else:
            self.voiture=voiture
            voiture.employe=self
            print(f"Voiture {voiture.marque} {voiture.modele} attribuée à {self.nom} {self.prenom}")
    def retirer_voiture(self):
        if self.voiture:
            print(f"voiture {self.voiture.marque} {self.voiture.model} retirer voiture de {self.nom} {self.prenom}")
            self.voiture.employe= None
            self.voiture= None
        else:
            print(f"{self.nom} {self.prenom} n a pas de voiture a retirer")
class voiture:
    def __init__(self,marque,model,imatriculation):
        self.marque = marque
        self.model = model
        self.imatriculation = imatriculation
        self.employe = None