# LIBRARIES
import numpy as np
import pandas as pd

#TODO 1.1. Creează o funcție care primește o propoziție și o separă în funcție de un separator dat ca parametru (spațiu, punct etc).

# def separateByKey(sentence, separator):
#     sentence = str(sentence).split(separator)
#     print(sentence)

# separateByKey("Hello world"," ")



#TODO: 1.2. Creează o funcție care primește o listă de cuvinte și returnează lista cuvintelor unice.

# def noDuplicates(listOfWords):
#     listOfWords = list(set(listOfWords))
#     print(listOfWords)

# noDuplicates(["car", "car", "drink", "food", "food"])



#TODO: 2. Creează un numpy array de 5x5 format din elemente aleatorii. Într-un alt numpy array copiază primele 4 coloane, apoi concatenează o coloană de zerouri. Schimbă primul element din al doilea array și adună-le.

# random_array = np.random.random((5,5)) 
# b = random_array[:, :4]  # primele 4 coloane
# c = np.zeros((5, 1))  # o coloană de zerouri
# d = np.concatenate((b, c), axis=1)  # concatenarea celor două matrice
# d[0, 0] = 1  # schimbarea primului element din array-ul d
# e = random_array + d  # adunarea celor
# print(e)



#TODO: 3.1. Conectează acest Colab la contul tău Drive. Downloadează fișierul Lyrics-Genre.csv și adaugă-l în proiect. Citește datele ca un dataframe Pandas și afișează primele 10 linii.

# filepath = "Lyrics-Genre.csv"
# df = pd.read_csv(filepath)
# print(df[:5])



#TODO: 3.2. Afișează câte datapoints (cântece per gen muzical) există pentru fiecare gen muzical folosind funcții din Pandas.

filepath = "Lyrics-Genre.csv"
df = pd.read_csv(filepath)
print(len(list(set(df['Genre']))), list(set(df['Genre'])))



#TODO: 3.3. Creează următoarele coloane noi pentru dataframe-ul vostru: număr cuvinte, număr cuvinte unice, număr propoziții, densitatea medie a propozițiilor din datapoint (număr propoziții / număr cuvinte). Completează aceste informații.
