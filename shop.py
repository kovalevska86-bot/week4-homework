import sys
import storage
import utils

def main():
    if len(sys.argv) < 2:
        print("Komandas: add [vārds] [daudzums] [cena], list, total, clear")
        return

    command = sys.argv[1]
    items = storage.load_list()

    if command == "add":
        # Pārbaudām, vai ir pietiekami daudz argumentu (kopā jābūt 5: shop.py, add, vārds, qty, price)
        if len(sys.argv) < 5:
            print("Kļūda: Jānorāda nosaukums, daudzums un cena! (Piemēram: add Maize 3 1.20)")
            return

        name = sys.argv[2]
        
        try:
            qty = int(sys.argv[3])
            price = float(sys.argv[4])
            
            if qty <= 0 or price <= 0:
                print("Kļūda: Daudzumam un cenai jābūt virs 0!")
                return
                
            new_item = {"name": name, "qty": qty, "price": price}
            items.append(new_item)
            storage.save_list(items)
            
            line_total = utils.calc_line_total(new_item)
            print(f"✓ Pievienots: {name} × {qty} ({price:.2f} EUR/gab.) = {line_total:.2f} EUR")
            
        except ValueError:
            print("Kļūda: Daudzumam un cenai jābūt skaitļiem!")

    elif command == "list":
        print("Iepirkumu saraksts:")
        for i, item in enumerate(items, 1):
            line_total = utils.calc_line_total(item)
            print(f"{i}. {item['name']} × {item['qty']} — {item['price']:.2f} EUR/gab. — {line_total:.2f} EUR")

    elif command == "total":
        total_price = utils.calc_grand_total(items)
        total_units = utils.count_units(items)
        print(f"Kopā: {total_price:.2f} EUR ({total_units} vienības, {len(items)} produkti)")

    elif command == "clear":
        storage.save_list([])
        print("✓ Saraksts notīrīts!")

if __name__ == "__main__":
    main()