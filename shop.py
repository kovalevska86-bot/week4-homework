import sys
import storage
import utils

def main():
    if len(sys.argv) < 2:
        print("Komandas: add [vārds] [qty], list, total, clear")
        return

    command = sys.argv[1]
    items = storage.load_list()

    if command == "add":
        # Pārbaudām, vai ir pietiekami daudz argumentu (add nosaukums daudzums)
        if len(sys.argv) < 4:
            print("Kļūda: Jānorāda nosaukums un daudzums! (Piemēram: add Maize 3)")
            return

        name = sys.argv[2]
        
        try:
            qty = int(sys.argv[3])
            if qty <= 0:
                print("Kļūda: Daudzumam jābūt virs 0!")
                return
            
            # 1. Pārbaudām, vai šim produktam jau ir zināma cena
            price = storage.get_price(name)
            
            if price is not None:
                print(f"Atrasta cena: {price:.2f} EUR/gab.")
                choice = input("[A]kceptēt / [M]ainīt? ").strip().upper()
                
                if choice == 'M':
                    new_price_input = input("Jaunā cena: > ")
                    price = float(new_price_input)
                    storage.set_price(name, price)
                    print(f"✓ Cena atjaunināta: {name} → {price:.2f} EUR")
            else:
                # 2. Ja cenas nav, prasām to lietotājam
                print("Cena nav zināma.")
                new_price_input = input("Ievadi cenu: > ")
                price = float(new_price_input)
                storage.set_price(name, price)
                print(f"✓ Cena saglabāta: {name} ({price:.2f} EUR)")

            if price <= 0:
                print("Kļūda: Cenai jābūt virs 0!")
                return

            # 3. Pievienojam produktu sarakstam un saglabājam
            new_item = {"name": name, "qty": qty, "price": price}
            items.append(new_item)
            storage.save_list(items)
            
            line_total = utils.calc_line_total(new_item)
            print(f"✓ Pievienots: {name} × {qty} ({price:.2f} EUR/gab.) = {line_total:.2f} EUR")
            
        except ValueError:
            print("Kļūda: Daudzumam un cenai jābūt skaitļiem!")

    elif command == "list":
        if not items:
            print("Saraksts ir tukšs.")
            return
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