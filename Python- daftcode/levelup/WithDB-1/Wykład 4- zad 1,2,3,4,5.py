'''
3. Dodaj do endpointu /tracks możliwość dzielenia wyniku na strony:
 - obsługa parametru ?per_page=10 - ilość wyników na stronie,
 - obsługa parametru ?page=1 - strona z której pokażą się wyniki. Pierwsza strona powinna mieć numer 1
 - rozwiązanie powinno działać porawnie z wcześniej obsługiwanymi parametrami - lub ich brakiem

Wskazówka:
Proszę zapoznać się z słowami kluczowymi LIMIT i OFFSET
4. Dodaj do endpointu /tracks
 - możliwość dodawania nowych kawałków (POST JSON)
 - stworzenie nowego obiektu powinno objawić się zwróconym kodem 200
 - niestworzenie obiektu powinno objawić się zwróconym kodem 400 jeśli przesłane dane będą niekompletne, można pokusić się o dodatkowe pole errors w zwracanym JSONie, które mówiłoby co poszło nie tak.

Przykładowy POST:
{
    "album_id": 21,
    "media_type_id": 1,
    "genre_id": 3,
    "name": "Speeding",
    "composer": "Hooker",
    "milliseconds": 100,
    "bytes": 10000,
    "price": 1000
}

Przykładowa odpowiedź z sukcesem:
{
    "track_id": 10000,
    "album_id": 21,
    "media_type_id": 1,
    "genre_id": 3,
    "name": "Speeding",
    "composer": "Hooker",
    "milliseconds": 100,
    "bytes": 10000,
    "price": 1000
}
5. Dodaj nowy endpoint /genres
 - zwrócić JSON w którym klucze to nazwy gatunków, a wartości to ilość utworów przynależących do danego gatunku

Wskazówka:
 - Proszę zapoznać się ze słowem kluczowym GROUP BY oraz agregacją

Przykładowa odpowiedź:
{
    "Alternative": 40,
    "Alternative & Punk": 0
    "Blues": 0,
    ...,
    "TV Shows": 0,
    "World": 0
}'''


from flask import Flask, request, g, redirect, jsonify
import sqlite3
import json


DATABASE = 'chinook.db'


app = Flask(__name__)

def get_db():
  db = getattr(g, '_database', None)
  if db is None:
    db = g._database = sqlite3.connect(DATABASE)
  return db

@app.teardown_appcontext
def close_connection(exception):
  db = getattr(g, '_database', None)
  if db is not None:
    db.close()



@app.route('/')
def hi():
    return 'hi'
 
@app.route('/tracks', methods = ['GET']) 
def tracks():
  limit = 999999 #To jest bardzo zle, zmien tutaj <----------------!
  offset = 0
  artist = request.args.get('artist')
  offsett = request.args.get('page')
  limitt = request.args.get('per_page')
  if(type(offsett) == str):
    offset = int(offsett)-1
  if(type(limitt) == str):
    limit = int(limitt)
  db = get_db()
  cursor = db.cursor()
  if(type(artist) != str):
    data = cursor.execute('SELECT name FROM tracks ORDER BY name COLLATE NOCASE LIMIT ? OFFSET ?',(limit, offset)).fetchall()
  else:
    data = cursor.execute('SELECT T.Name FROM [tracks] T JOIN albums AL ON T.AlbumId = AL.AlbumId JOIN artists AR ON AR.ArtistId = AL.ArtistId WHERE AR.name = ? ORDER BY T.Name COLLATE NOCASE LIMIT ? OFFSET ?',(artist, limit, offset*limit)).fetchall()
  cursor.close()
  lista = []
  for el in data:
    lista.append(el[0])
  
  return jsonify(lista)

@app.route('/genres',methods=['GET', 'POST'])
def genres():
  db = get_db()
  cursor = db.cursor()
  data = cursor.execute('SELECT Name FROM genres ORDER BY Name COLLATE NOCASE;',).fetchall()
  data2 = cursor.execute('SELECT COUNT(T.TrackId) FROM [tracks] T JOIN genres G ON T.GenreId = G.GenreId GROUP BY G.Name COLLATE NOCASE ;').fetchall()
  myList2 = []
  for el in data2:
    myList2.append(el[0])
  cursor.close()
  l = 0
  myList = {}
  for el in data:
    myList[el[0]] = myList2[l]
    l = l+1
  return jsonify(myList)

if __name__ == '__main__':
    app.run(debug=False)