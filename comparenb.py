# *******************************************************
# Nom ......... : comparenb.py
# Rôle ........ : Programme destiné à comparer l'ordre de grandeur entre deux nombres en complément à 2.
# Auteur ...... : Faure Alexandre
# Version ..... : V0.3 du 27/08/2022
# Licence ..... : Réalisé dans le cadre du cours de Architecture des Ordinateurs et d'Outils Collaboratifs. (L1)
# Utilisation . : Après avoir définit la fonction comparenb, entrez comparenb(), le terminal vous demandera de rentrer deux nombres. 
#********************************************************/
def comparenb():

	print("Veuillez entrer deux nombres écrit en complément à deux ayant le même nombre de bit")
	nb1 = input()
	nb2 = input()


	listenb1 = [c for c in nb1]
	listenb2 = [c for c in nb2]


	# Si les deux nombres sont identiques
	if nb1 == nb2:
		print("Les deux nombres sont égaux")

	# le premier nombre est positif
	elif nb1[0] == "0":

		# Le second nombre est négatif donc inférieur
		if nb2[0] == "1":
			print("Le premier nombre :", nb1, "est le plus grand des deux.")

		# Les deux sont positifs
		else :


			# On va comparer, de gauche à droite, chaque bit des deux nombres
			while len(listenb1) and len(listenb2) >= 0 :

				# Les deux bits sont identiques, cela ne permet pas de départager les deux nombres
				while listenb1[0] == listenb2[0]:
					listenb1.remove(listenb1[0])
					listenb2.remove(listenb2[0])

				# Si le bit de gauche du premier nombre est supérieur à celui du deuxième, alors le premier nombre est plus grand
				if int(listenb1[0]) > int(listenb2[0]):
					print("Le premier nombre : ", nb1, "est le plus grand des deux.")
					# On vide les listes pour sortir de la boucle
					listenb1.clear()
					listenb2.clear()

				# Cas inverse, le deuxième nombre est le plus grand
				elif int(listenb1[0]) < int(listenb2[0]):
					print("Le deuxième nombre :", nb2, "est le plus grand des deux.")
					listenb1.clear()
					listenb2.clear()


	# Le premier nombre est négatif
	elif nb1[0] == "1":

		# Le second nombre est positif donc supérieur
		if nb2[0] == "0":
			print("Le deuxième nombre :", nb2, "est le plus grand des deux.")	


		# Les deux sont négatifs
		else :

			# On va comparer, de gauche à droite, chaque bit des deux nombres 
			while len(listenb1) and len(listenb2) > 0 :

				# Les deux bits sont identiques, cela ne permet pas de départager les deux nombres, on passe aux suivants
				while listenb1[0] == listenb2[0]:
					listenb1.remove(listenb1[0])
					listenb2.remove(listenb2[0])

				# Si le bit de gauche du premier nombre est inférieur à celui du deuxième, alors le premier nombre est plus grand
				if int(listenb1[0]) > int(listenb2[0]):
					print("Le premier nombre : ", nb1, "est le plus grand des deux.")
					listenb1.clear()
					listenb2.clear()

				# Cas inverse, le deuxième nombre est le plus grand
				elif int(listenb1[0]) < int(listenb2[0]):
					print("Le deuxième nombre :", nb2, "est le plus grand des deux.")
					listenb1.clear()
					listenb2.clear()


	else :
		print("Vous n'avez pas entré un nombre binaire en complément à deux. Veuillez réessayer")



comparenb()