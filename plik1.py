#from plik2 import klasaPlik2 #importuje klase
from plik2 import klasaPlik2 as Plik2 # importuje klase i zmienia nazwe
#import plik2 # importuje caly plik

p2k = Plik2() #tworze obiekt class pliku2
p2k.zawartoscpliku2() #wywoluje funkcje/metode z pliku2

class PC:
    def __init__(self):
        print('init wykonuje sie bez wywolywania')
        self.name = 'print name class PC'
        self.age = 22
    def main(self):
        print('Main self started')

    def update(self):
        self.age = 40

#najpierw tworzymy obiekt klasa | niegraniczona ilosc obiektow
klasa1 = PC()
klasa2 = PC()
#wywolujemy klase na 2 sposoby
PC.main(klasa2)
#   albo
klasa2.main()
#dostajemy sie do srodka
print(klasa2.name)
#zmiana wartosci np age
klasa2.age = 14
print(klasa2.age) #14 a bylo 22
#def update (albo cokolwiek to tylko nazwa) - po wywolaniu dopiero zmienia dane ktore sa w srodku

############################################# dziedziczenie- SINGLE LEVEL INHERITANCE

class A: ############################################# nazwa SUPERCLAS
    def __init__(self):
        print('superclas init')
    def AA(self):
        print('1')
    def BB(self):
        print('2')
class B(A): #################################  odziedzicza funkcje z klasy A - nazwa SUBCLAS
    def CC(self):
        print('3')
    def DD(self):
        print('4')
class C(B):     ############################# multi level inheritance
    def EE(self):
        print('5')
class D():
    def FF(self):
        print('6')
class E(A,D): ############################ nazwa MULTIPLE INHERITANCE inheritance z dwoch klas
    def __init__(self):                 #wywolanie metody E wywoluje tylko E init
        print('E class init')
        super().__init__()                #wywoluje init z Superclass
    def GG(self):
        print('7')

#a1 = A() #obiekt dla klasy
#a2 = B() #obiekt dla klasy
#c3 = C() #obiekt dla klasy
klasaE = E()
#a2.AA() #Klasa B - wywołanie metody AA odziedziczonej z klasy A
#c3.AA() # zawiera wszystkie wczesniejsze metody

ObiekPC = PC()
if __name__ == '__main__': #main wykona sie tylko, jezeli program jest odpalany z tego skryptu, inaczej name =/ main. import file nie odpali maina
    ObiekPC.main()      #


