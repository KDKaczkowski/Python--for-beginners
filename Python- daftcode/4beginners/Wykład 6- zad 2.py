'''ZADANIE 2: walidacja wartości id_number 
Napisz funkcję validate_id_number, która przyjmuje id_number (str) oraz zwraca wartość typu bool:
True, jeśli id_number jest zgodny ze specyfikacją opisaną w zadaniu 1
False, jeśli nie jest zgodny

Uwagi: 
Funkcja ma sprawdzać wyłącznie poprawność przekazanej wartości, nie ma robić nic więcej (jak na przykład sprawdzanie unikalności).
Funkcja ma być przygotowana, by poprawnie walidować wszystkie wartości id_number z pliku personal_data_homework.csv.
Dodatkowo ma sobie radzić z wartościami zepsutymi na wiele innych sposobów, w tym takich, które nie nadają się do oczyszczenia (np. z brakującymi danymi).
'''


# zadanie 2


def validate_id_number(id_number):
  STRINGS_REPRESENTING_DEPARTMENT = {'ZA', 'IT', 'KS', 'KA', 'LO', 'SP', 'MA', 'CZ', 'OC'}
  if id_number is None:
    return False
  
  for word in id_number:
    if word =='-' or word =='.':
      return False
  
  if len(id_number)!=14:
    return False
  department, number, year=id_number.split('/')
  
  if department in STRINGS_REPRESENTING_DEPARTMENT:
    pass
  else:
    return False
  
  if len(number)!=6 or number.isdigit()==False:
    return False
    
  if len(year)!=4 or int(year)<1900 or int(year)>2018 or year.isdigit()==False:
    return False
  
  return True

  


assert validate_id_number("SP/987543/2000") is True
assert validate_id_number("ZA/434503/2005") is True
assert validate_id_number("ZA/434503/2005 ") is False
assert validate_id_number("ble ble") is False
assert validate_id_number("ZA/43450/2005") is False
assert validate_id_number("XX/987654/2011") is False
assert validate_id_number("IT/34343/1800") is False