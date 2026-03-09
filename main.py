
class employe:
    def __init__(self,nom,prenom,npermis):
        self.nom = nom
        self.prenom = prenom
        self.npermis = npermis
        self.voiture = None
    def afficher_info(self):
        info = f"employe: {self.nom}, prenom: {self.prenom} {self.npermis}"
        if self.voiture:
            info += f",voiture attribuee: {self.voiture.marque} {self.voiture.modele} {self.voiture.immatriculation}"
        else:
            info += ",pas de voiture attribuee"
        print(info)
    def attribuer_voiture(self,voiture):
        if self.voiture:
            print(f"{self.nom} {self.prenom} {self.npermis}a deja une voiture")
        elif voiture.employe:
            print (f"la voiture {voiture.marque} {voiture.modele} est deja attribuee a {voiture.employe.nom} {voiture.employe.prenom} {voiture.employe.npermis}")
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
            print(f"{self.nom} {self.prenom} {self.npermis} n a pas de voiture a retirer")
class voiture:
    def __init__(self,marque,modele,immatriculation,annee,km):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.km = km
        self.immatriculation = immatriculation
        self.employe = None
    def afficher_info(self):
        info = f"voiture: {self.marque} {self.modele} {self.immatriculation} {self.annee} {self.km}"
        if self.employe:
            info  += (f",attribuee a : {self.employe.nom} {self.employe.prenom} {self.employe.npermis }")
        else:
            info += ",pas d,employe attribuee"
        print(info)

e1=employe("hamdaoui","laala","h35409")
e2=employe("bourj","lina","l08567")
e3=employe("boukhalfa","ali","g56439")

v1=voiture("toyota","yaris","X50 MPC","2007","139000")
v2=voiture("renault","clio","y50 oPC","2009","140000")
v3=voiture("peugeot","207","R65 GEK","2012","120999")

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
