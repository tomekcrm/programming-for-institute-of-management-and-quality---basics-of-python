# Listy 

### Czym są listy
Lista pomaga nam w ustrykturyzowaniu oraz opanowaniu naszych danych.
Listy zapisujemy w kwadratowych nawiasach [], wewnątrz zapisująć jej elementy oddzielająć je przecinkiem. Na przykład
```python
studenci = ["Michał", "Andrzej", "Agata", "Stefan", "Monika"]
```

### Dodawanie elementów do listy

W celu dodania kolejnego elementu listy na jej koniec używamy metody .append()
```python
#chcemy dodać Anię do listy studentów
studenci = ["Michał", "Andrzej", "Agata", "Stefan", "Monika"]
print(studenci)
studenci.append("Ania")
print(studenci)
```
### Indeksy w liście

Każdy element na liście, podobnie jak to miało miejsce w stringach, ma swój numer nazywany indeksem.  Aby pozyskać elementu listy należy podać nazwę listy, a następnie w kwadratowym nawiasie podać indeks (przykład niżej)

W celu znalezienia Agaty na naszej liście, powinniśmy napisać:
```python
#chcemy dodać Anię do listy studentów
studenci = ["Michał", "Andrzej", "Agata", "Stefan", "Monika"]
studenci[2]

print(studenci[2])

```

Znajmość indeksów pozwala nam edytować ich zawartość oraz usuwać konkretne elementy listy. 

### Zmiana zawartości
W celu zmiany zawartości / elementu należy podać jego indeks, tak jak to miało miejsce w princie wyżej i nadpisać jak w przypadku normalnych zmiennych.

Przykład:
Agata indendyfikuje się jako mężczyzna i chce by nazywać go teraz Adam

```python
studenci = ["Michał", "Andrzej", "Agata", "Stefan", "Monika"]
print(studenci) # najpierw indeks pokazuje Agatę

studenci[2] = "Adam"
print(studenci) # po zmianie program pokazuje już nadpisane imię
```
### Usuwanie zawartości 
Aby usunąć kogoś z listy za zbyt dużą nieobecność, wystarczy użyć metody .pop() z odpowiednym indeksem w nawiasie

Przykład, Adam poprzez komplikacje po operacji opuścił zbyt dużo zajęć i musi zostać usunięty z listy

```python
studenci = ["Michał", "Andrzej", "Adam", "Stefan", "Monika"]
print(studenci) # najpierw indeks pokazuje pełną listę

studenci.pop(2) 
print(studenci) # po zmianie program pokazuje jużlistę bez Adama
```
Zwrócić należy natomiast uwagę, że jeżeli użyjemy metody .pop() bez podania indeksu, usunięty zostanie ostatni element listy.

### Przeszukiwanie listy

W celu sprawdzenia czy dany element znajduje się na liście, należy użyć funkcji "in"
Należy pamiętać jednak, że nie pokaże nam ona nic innego jak True lub False zależnie czy element znajduje się na liście lub nie.

Przykład:
```python
#Adam nakłamał rodzicom, że jednak chodzi dalej do szkoły i uczęszcza regularnie na zajęcia, chcemy więc sprawdzić czy jest na liści
studenci = ["Michał", "Andrzej",  "Stefan", "Monika"]
czy_adam_jest_na_liscie = "Adam" in studenci
print(czy_adam_jest_na_liscie)
```

Jeżeli chcemy jednak poznać indeks danego elementu użyć możemy .index() podając w nawiasie szukany element

Przykład:
```python
#Szukamy studenta o imieniu Monika

studenci = ["Michał", "Andrzej",  "Stefan", "Monika"]
index_moniki = studenci.index("Monika")

print(index_moniki)

```

Prosta funkcja pozwala nam również policzyć ile razy dany element występuje na liście, robimy to za pomocą .count() gdzie standardowo podajemy w nawiasie czego szukamy

```python
#Szukamy studenta o imieniu Monika

studenci = ["Michał", "Andrzej",  "Stefan", "Monika"]
ile_razy_monika = studenci.count("Monika")

print(ile_razy_monika)

```
### Zagnieżdzanie list

Listy można zagnieżdzać, czyli umieszczać jedną listę w drugiej. Rodzi to duży potencjał do organizacji danych.

Za przykład możemy podać studentów, ale niech wszystko kryje się pod numerem albumu poprzedzonym literą "s" jako "student".
Sama liczba nie może być zmienną!!!

```python
#Każdy student w przykładzie ma imię, nazwisko, miejsce zamieszkania - ważne - dane muszą być podane dokładnie w takiej kolejności

s18112 = ["Michał", "Zalewski", "Siedlce"]
s21542 = ["Andrzej", "Staszewski", "Mińsk Mazowiecki"]
s81123 = ["Stefan", "Kolanowski", "Siedlce"]
s91221 = ["Monika", "Kaszewska", "Siedlce"]

#każdy numer albumu zawiera listę z danymi studenta, teraz należy utworzyć listę numerów albumów !!! WAŻNE !!! Pamiętaj aby nie podawać numeru albumu w cudzysłowie, gdyż wtedy program uzna go za string'a a nie listę

studenci = [s18112, s21542, s81123, s91221]

print(studenci)

#Przez każdy element listy możemy iterować, spróbujmy więc wyświetlić studentów 
for student in studenci:
    print (student)

#Teraz sprawdzimy czy dany student to Stefan - używając "in" wewnątrz pętli
for student in studenci:
    print ("Stefan" in student)

```
Właściwie na tym etapie granice stawia już czysta fantazja.
Możemy więc przejść do zadań.

# Zadania
### Zadanie 1 - studenci
```python
s18112 = ["Andrzej", "Zalewski", "Siedlce"]
s21542 = ["Grażyna", "Staszewski", "Mińsk Mazowiecki"]
s81123 = ["Stefan", "Kolanowski", "Łuków"]
s91221 = ["Monika", "Kaszewska", "Siedlce"]

#TODO: Utwórz listę studentów z podanych numerów indeksów
#TODO: Stefan zmienił miejsce zamieszkania na Siedlce - nanieś zmiany w kodzie, nie w samej zmiennej
#TODO: W obu programach niżej, system ma pytań użytkownika, czy chce wyszukać lub dodać następną osobę
#TODO: Utwórz program, który analogicznie tworzy i dodaje studentów do listy - użyj input()
#TODO: Utwórz program, który w podanej liście studentów wyświetla dane studenta po podaniu mu numeru albumu

```
### Zadanie 2 - Tiara przydziału
```python
#Utwórz program, który pyta użytkownika o imię, następnie losuje dla niego, do którego domu zostaje przypisany. Całość można okrasić odpowiednimi komentarzami tiary.

import random   #ta biblioteka pozowli nam losować element listy random.choice(nazwa_listy)
import time         #ta biblioteka ma funkcję time.sleep() gdzie program na podaną ilość sekund się zatrzymuje

#poniżej znajduje się lista domów, w każdej z list indeks 0 wskazuje nazwę domu.
Gryffindor = ["Gryffindor"]
Slytherin = ["Slytherin"]
Ravenclaw = ["Ravenclaw"]
Hufflepuff = ["Hufflepuff"]

#TODO: Stwóz listę zawierającą powyższe domy
#TODO: Zapytaj przybysza jak ma na imię i zapisz imię do zmiennej
#TODO: Wylosuj przybyszowi dom z listy - 
#TODO: Dodaj przybysza do konkrentego domu
#TODO: Napisz kto jest w domu razem z nim
#TODO: Zapytaj czy jest kolejna osoba w kolejce - jeśli tak to wróć do pytania o imię, w innym przypadku napisz wszystkie domy i kto w nich jest


```
