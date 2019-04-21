'''ZADANIE 4: wyznaczanie mediany monthly_salary pięciu najkosztowniejszych pracowników w danym dziale 
Napisz funkcję median_of_top_five, która przyjmuje: 
filename – nazwę pliku CSV, w którym mamy dane (struktura pliku będzie taka sama jak na zajęciach),
department_name – dwuliterowy skrót nazwy działu firmy, pisany wielkimi literami. 

Funkcja ma zwracać wartość `Decimal` z medianą wynagrodzeń pięciu najlepiej zarabiających pracowników firmy w danym dziale.

UPDATE: działu szukamy w kolumnie `department`, a nie wyciągamy go z `id_number`. Zatem jeśli brakuje wartości pod `department`, to ignorujemy ten wiersz.

UPDATE 2: zadaniem tej funkcji nie jest radzenie sobie z duplikatami. Zatem nie usuwamy duplikatów. Jeśli wiersz powtórzony, to traktujemy je jako dwa różne wiersze.

Uwagi: 
Dane walutowe w pliku (kolumna monthly_salary) są do oczyszczenia. Niestety będą miały dodatkowe “brudy” względem tych
pokazanych na zajęciach. Brudy te trzeba zaleźć i usunąć. Będą również puste wartości, należy je zignorować (nie mają wartości zero!).
W trakcie czyszczenia dane mają być zaokrąglane do dwóch miejsc po przecinku, tak jak na zajęciach. '''


# zadanie 4
import csv
from statistics import median

from decimal import Decimal

def get_csv_lines(filename):
    with open(filename, encoding='utf8') as csv_file:
      reader = csv.DictReader(csv_file, delimiter=',')
      for row in reader:
        yield row

def median_of_top_five(filename, department):
  STANOWISKO={
    'IT': 'IT',
    'ZA': 'ZARZĄD',
    'KS': 'KSIĘGOWOŚĆ',
    'KA': 'KADRY',
    'LO': 'LOGISTYKA',
    'SP': 'SPRZEDAŻ',
    'MA': 'MARKETING',
    'CZ': 'CZYSTOŚĆ',
    'OC': 'OCHRONA',
    }
    
  salaries=[]
  top_five=[]
  people=get_csv_lines(filename)
  for line in people:
    line['department'] = line['department'].strip()
    if STANOWISKO[department] == line['department']:
      salaries.append(clean_monetary_value(line['monthly_salary']))
  salaries.sort(reverse=True)
  for i in range(0,5,1):
    top_five.append(salaries[i])
  return median(top_five)
  
def clean_monetary_value(amount):
  if amount is None:
    return None
  amount= amount.strip()
  amount = amount.replace(' ', '')
  amount = amount.replace(',', '.')
  amount = amount.strip()
  amount = amount.replace(' ', '')
  amount = amount.replace(',', '.')
  amount = amount.replace('PLN', '')
  amount = amount.replace('ZŁ', '')
  amount = amount.replace('złotych', '')
  amount = amount.replace('Złotych', '')
  amount = amount.replace('pln', '')
  amount = amount.replace('Pln', '')
  amount = amount.replace('zł', '')
  amount = amount.replace('Zł', '')
  amount = amount.replace('ZŁOTYCH', '')
  return Decimal(amount).quantize(Decimal('0.01'))

assert median_of_top_five('personal_data_homework.csv', 'IT') == Decimal("9160.25")
assert median_of_top_five('personal_data_homework.csv', 'ZA') == Decimal("90640.00")
assert median_of_top_five('personal_data_homework.csv', 'LO') == Decimal("5104.84")