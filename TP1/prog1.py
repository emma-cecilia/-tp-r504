import fonctions as f

print("CTRL-C pour quitter.")
while True:
    try:
        a = int(input("a = "))  # on veut des entiers
        b = int(input("b = "))
        res = f.puissance(a, b)  # Q2.3 : appel via le module importé
        print(res)
    except ValueError:
        print("Veuillez entrer des entiers valides.")
    except KeyboardInterrupt:
        print("\nAu revoir.")
        break

# Q2.5 : vérification que des flottants déclenchent TypeError
try:
    f.puissance(2.5, 3.0)   # flottants -> doit lever TypeError
except TypeError as e:
    print("OK:", e)

