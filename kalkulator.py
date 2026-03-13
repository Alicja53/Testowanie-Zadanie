login = input("Wpisz swoj login")
print(f"Hej {login}")
a = int(input("Podaj wartosc a:")
b = int(input("Podaj wartosc b:")
wybor = int(input("Wybierz 1 - dzielenie a / b, wybierz 2 - dzielenie b / a")
if (wybor != 1 or wybor != 2):
            print("Nie ma takiej opcji") 
elif(wybor == 1):
            if(b==0):
                        print("Błąd dzielenia przez 0")
  wynik = a/b
else:
            if(a==0):
                        print("Błąd dzielenia przez 0")
  wynik = b/a 

print(wynik)
print("zmiana2")
