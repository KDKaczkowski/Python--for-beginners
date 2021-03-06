'''Mamy plik personal_data_homework.csv. Plik ma tę samą strukturę, co plik omawiany na zajęciach. Tym razem naszym zadaniem jest oczyścić pole id_number.

Specyfikacja id_number
{dwuliterowy_skrót_nazwy_działu}/{sześciocyfrowy_numer}/{rok_zatrudnienia}

na przykład:

- "ZA/434503/2005"
- "IT/222345/2009"
- "OC/983421/2017"

A dokładniej:

- Skrót nazwy działu
    - jeden z: {'ZA', 'IT', 'KS', 'KA', 'LO', 'SP', 'MA', 'CZ', 'OC'}
    - wielkimi

- Sześciocyfrowy numer:
    - 123456 ok
    - 12345 nie ok
    - 12345x nie ok
    - 1234.5 nie ok

- Rok zatrudnienia:
    - od 1900
    - do 2018

ZADANIE 1: liczenie unikalnych id_number przed czyszczeniem
Napisz funkcję `count_unique_id_numbers_before_clean`, która przyjmie nazwę pliku csv (str), a zwróci inta, którego wartością będzie liczba unikalnych wartości id_number w przekazanym pliku csv. Ma być to wartość przed jakimkolwiek czyszczeniem pliku csv. Do testów używamy pliku personal_data_homework.csv. Formatowanie pliku to UTF-8.

Na przykład:

Dla wejściowych danych (ignoruję tu inne kolumny, w pliku będą wszystkie, co na zajęciach):

1. "KA/123456/2005"
2. "IT/111111/2001"
3. "IT/111111/2001"
4. "IT/111111/   2001"

Unikalnych wartości `id_number` jest `3` (trzy):

- "KA/123456/2005" (1.) 
- "IT/111111/2001" (2. i 3.) 
- "IT/111111/   2001" (4.)

Pozycja 4. nie równa się pozycji 2. oraz 3., bo ma dodatkowe spacje w środku.'''

# zadanie 1
import csv

def count_unique_id_numbers_before_clean(filename):
  people=get_csv_lines(filename)
  a={
    person['id_number']
    for person in people
      if person['id_number'] is not None
  }
  
  return len(a)

def get_csv_lines(filename):
    with open(filename, encoding='utf8') as csv_file:
      reader = csv.DictReader(csv_file, delimiter=',')
      for row in reader:
        yield row



assert count_unique_id_numbers_before_clean('personal_data_homework.csv') == 1588