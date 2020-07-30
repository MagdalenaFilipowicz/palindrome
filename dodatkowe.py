import logging
logging.basicConfig(level=logging.INFO)

print("Projekt Magazyn")

magazyn = {"Screwdriver":[5, 'no', 40], "Wrench":[10, 'no', 50], "Hex key":[50, 'no', 100]}

def get_items():
    a=input("What would you like me to do?") 
    if a == (f"show"):
        print("Name\tQuantity\tUnit\tUnit Price (PLN)")
       
 
get_items()
