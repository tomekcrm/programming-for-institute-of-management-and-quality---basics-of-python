# Słowniki

### Czym są i jak działają słowniki
Już z samej nazwy możemy wywnioskować, że słownik zawiera jakieś określenie oraz jego wytłumaczenie. 
Nieinaczej jest w pythonie - słownik zawiera zestaw klucza i wartości

Słowniki tworzymy za pomocą klamerek, klucz od wartości natomiast rozdzielamy dwókropkiem.
```python3
slownik = {'klucz1': 'wartosc1', 'klucz2': 'wartosc2'}
```
Do słowników zapisywać możemy różne typy danych, tak jak we wskazanym przykładzie.

```python3
slownik = {'klucz1': 'tekst', 'klucz2': 123, 'klucz3': ['1elementlisty', '2elementlisty', '3elementlisty']}
```
W celu odczytania konkretnej wartości przypisanej do klucza, należy do użytej zmiennej zawierającej słownik dopisać ["nazwa_klucza"], w naszym przypadku, aby odczytać wartość klucza2, użyjemy

```python3
slownik['klucz2']
```
program zwróci nam wtedy 

```python3
123
```
### Co możemy z nimi zrobić?
W przykładach będziemy używali słownika z poprzedniego rozdziału
```python3
slownik = {'klucz1': 'tekst', 'klucz2': 123, 'klucz3': ['1elementlisty', '2elementlisty', '3elementlisty']}
```
####dodawanie do słownika
W celu dodania nowego zestawu klucz : wartość , należy do zmiennej zawierającej słownik dopisać ["nowy_klucz"] = "nasza nowa wartość"

```python3
slownik['klucz4'] = "jakakolwiek potrzebna nam wartość" 
```
po dodaniu, nasz słownik powinien wyglądać tak:

```python3
slownik = {'klucz1': 'tekst', 'klucz2': 123, 'klucz3': ['1elementlisty', '2elementlisty', '3elementlisty'], 'klucz4' : "jakakolwiek potrzebna nam wartość"}
```
#### Modyfikowanie wartości słownika

Aby zmodyfikować wartość klucza, należy wywołać go jak poprzednio i ustawić nową, wartość !WAŻNE! stara wartość zostanie utracona

Chcąc zaktualizować wartość klucz4 i nadać mu nową o treści "nowa wartość klucza 4"

```python3
slownik['klucz4'] = "nowa wartość klucza 4" 

slownik = {'klucz1': 'tekst', 'klucz2': 123, 'klucz3': ['1elementlisty', '2elementlisty', '3elementlisty'], 'klucz4' : "nowa wartość klucza 4" }
```
Okej, wartość klucz4 nie jest nam już potrzebna, jak możemy ją usunąć?
Możemy zrobić to za pomocą 'del' jak w przykładzie poniżej:

```python3
del slownik['klucz4']
```
aby usunąć wszystkie elementy słownika i całkowicie go wyczyścić z kluczy i wartości, możemy użyć metody clear() w podany poniżej sposób:

```python3
slownik.clear()
```

#### Wbudowane metody słownika
Słownika posiada liczne metody, które pomagają nam z nim pracować.
Użyjemy znanego już wam słownika.

```python3
slownik = {'klucz1': 'tekst', 'klucz2': 123, 'klucz3': ['1elementlisty', '2elementlisty', '3elementlisty'], 'klucz4' : "wartość klucza 4" }
```
W celu sprawdzenia liczby kluczy, należy użyć poznanego już len() w sposób zaprezentowany poniżej:

```python3
len(slownik)
```
Słowniki mogą mieć złożoną strukturę, w celu wyświelenia par  klucz : wartość należy użyć  *.items() *
Jeżeli zależy nam wyłącznie na kluczach, używamy* .keys()*
Jeżeli natomiast potrzebujemy wyłącznie wartości należy użyć *.values()*

Wszystkie te metody są przydatne chociażby podczas iteracji przez słownik.
Użycie przedstawionych metod prezentuję poniżej.

```python3
slownik.items()
slownik.keys.()
slownik.values()
```

Aby przeiterować "zestawy" w słowniku i dla każdego zestawu zwrócić klucz oraz wartość, należy zrobić to w następujący sposób:

```python3
slownik = {'klucz1': 'tekst', 'klucz2': 123, 'klucz3': ['1elementlisty', '2elementlisty', '3elementlisty'], 'klucz4' : "wartość klucza 4" }

for key, value in slownik.items():
	print(key)
	print(value)
	print("-----")
```

## Zadania
### Zadanie 1 

```python3
#Działamy na podanym niżej słowniku zawierającym jako klucz kierunki studiów i jako wartość, liczbę uczęszczających studentów

slownik = {"Zarządzanie": 133, "Administracja": 87, 'Bezpieczeństwo' : 142}

#ToDo: Trzech studentów dopisało się do kierunku Administracja oraz dwunastu do kierunku Bezpieczeństwo, nie zmieniająć pierwotnego słownika, zmień odpowiednie wartości

#ToDo: Na kierunku zarządzanie, ustawiamy wartości jako słownik z ilościami na konkretnych specjalnościach MŚP -> 33, Rachunkowość -> 45, Logistyka -> 55
```

### Zadanie 2

```python3
#Działamy na podanym niżej słowniku, zawiera on imiona dzieci oraz listę punktów za złe oraz dobre uczynki.

slownik = {"Michałek": [12,-5,2,-17,2,50,32,15,2,-6,8,-12] , "Anżelika": [5,25,-10,7,2,12,-8,15,20,12,52] ,'Grażynka' : [15,-10,-7,10,-3,5,-15,8,-10,3,-15,5,-15], 'Stefan' : [14,-6,1,-5,12,25,17,12,26,-60,25,5,-10,32,22,-5], 'Czesio' : [25,-15,-5,10,-2,5,-15,8,-10,3,-20,5,-15]}

#ToDo: Napisz kod, który wszystkie punkty dla każdego dziecka zsumuje, aby następnie wydać werdykt, jeżeli dziecko zebrało więcej jak 10 punkty - dostaje prezent, jeżeli mniej - będzie węgiel

#ToDo: Czesio napisał bardzo ładny list przepraszająć za swoje złe uczynki, zhackuj kod i zapewnij czesiowi taką ilość punktów, aby dostał prezent od Mikołaja !!!Nie ruszamy pierwotnego słownika!!!
```


    
