from matplotlib.pyplot import *
import csv
def LectureCSV():
    file_path = input("Quel est le nom du fichier de pointage (sans l'extension .csv)? : ")+".csv"
    donnée_csv = {}
    with open(file_path, newline='', encoding='ISO-8859-1') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=';')
        rows = list(csvreader)
        header_index = 0
        for i, row in enumerate(rows):
            try:
                [float(value.replace(',', '.')) for value in row]
            except ValueError:
                header_index = i
                break
        headers = rows[header_index]
        data_columns = list(zip(*rows[header_index + 2:]))
        for header, column in zip(headers, data_columns):
          donnée_csv[header] = [float(value.replace(',', '.')) for value in column]
    return donnée_csv

donnee = LectureCSV()
clé = donnee.keys()
print('quelle est le nom de la variable des abcissses dans le fichier CSV (parmis''', clé, ' ) ? ')
objet = donnee[input()]
print('quelle est le nom de la variable des ordonnées dans le fichier CSV (parmis''', clé, ' ) ? ')
image = donnee[input()]
fig, ax = subplots(num="construction de Bouasse",nrows=1, ncols=1,figsize=(12,6))
grid(visible=True, which='major', color='b', linestyle='-')
grid(visible=True, which='minor', color='g', linestyle='--')
ax.axis("equal")
minorticks_on()
title('construction de Bouasse')
xlabel(r'$\overline{OA}$ en m')
ylabel(r"$\overline{OA'}$ en m")
for i in range(0,len(objet),1):
    axline((objet[i], 0), (0, image[i]),linewidth=1, color='r')
show()
