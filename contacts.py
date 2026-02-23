import json
import sys
import os

FILENAME = "contacts.json"

# 1. Funkcija, kas ielādē esošos kontaktus
def load_contacts():
    if not os.path.exists(FILENAME):
        return [] # Ja faila nav, atdodam tukšu sarakstu
    with open(FILENAME, "r", encoding="utf-8") as f:
        return json.load(f) # Nolasa datus no faila

# 2. Funkcija, kas saglabā visus kontaktus
def save_contacts(contacts):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=4) # Ieraksta ar atkāpēm, lai smuki

# 3. Galvenā loģika komandu apstrāde
if len(sys.argv) > 1:
    command = sys.argv[1]

    if command == "add":
        # Ielādējam to, kas jau ir failā
        contacts = load_contacts()
        
        # Izveidojam jaunu kontaktu no termināļa datiem
        new_contact = {
            "name": sys.argv[2],
            "phone": sys.argv[3]
        }
        
        # Pieliekam klāt sarakstam un saglabājam
        contacts.append(new_contact)
        save_contacts(contacts)
        print(f"Kontakts {sys.argv[2]} pievienots!")