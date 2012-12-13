fichier = open("Liste.md", "r")
lignes = fichier.readlines()

for ligne in lignes :
    temp = ligne.split(" [Utilite]")
    if len(temp) > 1 :
        print temp
        ligne = temp[0].replace("    * ","")
        ligne = ligne.replace(".","")
        ligne = ligne.replace("/","")
        ligne = ligne.replace("&","")
        ligne = ligne.replace("'"," ")
        ligne = ligne.replace("  "," ")
        temp = ligne
        tag1 = ligne.replace(" ","")
        tag2 = ligne.replace(" ",",")
        ligne = ligne.replace(" ","_")
        print ligne
        fichier2 = open("%s.md"%ligne, "w+")
        texte = """Date: 2012-12-07
Title: %s
Category: Objet
Tags: Objet,%s,%s
        """%(temp,tag1,tag2)
        fichier2.write(texte)
        fichier2.close()
fichier.close()
        