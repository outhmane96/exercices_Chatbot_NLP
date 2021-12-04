import numpy as np
import csv
import collections
import statistics
import matplotlib.pyplot as plt

# lire le fichier csv et mettre les codes dans un numpy array
def read_csv(file):
	codes = open(file)
	reader = csv.reader(codes)
	list_codes = []
	for row in reader:
		list_codes.append(row)
	list_codes = np.array(list_codes[1 :]).flatten()
	return list_codes
	
# calcul de la fréquence pour chaque code en utilisant collections
def calculate_frequency(code,list_codes):
	code_frequency=collections.Counter(list_codes)	
	return code_frequency[str(code)]

#comparer la liste des fréquences donnée
def compare_frequency(list_codes,available_codes):
	list_frequencies = []

	# pour chaque code calculer la fréquence en utilisant la fonction calculate_frequency
	for code in list_codes:
		list_frequencies.append(calculate_frequency(code,available_codes))
	print(list_frequencies)
	# aficher un barplot contenant les frequences des codes
	plt.bar([str(x) for x in list_codes],list_frequencies, color ='blue',
			width = 0.4)
	plt.xlabel("Codes")
	plt.ylabel("Frequences")
	plt.title("La fréquence de chaque code")
	plt.show()

# les statistiques concernant les frquences des codes 
def analyse_frequencies(list_codes):
	code_frequency=collections.Counter(list_codes)

	# une list contenant les féquences
	array_frequency = list(code_frequency.values())

	# le min des frequences
	min_freq = min(array_frequency)
	# le max des frequences
	max_freq = max(array_frequency)
	# la mediane des frequences
	median_freq = statistics.median(array_frequency)
	# la moyenne
	mean_freq = sum(array_frequency) / len(array_frequency)

	# list pour les statistiques
	stats = [min_freq,max_freq,median_freq,mean_freq]
	plt.bar(['min = {}'.format(min_freq),'max = {}'.format(max_freq),'median = {:.2f}'.format(median_freq),'mean = {:.2f}'.format(mean_freq)],stats, color ='blue',
			width = 0.4)
	plt.xlabel("Codes")
	plt.ylabel("Frequences")
	plt.title("Statistics")
	plt.show()




if __name__ == '__main__':

	# initialisation des listes de codes
	all_codes = []
	available_codes = []

	# mettre les codes dans les listes
	all_codes= read_csv('tous les codes.csv')
	available_codes = read_csv('codes disponibles.csv')
	
	# numero de tous les codes sans duplication
	number_all_codes = len(list(dict.fromkeys(all_codes)))
	# numero des codes disponibles sans duplication
	number_available_codes = len(list(dict.fromkeys(available_codes)))

	print('number of all code without duplication :',number_all_codes)
	print('number of available codes without duplication',number_available_codes)

	#Calculer le pourcentage des codes disponibles par rapport à tous les codes.
	percentage = (number_available_codes * 100)/ number_all_codes
	print("The percentage of available codes compared to all codes: {:.2f}".format(percentage))


	# Calculer la fréquence d’un code disponible donné.
	code_disponoble = 630790
	number_of_occurence = calculate_frequency(code_disponoble,available_codes)
	print('The number of occurences is :' , number_of_occurence)

	# Afficher un graphique qui compare les fréquences de 5 codes disponibles
	compare_frequency([640520,852351,210690,630790,611693],available_codes)

	# Afficher un graphique qui permet de visualiser le maximum, minimum, médiane,
    #et la moyenne des fréquences des codes disponibles.
	analyse_frequencies(available_codes)

