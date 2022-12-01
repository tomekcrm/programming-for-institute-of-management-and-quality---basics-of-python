# Lekcja 1 - stringi

Ogólnie możemy zdefiniować, że jest to "ciąg znaków".
Jeżeli zapiszecie jakąś liczbę jako string, nie będzie ona traktowana jako liczba i nie doda się do innej w standardowy sposób.
Przy próbie takiego działania, program zwróci wam błąd
```python
TypeError: can only concatenate str (not "int") to str
```

## Komentowanie 

W przyszłej pracy przyda się opcja komentowania kodu, jest to opcja na opisanie co w danym miejscu należy zrobić, lub co zostało zrobione i jak działa. Pomaga w zrozumieniu zagadnienia oraz ewentualnie przy dalszych pracach nad kodem w przyszłości, aby skomentować kod, wystarczy użyć #, ewentualnie w przypadku, gdy chcemy dać dłuższe instrukcje lub komentarz możemy zacząć go """ oraz zakończyć w ten sam sposób """

Przykład:

```python
# definiujemy zmienną X o wartości 10
x = 10
print(type(x))

#następnie zmieniamy ją na stringa
x = str(x)

print(type(x)) #komentarz możemy zamieścić również zaraz obok kodu

"""
Tutaj damy dłuższy komentarz 
na jakiś inny temat
"""



```

Komentarze nie są wykonywanie przez program, mają służyć wyłącznie jako instrukcje lub wskazówki

## f-stringi
F-stringi jest to jedna z metodow na połączenie ciągu znaków oraz zawartości zmiennych.
Dzięki czemu możemy na przykład wydrykować powitanie dla każdego uczestnika z listy, mając ich listę imion, lub mając zapisaną w zmiennej temperaturę (w przykładzie zapisaną na stałą, jednak w rzeczywistości pochodizłaby z czujnika temperatury) wyświetlić ją w ładny sposób wraz z opisem miejsca gdzie się znaduje.
Poprawny format takiego f-stringa to 
```python
nazwa_zmiennej_1 = "coś tam"
nazwa_zmiennej_2 = "coś tam ale drugie"
fstring = f"TREŚĆ {nazwa_zmiennej_1} {nazwa_zmiennej_2}" 

#gdy chcemy to wyprintować to należy umieścić wewnątrz print()

print(f"jakaś tam treść która coś wyjaśnia lub nadaje kontekstu {nazwa_zmiennej_1} oraz tutaj {nazwa_zmiennej_2} i można zakończyć ")
```

Przykłady 1: 

```python
uczestnicy = ['Damian', 'Michał', 'Aneta', 'Stefan'] # lista uczestników spotkania

for uczestnik in uczestnicy:  #tworzym pętlę iterującą przez każdego uczestnika na liście w zmiennej uczestnicy
	print(f"Witaj {uczestnik}") #drukujemy słowo witaj oraz zawartość zmiennej uczestnik
	
```

Przykłady 2: 

```python
temp_salon = 16    	#wartość temperatury w salonie
temp_pokoj_1 = 2	#wartość temperatury w pokoju dziecka

print(f" Temperatur w salonie wynosi {temp_salon} stopni, w pokoju dziecka {temp_pokoj_1} stopni ")

#możemy również stworzyć funkcję, która poinformuje gdy temperatura w pokoju dziecka będzie większa lub mniejsza niż X

if temp_pokoj_1 < 0:
    print(f"Dziecko zamarznie, w jego pokoju jest {temp_pokoj_1} stopni")
    
elif temp_pokoj_1 > 22:
    print(f"Dziecko zaraz się usmaży! W jego pokoju jest {temp_pokoj_1} stopni")
	
```


## Definiowanie 

Stringi możemy definiować na kilka sposobów, "otaczając" je cudzysłowem. Najważniejsze jest, aby na początku i na końcu był taki sam, oraz należy zwrócić szczególną uwagę, aby wewnątrz stringa nie było słów wziętych w taki sam typ cudzysłowie. 

Ponadto ciąg znaków musi być w jednej linii. 

Wyjątkiem jest przykład 4 (potrójny cudzysłów)


Przykłady: 

```python
string = 'Hello world'
print(string)

string = "Hello world"
print(string)

string = '''Hello world'''
print(string)
```
Użycie potrójnego cudzysłowu daje możliwość zapisania dłuższego tekstu w kilku liniach tekstu, robi się to w następujący sposób:

```python
long_string = """jest to jakiś dłuższy tekst, 
		może być zapisany w wielu liniach, 
		dzięku zastosowaniu potrójnego cudzysłowia"""
print(long_string)
```


## Wycinanie fragmentów stringów:

Wycinanie/dostęp do konkretnego fragmentu
Python daje nam możliwość "wycinania" części stringa dzięki wpisaniu [] zaraz po nazwie zmiennej.4


#### Jak python liczy miejsce w sekwencji (pamiętać należy, że od 0 - nie od 1)
![This is an image](https://developers.google.com/static/edu/python/images/hello.png)


Przykłady:


```python
string = "Uniwerek"
print(str)

#Gdy chcemy uzyskać tylko pierwszą literę, musimy pamiętać, że liczenie zaczynamy od 0, nie od 1:
print( string[0])

#Możemy również liczyć "w tył", więc aby uzyskać ostatnią wystarczy wpisać:
print(string[-1])

#Aby uzyskać tekst od 2 do 5 litery, musimy wpisać:
print(string[1:5])
```
Jeżeli będziemy chceli uzyskać dostęp do nieistniejącego "zasięgu" stringa, program zwróci nam błąd:
```python 
IndexError: string index out of range
```





## Operacje na stringach
Stringi możemy do siebie dodawać, oraz zwielokrotnić ich ilość. Jednak wracając do początku tej lekcji, pamiętać musimy, że dodając cyfrę będącą stringiem np ```1``` do ```1```, nie otrzymamy ```2```, a ```11```. Program zestawi na po prostu te dwie cyfry ze sobą.


```python 
#Przykład z góry
#jeżeli cyfry są zapisane do zmiennych bez cudzysłowu, są najczęściej traktowane jako int() czyli cyfry - możemy to łatwo sprawdzić wpisując nazwę zmiennej do funkcji type() - przykład niżej

cyfra_pierwsza = 1
cyfra_druga = 2 
print(type(cyfra_pierwsza))
print(cyfra_pierwsza + cyfra_druga )

#jednak jeżeli cyfry weźmiemy w cudzysłów, będą traktowane jako stringi, czyli ciągi znaków

cyfra_pierwsza = "1"
cyfra_druga = "2" 
print(type(cyfra_pierwsza))
print(cyfra_pierwsza + cyfra_druga )
#wynik również będzie stringiem 


```

```python 
#Przykład drugi
st1 = 'Hello'
st2 ='Uniwersity!'

print (f"dodawanie dwóch słów do siebie {st1 + st2}")

print(f"możemy również pomnożyć słowo wielokrotnie {st1 * 3}")
``` 
## Iterowanie przez stringa


Przez stringa możemy również iterować, czyli sprawdzić kawałek po kawałku. W podstawowej formie, program sprawdza każdą literę.

Przykład:
```python 
liczba_liter_e = 0

for letter in 'Hello Uniwersity':
    if(letter == 'e'):
        liczba_liter_e += 1

print(f"Liczba liter 'e' wynosi {liczba_liter_e }")
```

Ponadto możecie sprawdzić, czy dany ciąg znaków zawiera w sobie konkretny element:

```python 
str = "cała masa różnych słów, dobrych jak i tych nienajlepszych"
print("dobry" in str)
print("dobry" not in str)

len() jako przykład funkcji wbudowanej
```

## Funkcje wbudowane w stringach
Stringi posiadają całą masę tak zwanych "funkcji zbudowanych"
Aby ich użyć, należy nazwię zmiennej w której został umieszony string (lub sam string) podać ją w warunku (nawiasie)
Za przykład niech nam posłuży funkcja len() która podaje długość stringa.
```python 
str = 'Hello Uniwersity'
print(len(str))

```
## Co gdy wewnątrz stringa mamy cudzysłów?

W przypadku gdy w stringu trafimy na cudzysłów, możemy od niego "uciec" używając \

#### BŁĄD SPOWODOWANY CUDZYSŁOWIEM WEWNĄTRZ STRINGA
```python
>>> print("He said, "What's there?"")
...
SyntaxError: invalid syntax
>>> print('He said, "What's there?"')
...
SyntaxError: invalid syntax

```

#### METODY NA UCIECZKĘ:


Metody zależnie od tego, jakim cudzysłowiem "okrążony" jest string - uciec powinniśmy w takim samym.
```python
print('He said, "What\'s there?"')
print("He said, \"What's there?\"")
```

## Stringowie metody



Metody upraszają nam pracę ze stringami i pomagają w serializacji danych.
Na przykład, aby cały tekst był wyłącznie małymi literami, możemy użyć metody .lower()
metoda .upper() natomiast spowoduje, że cały tekst będzie pisany wielkimi literami.

```python
print("ProGramoWanieNaUpH".lower())
#wynikiem będzie -> 'programowanienauph
print(("ProGramoWanieNaUpH".upper())
#wynikiem będzie -> 'PROGRAMOWANIENAUPH' 
```

Kolejną przydatną metodą, jest .split() który dzieli nam stringa na pojedyncze słowa. 
```python
lista_slow = "To całe zdanie zostanie podzielona na pojedyncze słowa i wstawione jako lista słów. Jeżeli chcemy policzyć ile razy użyliśmy słowa, słowo to zawsze można użyć kodu który zaraz w krótkich słowach wyjaśnię".split()
print(lista_slow)
```

Przez taką listę możemy również iterować, jak w przypadku liter podanym wyżej

```python
lista_slow = "To całe zdanie zostanie podzielona na pojedyncze słowa i wstawione jako lista słów. Jeżeli chcemy policzyć ile razy użyliśmy słowa, słowo to zawsze można użyć kodu który zaraz w krótkich słowach wyjaśnię".split()
for slowo in lista_slow:
	print(slowo)
```
Dodając tylko metodę liczenia którą również poznaliśmy wyżej, możemy w łatwy sposób policzyć ilość słów które występują w ciągu.

```python
ile_razy_wystapilo_slowo = 0
lista_slow = "To całe zdanie zostanie podzielona na pojedyncze słowa i wstawione jako lista słów . Jeżeli chcemy policzyć ile razy użyliśmy słowa, słowo to zawsze można użyć kodu który zaraz w krótkich słowach wyjaśnię".split()
for slowo in lista_slow:
	if slowo == "słów":
		ile_razy_wystapilo_slowo += 1
print(f"słowo 'słów' wystąpiło {ile_razy_wystapilo_slowo } razy")
```

Aby znaleźć miejsce w którym dany ciąg lub słowo (pierwszy raz) się znajduje możne użyć funkcji .find()

```python
lista_slow = "To całe zdanie zostanie podzielona na pojedyncze słowa i wstawione jako lista słów . Jeżeli chcemy policzyć ile razy użyliśmy słowa, słowo to zawsze można użyć kodu który zaraz w krótkich słowach wyjaśnię"
wystapilo = lista_slow.find('słów')
print(f"słowo 'słów' wystąpiło na {wystapilo} miejscu.")
```

### W podstawach byłoby tego na tyle. 


# Zadanie 1
```python
""" W zbiorze podanym niżej, sprawdź ile razy występuje litera "a". 
podpowiedź -> użyj funkcji .count() podająć w nawiazie to, czego szukasz
"""


string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin elementum at est vitae cursus. Donec accumsan pulvinar mi eu congue. Maecenas porta sit amet purus ut faucibus. Cras vitae purus auctor, cursus est sed, fermentum felis. Duis tempor leo eu ex bibendum, consectetur facilisis justo ullamcorper. Nam sit amet lorem et nunc dapibus facilisis id quis libero. Fusce pulvinar ex nisi, aliquet sodales lorem viverra ac. Sed augue nibh, porttitor sit amet gravida a, hendrerit sed nulla. In pellentesque nibh at elit volutpat semper. Nunc porta libero luctus ligula sodales aliquam. Vestibulum pulvinar quam pulvinar, bibendum turpis sit amet, malesuada nibh. Aenean nec massa sit amet diam ullamcorper bibendum. Proin hendrerit posuere nulla, non ultrices neque tincidunt sit amet Curabitur eu nisi in ipsum pharetra sodales non eu ex. Fusce varius ante ac sem volutpat, sed maximus eros dignissim. Maecenas vitae egestas odio, vitae tincidunt neque. Ut volutpat lorem non quam scelerisque tempus ac eget lacus. Morbi maximus augue id magna dignissim lacinia. Maecenas aliquam et ipsum at tempus. Praesent maximus urna sit amet nunc ornare pulvinar. Vivamus rhoncus nulla in venenatis sodales. Maecenas convallis lacinia fermentum. Vivamus dapibus libero et eros condimentum interdum. Curabitur quam velit, ultrices nec faucibus sit amet, molestie vel neque. Mauris accumsan metus ex, nec pretium sapien pretium eu. Aenean feugiat sollicitudin ex, cursus sollicitudin ligula faucibus ut. Aenean ac ipsum tincidunt, auctor magna non, convallis nunc. Vestibulum condimentum efficitur ullamcorper. Maecenas non finibus augue, condimentum efficitur lacus. Mauris in augue vel nisi euismod tempus quis non purus. Donec pulvinar, lacus in hendrerit hendrerit, nibh metus lacinia leo, quis fermentum augue magna vitae nisl. Nullam ac tempor nibh, ac accumsan massa. Aenean interdum non felis eget pellentesque. Sed a lectus tincidunt, semper magna pretium, consectetur urna. Maecenas elementum diam et urna gravida varius. Nullam scelerisque ligula ante, at ullamcorper dui efficitur eu. Etiam vehicula est fringilla, bibendum purus ac, ultrices nibh. Nam vel ornare augue, id venenatis erat. Nullam dolor odio, molestie eu quam sed, pharetra rutrum mauris. Pellentesque odio nisi, tincidunt eget tempor ut, tempor eu erat. Aenean ullamcorper tortor orci, a rutrum ante accumsan sit amet. Nulla non justo sit amet risus consequat vestibulum.In non mollis tortor. Curabitur in tortor elit. Nullam dolor elit, laoreet eu velit interdum, malesuada accumsan massa. Etiam sollicitudin enim quis mi porttitor dapibus ac quis nisi. Quisque sed nulla velit. Fusce nunc eros, pharetra non mauris vitae, vulputate tristique nunc. Nullam eget metus purus. Ut pellentesque scelerisque dolor, ut ultricies dui aliquam et."
```
# Zadanie 2
```python
"""
Stwórz program, który w podanym stringu sprawdzi ile razy występuje słowo "non".

Podpowiedzi:
krok 1 - stwórz zmienną która przechowuje liczbę z ilością wystąpień, z wiadomych względów na początku ma wynosić 0
krok 2 - stwórz zmienną i zapisz w niej listę z podzielonymi słowami (funkcji .split() )
krok 3 - stwórz iterację, w której każde słowo będzie sprawdzane i porównywane do słowa "non"
krok 4 - jeżeli słowo "non" się zgadza, zwięk licznik wystąpień o 1
krok 5 - wydrukuj ilość wystąpień -- w wersji pro, możesz użyć f-stringa w formie print(f"Słowo 'non' wystąpiło {} razy")

"""




string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin elementum at est vitae cursus. Donec accumsan pulvinar mi eu congue. Maecenas porta sit amet purus ut faucibus. Cras vitae purus auctor, cursus est sed, fermentum felis. Duis tempor leo eu ex bibendum, consectetur facilisis justo ullamcorper. Nam sit amet lorem et nunc dapibus facilisis id quis libero. Fusce pulvinar ex nisi, aliquet sodales lorem viverra ac. Sed augue nibh, porttitor sit amet gravida a, hendrerit sed nulla. In pellentesque nibh at elit volutpat semper. Nunc porta libero luctus ligula sodales aliquam. Vestibulum pulvinar quam pulvinar, bibendum turpis sit amet, malesuada nibh. Aenean nec massa sit amet diam ullamcorper bibendum. Proin hendrerit posuere nulla, non ultrices neque tincidunt sit amet Curabitur eu nisi in ipsum pharetra sodales non eu ex. Fusce varius ante ac sem volutpat, sed maximus eros dignissim. Maecenas vitae egestas odio, vitae tincidunt neque. Ut volutpat lorem non quam scelerisque tempus ac eget lacus. Morbi maximus augue id magna dignissim lacinia. Maecenas aliquam et ipsum at tempus. Praesent maximus urna sit amet nunc ornare pulvinar. Vivamus rhoncus nulla in venenatis sodales. Maecenas convallis lacinia fermentum. Vivamus dapibus libero et eros condimentum interdum. Curabitur quam velit, ultrices nec faucibus sit amet, molestie vel neque. Mauris accumsan metus ex, nec pretium sapien pretium eu. Aenean feugiat sollicitudin ex, cursus sollicitudin ligula faucibus ut. Aenean ac ipsum tincidunt, auctor magna non, convallis nunc. Vestibulum condimentum efficitur ullamcorper. Maecenas non finibus augue, condimentum efficitur lacus. Mauris in augue vel nisi euismod tempus quis non purus. Donec pulvinar, lacus in hendrerit hendrerit, nibh metus lacinia leo, quis fermentum augue magna vitae nisl. Nullam ac tempor nibh, ac accumsan massa. Aenean interdum non felis eget pellentesque. Sed a lectus tincidunt, semper magna pretium, consectetur urna. Maecenas elementum diam et urna gravida varius. Nullam scelerisque ligula ante, at ullamcorper dui efficitur eu. Etiam vehicula est fringilla, bibendum purus ac, ultrices nibh. Nam vel ornare augue, id venenatis erat. Nullam dolor odio, molestie eu quam sed, pharetra rutrum mauris. Pellentesque odio nisi, tincidunt eget tempor ut, tempor eu erat. Aenean ullamcorper tortor orci, a rutrum ante accumsan sit amet. Nulla non justo sit amet risus consequat vestibulum.In non mollis tortor. Curabitur in tortor elit. Nullam dolor elit, laoreet eu velit interdum, malesuada accumsan massa. Etiam sollicitudin enim quis mi porttitor dapibus ac quis nisi. Quisque sed nulla velit. Fusce nunc eros, pharetra non mauris vitae, vulputate tristique nunc. Nullam eget metus purus. Ut pellentesque scelerisque dolor, ut ultricies dui aliquam et."
```

# Zadanie 3
```python
"""
Stwórz program, który w ciągu znaków będącej wierszem prosi o podanie słowa input(), 
a następnie sprawdza czy słowo występuje w ciągu i ewentualnie ile razy się w nim znajduje.
"""
```


[Przejdź do następnej lekcji](https://github.com/tomekcrm/python-basics-for-WS-students/blob/main/lekcja2.md)
