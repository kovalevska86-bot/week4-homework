import sys
import storage  # Importējam mūsu pašu izveidoto moduli!

def main():
    if len(sys.argv) < 2:
        print("Lūdzu, ievadi komandu (add, list, total, clear)")
        return

    command = sys.argv[1]
    items = storage.load_list()

    if command == "add":
        name = sys.argv[2]
        price = float(sys.argv[3]) # Pārvēršam tekstu par skaitli
        items.append({"name": name, "price": price})
        storage.save_list(items)
        print(f"✓ Pievienots: {name} ({price:.2f} EUR)")

    elif command == "list":
        print("Iepirkumu saraksts:")
        for i, item in enumerate(items, 1):
            print(f"{i}. {item['name']} — {item['price']:.2f} EUR")

    elif command == "total":
        # Saskaitām visas cenas sarakstā
        kopsumma = sum(item['price'] for item in items)
        print(f"Kopā: {kopsumma:.2f} EUR ({len(items)} produkti)")

    elif command == "clear":
        storage.save_list([]) # Saglabājam tukšu sarakstu
        print("✓ Saraksts notīrīts!")

if __name__ == "__main__":
    main()