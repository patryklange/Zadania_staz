import numpy as np
import decimal as dc

def generator_listy(poczatek, koniec, krok):
    lista = np.arange(dc.Decimal(poczatek), dc.Decimal(koniec + 0.1) , dc.Decimal(krok)) #arange nie uwzględnia ostatniego elementu "koniec"
    return lista

l = generator_listy(2, 5.5, 0.5)
