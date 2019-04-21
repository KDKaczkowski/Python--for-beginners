'''ZADANIE 3: czyszczenie id_number i liczenie unikalnych id_number po czyszczeniu 
Napisz funkcję count_unique_id_numbers_after_clean, która przyjmie nazwę pliku csv (str), a zwróci inta, którego wartością będzie liczba
unikalnych id_number w przekazanym pliku csv. Ma być to wartość po czyszczeniu pliku csv. Do testów używamy pliku
personal_data_homework.csv (tego samego, co w zadaniu 1). 

Uwagi: 
Funkcję czyszczącą trzeba napisać samemu i wywołać ją w count_unique_id_numbers_after_clean. Mogą przydać się materiały z
wykładu.
W przekazanym pliku nie będzie wartości id_number, której nie da się oczyścić (np. z brakującymi danymi).
W przekazanym pliku nie będzie pustych id_number. 
(Podpowiedź: po oczyszczeniu wszystkich id_number funkcja validate_id_number z poprzedniego zadania powinna zwrócić True dla
wszystkich tych oczyszczonych wartości. validate_id_number musi być oczywiście poprawnie napisana;) 

Przykład: 
Dla wyjściowych danych (ignoruję tu inne kolumny, w pliku będą wszystkie, co na zajęciach):

1. "KA/123456/2005"
2. "IT/111111/2001"
3. "IT/111111/2001"
4. "IT/111111/   2001"

Unikalnych wartości, po czyszczeniu, id_number jest 2 (dwie): 
- "KA/123456/2005" (1.) 
- "IT/111111/2001" (2., 3., 4.)
Jest tak, bo po czyszczeniu "IT/111111/   2001" staje się "IT/111111/2001", czyli tym samym, co pozycje 2. oraz 3.'''


# zadanie 3
import csv
def count_unique_id_numbers_after_clean(filename):
  people=get_csv_lines(filename)
  a=set()
  for line in people:
    line['id_number'] = line['id_number'].strip()
    line['id_number'] = line['id_number'].replace(' ', '')
    line['id_number'] = line['id_number'].replace('\\', '/')
    line['id_number'] = line['id_number'].replace('-', '/')
    line['id_number'] = line['id_number'].replace('.', '/')
    line['id_number'] = line['id_number'].replace('_', '/')
    line['id_number'] = line['id_number'].upper()
    a.add(line['id_number'])
  
  return len(a)

def get_csv_lines(filename):
    with open(filename, encoding='utf8') as csv_file:
      reader = csv.DictReader(csv_file, delimiter=',')
      for row in reader:
        yield row



assert count_unique_id_numbers_after_clean('personal_data_homework.csv') == 1533