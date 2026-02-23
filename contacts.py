import json
import sys
import os

FILENAME = "contacts.json"

# 1. Funkcija ielādēšanai
def load_contacts():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as f:
        return json.load(f)

# 2. Funkcija saglabāšanai
def save_contacts(contacts):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=4, ensure_ascii=False)

# 3. Funkcija visu kontaktu parādīšanai (list)
def list_contacts():
    contacts = load_contacts()
    if not contacts:
        print("Kontaktu saraksts ir tukšs.")
        return
    print("Kontakti:")
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} — {c['phone']}")

# 4. Funkcija meklēšanai (search)
def search_contacts(query):
    contacts = load_contacts()
    # Atrod visus, kuru vārdā ir meklētais teksts
    found = [c for c in contacts if query.lower() in c['name'].lower()]
    
    if found:
        print(f"Atrasti {len(found)} kontakti:")
        for i, c in enumerate(found, 1):
            print(f"{i}. {c['name']} — {c['phone']}")
    else:
        print(f"Kontakti ar vārdu '{query}' netika atrasti.")

# --- Galvenā loģika komandu apstrādei ---
if len(sys.argv) > 1:
    command = sys.argv[1]

    if command == "add":
        contacts = load_contacts()
        name = sys.argv[2]
        phone = sys.argv[3]
        
        contacts.append({"name": name, "phone": phone})
        save_contacts(contacts)
        print(f"✓ Pievienots: {name} ({phone})")

    elif command == "list":
        list_contacts()

    elif command == "search":
        if len(sys.argv) > 2:
            search_contacts(sys.argv[2])
        else:
            print("Lūdzu, norādi meklējamo vārdu!")