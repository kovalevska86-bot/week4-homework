def calc_line_total(item):
    # Sareizina daudzumu ar cenu vienam produktam
    return item['qty'] * item['price']

def calc_grand_total(items):
    # Saskaita visu produktu kopsummu
    return sum(calc_line_total(item) for item in items)

def count_units(items):
    # Saskaita kopējo fizisko vienību skaitu (piem., 3 maizes + 2 pieni = 5 vienības)
    return sum(item['qty'] for item in items)