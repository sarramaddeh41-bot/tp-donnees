def somme_valeurs(liste):
    return sum(liste)

def nb_elements(liste):
    return len(liste)

def val_centrale(liste):
    return liste[2]
def produit_valeurs(liste):
    s=1
    for i in range(len(liste)):
        s=s*liste[i]
    return s
        
liste=[4,7,2,9,5]
print("somme valeurs",somme_valeurs(liste))
print("nombre d'elements",nb_elements(liste))
print("valeur centrale",val_centrale(liste))
print("le produit de valeurs",produit_valeurs(liste))