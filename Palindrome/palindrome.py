def palindrome(a):
    result = "Czy slowo jest palindromem?"
    if a[::-1] == a:
            print('Tak')
    else:
            print('Nie')
    return result

print(palindrome(["kajak", "potop"]))