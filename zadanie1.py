
def generator_kodow (kod_poczatkowy, kod_koncowy):
    a,b = kod_poczatkowy.split("-")
    c,d = kod_koncowy.split("-")    #rozdzielenie stringów
    
    int_a = int(a)
    int_b = int(b)  #zamiana stringów na int
    int_c = int(c)
    int_d = int(d)
    
    int_b=int_b+1 #pominięcie wypisania pierwszego kodu
    
    while int_a <= int_c:
        while int_b < 1000:
            if int_a == int_c and int_b == int_d: break   
            print(int_a,"-","{:03}".format(int_b))          #wypisanie kodów
            int_b = int_b + 1
        int_b = 0
        int_a = int_a + 1
    

generator_kodow("79-900", "80-155")
            
