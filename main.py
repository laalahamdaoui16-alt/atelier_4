
class employe:
    def __init__(self,nom,prenom):
        self.nom = nom
        self.prenom = prenom
        self.voiture = None
    def afficher_info(self):
        info = f"employe: {self.nom}, prenom: {self.prenom}"
        if self.voiture:
            info += f",voiture attribuee: {self.voiture.marque} {self.voiture.modele} {self.voiture.immatriculation}"
        else:
            info += ",pas de voiture attribuee"
        print(info)
    def attribuer_voiture(self,voiture):
        if self.voiture:
            print(f"{self.nom} {self.prenom} a deja une voiture")
        elif voiture.employe:
            print (f"la voiture {voiture.marque} {voiture.modele} est deja attribuee a {voiture.employe.nom} {voiture.employe.prenom}")
        else:
            self.voiture=voiture
            voiture.employe=self
            print(f"Voiture {voiture.marque} {voiture.modele} attribuée à {self.nom} {self.prenom}")
    def retirer_voiture(self):
        if self.voiture:
            print(f"voiture {self.voiture.marque} {self.voiture.modele} retirer voiture de {self.nom} {self.prenom}")
            self.voiture.employe= None
            self.voiture= None
        else:
            print(f"{self.nom} {self.prenom} n a pas de voiture a retirer")
class voiture:
    def __init__(self,marque,modele,immatriculation):
        self.marque = marque
        self.modele = modele
        self.immatriculation = immatriculation
        self.employe = None
    def afficher_info(self):
        info = f"voiture: {self.marque} {self.modele} {self.immatriculation}"
        if self.employe:
            info  += (f",attribuee a : {self.employe.nom} {self.employe.prenom}")
        else:
            info += ",pas d,employe attribuee"
        print(info)

e1=employe("hamdaoui","laala")
e2=employe("bourj","lina")
e3=employe("boukhalfa","ali")

v1=voiture("toyota","yaris","X50 MPC")
v2=voiture("renault","clio","y50 oPC")
v3=voiture("peugeot","207","R65 GEK")

print("info initial des employes")
for e in [e1,e2,e3]:
    e.afficher_info()
print("infos initial des voitures")
for v in [v1,v2,v3]:
    v.afficher_info()

e1.attribuer_voiture(v1)
e2.attribuer_voiture(v2)
print("infos apres attributions")
for e in [e1,e2,e3]:
    e.afficher_info()
for v in [v1,v2,v3]:
    v.afficher_info()

e1.retirer_voiture()
print("infos apres retires voitures")
for e in [e1,e2,e3]:
    e.afficher_info()
for v in [v1,v2,v3]:
    v.afficher_info()

e3.attribuer_voiture(v2)
