#Zadanie 1 (4pkt):
#Utwórz klasę iteratora dla listy. Użyj go do wstawienia elementów listy lista1 do strina.
# elementy mają znajdować się w stringu jednym wierszu niczym nierozdzielone:
class listIterator:
    def __init__(self, list):
        self.list = list
        self.index = 0
        self.string = ""
    def __iter__(self):
        return self
    #def addToList(self, int):

    def __next__(self):
        if self.index >= len(self.list):
            raise StopIteration
        else:
            self.string = self.string + str(self.list[self.index])
            self.index += 1



lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
list = listIterator(lista1)
for x in list:
    pass
wynik1 = list.string

print(wynik1)

#Zadanie2: (4pkt)
#Napisz funkcję fizzbuzz(n), która używając listy składanej zwróci
#listę od 1 do n włącznie liczb lub wyrazów Fizz, Buzz, FizzBuzz, zgodnie ze standradową
#reguła gry w FizzBuzz:
#Jeśli liczba jest podzielna przez 3 i niepodzielna przez 5, zamiast liczby mamy "Fizz".
#Jeśli liczba jest podzielna przez 5 i niepodzielna przez 3, zamiast liczby mamy "Buzz".
#Jeśli liczba jest zarówno podzielna przez 3, jak i przez 5, zamiast liczby mamy "FizzBuzz".
def fizbuzz(n):
    return ["Fizz" if x % 3 == 0 and x % 5 != 0 else "Buzz" if x % 3 != 0 and x % 5 == 0 else "FizzBuzz" if x % 3 == 0 and x % 5 == 0 else x for x in range(1, n+1)]

wynik2 = fizbuzz(16)
print(wynik2)
#Zadanie 3 (4pkt):
#Napisz generator zwracający n wyrazów ciągu Lucasa
#do wyniku zapisz 6 element tego ciągu.

def lucasGenerator(max):
    num1 = 2
    num2 = 1
    temp = 0
    numOfItr = 0
    while numOfItr < max:
        yield num1
        temp = num2 + num1
        num1 = num2
        num2 = temp
        numOfItr = numOfItr + 1
gen = lucasGenerator(6)
for a in gen:
    e = a
wynik3 = e

print(wynik3)
#Zadanie4 (4pkt):
#Uzyj klasy napisanej na ostatnich zajęciach - wersji z iteratorem (wklej tutaj klasę)
#Do przechowywania znaków kodu javy z pliku Main.java.


obiekt = " tutaj utworz obiekt tej klasy."
wynik4="wstaw w wynik4"
#następnie wstaw do niej znaki z kodu javy, które wczytasz z pliku Main.java
#ODKOMENTUJ poniższą linijkę, gdy utworzysz obiekt i dodasz do niego znaki:
'''
!odkomentuj wynik4!:
'''
#wynik4 = obiekt.size()
print(wynik4)

#Zadanie 5 (4pkt):
#Napisz funkcję, która sprawdzi poprawność kodu javy, używając obiektu z poprzedniego zadania
# i uwzględniając tylko nawiasy w kodzie.
#funkcja ma zwrocic True albo False w zależności czy kod jest poprawny czy nie.

def validation(kod_o):
    #zamiast pass napisz swój kod
    pass
wynik5 = validation(kod_o=obiekt)
print(wynik5)







