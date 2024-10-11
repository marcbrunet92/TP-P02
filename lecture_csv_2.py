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
    
        # Récupérer les noms des colonnes depuis l'en-tête
        headers = rows[header_index]
    
        # Transposer les lignes en colonnes
        data_columns = list(zip(*rows[header_index + 2:]))
    
        # Associer les noms des colonnes avec les données correspondantes
        for header, column in zip(headers, data_columns):
            # Convertir les valeurs dans chaque colonne en float (remplacer les virgules par des points)
            donnée_csv[header] = [float(value.replace(',', '.')) for value in column]

    # Afficher le dictionnaire
    return donnée_csv
if __name__ == "__main__":
    print('''lecture d'un fichier de données''')
    print(LectureCSV())
