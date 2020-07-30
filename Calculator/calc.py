print("Kalkulator 1")

import logging
logging.basicConfig(level=logging.INFO)

a = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:  ") 
x = int(input("Podaj składnik 1."))
y = int(input("Podaj składnik 2."))

operators = {"+": x+y, "-": x-y, "*": x*y, "/": x/y, "**": x**y}

if a == "1":
    logging.info(f"Dodaję {x} i {y}")
    print("Wynik to = ", operators["+"])
elif a == "2":
    logging.info(f"Odejmuję {y} od {x}")
    print("Wynik to = ", operators["-"])
elif a == "3":
    logging.info(f"Mnożę {x} i {y}")
    print("Wynik to = ", operators["*"])
elif a == "4":
    logging.info(f"Dzielę {x} przez {y}")
    print("Wynik to = ", operators["/"])
else:
    print("Error: no such operation)")
