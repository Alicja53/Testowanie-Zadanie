a = int(input("Podaj wartosc a:")
b = int(input("Podaj wartosc b:")
wybor = int(input("Wybierz 1 - dzielenie a / b, wybierz 2 - dzielenie b / a")
if (wybor != 1 or wybor != 2):
            print("Nie ma takiej opcji") 
elif(wybor == 1):
  wynik = a/b
else:
  wynik = b/a 

print(wynik)
