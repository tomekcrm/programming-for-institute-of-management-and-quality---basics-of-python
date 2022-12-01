s18112 = ["Andrzej", "Zalewski", "Siedlce"]
s21542 = ["Grażyna", "Staszewski", "Mińsk Mazowiecki"]
s81123 = ["Stefan", "Kolanowski", "Łuków"]
s91221 = ["Monika", "Kaszewska", "Siedlce"]



#TODO: Utwórz listę studentów z podanych numerów indeksów
studenci = [s18112, s21542, s81123,s91221 ]
#TODO: Stefan zmienił miejsce zamieszkania na Siedlce - nanieś zmiany w kodzie, nie w samej zmiennej

for student in studenci:
    if student[0] == "Stefan":
        student[2] = "Siedlce"

#TODO: W obu programach niżej, system ma pytań użytkownika, czy chce wyszukać lub dodać następną osobę

while True:
    print(studenci)
    print("czy chcesz dodać studenta do listy? T/N")
    decyzja = input()
    
    if decyzja == "T":
        print("Podaj imię studenta")
        imie = input()
        print("Podaj nazwisko studenta")
        nazwisko = input()
        print("Podaj miejsce zamieszkania studenta")
        miejsce = input()
        studenci.append([imie,nazwisko,miejsce])
        
    elif decyzja == "N":
        print("Dziękuję")
        break
    else:
        print("Wpisz T-Tak lub N - Nie")

print(studenci)
#TODO: Utwórz program, który analogicznie tworzy i dodaje studentów do listy - użyj input()
