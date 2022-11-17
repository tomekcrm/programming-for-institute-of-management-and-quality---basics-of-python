
# Lekcja 0

Podstawowe założenia języka - głownie forma wykładowa z elementami mikro ćwiczeń.


## Zen of python

Język który omawiamy to python w wersji 3

Język python oparty został o szereg założeń już na etapie tworzenia, nazywa się to ZEN of Python,


```python
Piękne jest lepsze niż brzydkie.
Wyrażone wprost jest lepsze niż domniemane.
Proste jest lepsze niż złożone.
Złożone jest lepsze niż skomplikowane.
Płaskie jest lepsze niż wielopoziomowe.
Rzadkie jest lepsze niż gęste.
Czytelność się liczy.
Sytuacje wyjątkowe nie są na tyle wyjątkowe, aby łamać reguły.
Choć praktyczność przeważa nad konsekwencją.
Błędy zawsze powinny być sygnalizowane.
Chyba że zostaną celowo ukryte.
W razie niejasności powstrzymaj pokusę zgadywania.
Powinien być jeden -- i najlepiej tylko jeden -- oczywisty sposób na zrobienie danej rzeczy.
Choć ten sposób może nie być oczywisty jeśli nie jest się Holendrem.
Teraz jest lepsze niż nigdy.
Chociaż nigdy jest często lepsze niż natychmiast.
Jeśli rozwiązanie jest trudno wyjaśnić, to jest ono złym pomysłem.
Jeśli rozwiązanie jest łatwo wyjaśnić, to może ono być dobrym pomysłem.
Przestrzenie nazw to jeden z niesamowicie genialnych pomysłów -- miejmy ich więcej!
```


## Ogólne założenia języka
Należy pamiętać, że nauka programowania, to nie nauka "na pamięć".

Podstawą jest znajomość pewnych konceptów oraz umiejętne ich stosowanie.

Zaczniemy więc od podstaw.

Python "czyta" wasz kod -od góry - do dołu - linijka po linijce zwracając uwagę na instrukcje jakie mu dajecie. 

Tak więc możecie kazać mu skończyć "czytanie" czy powtórzyć daną czynność określoną ilość razy.

Ponadto mając X rzeczy w "pudełku" o którym teraz porozmawiamy, możecie kazać mu "obejrzeć" je i przenalizować pod konkretnym kątem.

Niezwykle ważną rzeczą w tym języku są "wcięcia". Python jest "case-sensitive" i każde "wcięcie" czy tabulację uznaje za odrębny kawałek kodu. Ten system i jego sensowność omówimy w kolejnych etapach tej lekcji omawiając podstawowe pętle oraz funkcje.
## Python jako język obiektowy

Następną ważną koncepcją jest obiektowość języka. 

Object-oriented programming czyli programowanie obiektowe, jest programowaniem, które w sporym uproszczeniu zakłada, że każdy element kodu jest obiektem. 
Obiekty mogą zawierać kod lub nawet całe funkcje, czyli zestawy poleceń

Zaczniemy więc od zmiennych, czyli swoistego "pudełka" do którego możemy wkładać przeróżne rzeczy.
Aby łatwiej "namierzyć" pudełko należy nadać mu nazwę,może być właściwie dowolne, jednak pamiętać należy o odpowiednieć wielkości liter oraz tym, aby wskazywała ona odpowiednią zawartość "pudełka".
Bezsensu byłoby przecież nazwanie pudełka "płyty CD", gdy w środku znajdują się książki.

Tak samo należy unikać nazywania dwóch "pudełek" tak samo, gdyż możemy się pomylić (w pythonie, usuniemy stare pudło, by zastąpić je nowym [nadpiszemy]).

W przypadku, gdy chcemy nazwać zmienną kilkoma słowami, należy użyć podkreślania "_"

Więc, aby coś przypisać do zmiennej o określonej nazwie to wystarczy użyć składni:
```python
pudełko = zawartość
```

np.: 
```python
student = “Michał”
liczba = 2127
```

Gdzie teraz, każdorazowo wywołując `student`, program widzi jego zawartość `Michał`


## Przydatne nam polecenia

W celu lepszego pracowanie z kodem, poznajmy podstawowe polecenia.

- Przyjmujemy, że zmienna to dowolna zmienna jaką utworzyliśmy!

Aby:

- "wydrukować" (wyświetlić) coś do konsoli, należy użyć `print(zmienna)`
- przyjąć informację od użytkownika, należy użyć `input()`
- W celu wyprintowania treści, oraz zawartości zmiennej należy użyć tak zwanego f-stringu, gdzie zmienną umieszamy w `{zmienna}` - na przykład `print(f"moje imię to {imię}")`


## Zmienne (variables)

Aby zdefiniować zmienną (pudełko), należy nadać jej odpowiednią nazwę - wspominaliśmy o tym wyżej.

Podczas nadania nazwy, takie pudełku jest z założenia puste, możemy więc do niego coś wsadzić.

Podstawowych typów tych zmiennych jest kilka, a ich typy obrazuje poniższy schemat:

![This is an image](https://miro.medium.com/max/631/1*8J9yViDiXqNYeEWctWkdfQ.jpeg)


Obecnie dla nas najważniejsze to:

- **string - str →** w uproszczeniu jest to zapis liter, zwykle jak chcemy, żeby dana zmienna była stringiem musimy dać ją w cudzysłów “to jest string” (tutaj bez problemu możemy robić spacje czyli odstępy między słowami/literami)
- **int - integer →** liczba całkowita, bez przecinków, program nam to zaokrągla – tego typu zmiennej, używamy gdy chcemy wykonać na przykład jakieś równanie matematyczne 1+1
- **dict - dictionary →** słownik, czyli połączenie klucza z jego wartością, słownik zawsze jest zapisywany w formie `{klucz1 : wartość, klucz2 : wartość2}`
    -   Za przykład niech nam posłuży imię oraz numer albumu, przypisane do tej zmiennej (wsadzone do pudełka) o nazwie studenci:
      
 ```python
studenci = {“Michał” : 22121, “Andrzej” : 15521, “Ancymon” : 91211} 
```
    -  Taki słownik może być naprawdę duży, więc aby znaleźć numer albumu pana Ancymona wystarczy wpisać 
 ```python studenci[“Ancymon”]```

    
## Warunki

Dość istotną w programowaniu kwestią są warunki.
Podstawowym założeniem jest sprawdzenie czy coś jest prawdą czy fałszem.

Tak na przykład:
```python

x = 5

if x == 10:
    print("tak, x równa się 10")

```

Nie wyprintuje nam słowa success gdyż x nie równa się 10 tylko 5.

Zwrócić uwagę należy na podwójny ==

W pythonie w ten sposób stawiamy znak równości. Pojedynczy znak =, oznacza w tym przypadku zdefiniowanie zmiennej.


W kondycjach warunkowych możemy stawiać różne warunki, przy użyciu znaku więkoszści, mniejszości czy obu jednocześnie.

Ponadto porównywać możemy nie tylko liczny, ale i słowa/litery etc. 

Dodatkową funkcją warunków jest możliwość tworzenia ich wielokrotnie, a robimy to przy użyciu słowa elif oraz else.

Tak na przykład:

```python

x = 5

if x == 10:
    print("tak x równa się 10")
elif x > 1:
    print("x jest większy od 1")
elif x < 1:
    print("x jest mniejszy od 1")
else:
    print("coś chyba nie zgadłeś")

```

pamiętać należy, że `else` obsługuje wszystko co nie spełniło warunków w poprzednich `if` oraz `elif`
## Funkcje 

Podstawą utworzenia funkcji jest zdefiniowanie jej nazwy.
Robimy to poprzez użycie:
`def nazwafunkcji():`

Możemy do takiej funkcji przekazać również pewnie dane/informacje, należy umieścić ich nazwy po przecinku w nawiasie.

Dla przykładu, jeżeli chcemy utworzyć funkcję, która ma dodać do siebie dwie liczby, musimy zdefiniować jej nazwę, oraz przekazać dwie liczny, które mają być do siebie dodane, przyjmijmy, że będzie to liczba A i liczba być
```python
def dodawanie(a,b):
    wynik = a+b
    return wynik
```


## Pętle

Kolejną ważną rzeczą w programowaniu są pętle.

Polega to na powtórzeniu kodu określoną ilość razy.

Za pierwszą, podstawową w ramach zajęć 0, niech posłuży nam pętla `while`, gdzie w formacie
`while True:`
wykonuje się ona do momentu, aż nie przerwiemy jej słowem `break`


Za przykład posłuży pętla, która co jeden “obrót” podnosi liczbę znajdującą się w zmiennej
`numer_obrotu` o 1, przerwie się jeżeli jego wartość będzie wynosiła 10.

Pamiętać należy, o wcześniejszym utworzeniu zmiennej o nazwie "numer_obrotu"

```python
numer_obrotu = 0
while True:
    numer_obrotu = numer_obrotu + 1
    print (numer_obrotu)
    if numer_obrotu == 10:
        print(“Udało się”)
        break
```

Pamiętaj  o “wcięciach” w kodzie, w przypadku pythona jest to bardzo ważne, gdyż każde takie wcięcie uważane jest za program jakby pod siebie podlegało, było osobnym
“blokiem”.

![pętla1](https://i.imgur.com/Oq1Jyst.png)


Więc w powyższym przykładzie, część pierwszą stanowią zmienna z numerem obrotu oraz
pętla while, “w środku” czyli po tabulacji jest zawartość pętli,



![pętla2](https://i.imgur.com/Wh3dJAu.png)



- w ramach której zwiększamy numer obrotu o 1,
- printujemy ten numer do konsoli (aby go zobaczyć)
- sprawdzamy czy numer równa się == 10

Dopiero w sytuacji, gdy warunek ==10 zostanie spełniony, wykona się część kody "wcięta" pod nim
Takich wcięć możemy zrobić dość dużo (jedno w drugim), jednak nie jest to wspazanie i często nazywane "spaghetti code

![pętla3](https://i.imgur.com/mIESiyq.png)


Cały proces krok-po-kroku możesz prześledzić tutaj: https://tiny.pl/wwrjq
Zmieniony został tylko warunek z == 10 na == 5
