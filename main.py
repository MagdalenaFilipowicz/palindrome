print("Zadanie 1")
shop = {'piekarnia':['Chleb','pączek','Bułki'] , 'Warzywniak':['Marchew','Seler','Rukola']}
for k in shop:
    print(f"Idę do {k.capitalize()}, Kupuję tu następujące rzeczy: {str(shop[k]).title()}")
print(f"W sumie kupuję {sum(len(v)for v in shop.values())} produktów.")
print("\n")
print("Zadanie 2")
list = []
for i in range(101):
    if i%5 ==0:
        a=i**3
        print(i)
        list.append(a)
print(list)


