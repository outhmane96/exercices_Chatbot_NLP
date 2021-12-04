import numpy as np
import csv
import collections

def read_csv(file):
	codes = open(file)
	reader = csv.reader(codes)
	list_codes = []
	for row in reader:
		list_codes.append(row)
	list_codes = np.array(list_codes[1 :]).flatten()
	return list_codes
	

def calculate_frequency(code,list_codes):
	counter=collections.Counter(list_codes)	
	return counter[str(code)]




if __name__ == '__main__':
	all_codes = []
	available_codes = []

	all_codes= read_csv('tous les codes.csv')
	available_codes = read_csv('codes disponibles.csv')
	#print(len(all_codes))

	

	number_all_codes = len(list(dict.fromkeys(all_codes)))
	number_available_codes = len(list(dict.fromkeys(available_codes)))

	print('number of all code without duplication :',number_all_codes)
	print('number of available codes without duplication',number_available_codes)

	percentage = (number_available_codes * 100)/ number_all_codes
	print("The percentage of available codes compared to all codes: {:.2f}".format(percentage))

	number_of_occurence = calculate_frequency(100630,available_codes)
	print('The number of occurences is :' , number_of_occurence)


