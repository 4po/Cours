#==============================================================#

                            # Liste

x = [valeur_1 ,valeur_2, ... , valeur_n] #création d'une liste

#==============================================================#

          #Afficher, editer ajouter les valeurs d'une liste

x = ['chocolat','courgette','tomate']

print(x[0])
#Console : chocolat

print(x[1])
#Console : courgette

print(x[3])
#Console : tomate

x[1] = 'test'
#Console : test
#Et x sera modifié en x = ['chocolat','test','tomate']

x.append('test')
#Et x sera modifié en x = ['chocolat','courgette','tomate', 'test']

#==============================================================#


                     #Parcourir une liste

x = ['chocolat','courgette','tomate']

for i in x :
    print(i)
#Console : chocolat
#          courgette
#          tomate

#==============================================================#
