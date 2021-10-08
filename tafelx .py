# Het programma begint met de vraag: “Van welk getal wilt u de tafel zien?”

# Het antwoord van de vraag wordt als argument aan een function mee gegeven die 1 parameter heeft dat een int moet zijn.

# De function laat door middel van een loop de tafel (1 t/m 10) van het gekozen getal op het scherm zien.

 
def tafel(a,b):                              # tafel = a maal b 
    return(a*b)                              # retun functie a maal b 
kiestafel=int(input("welke tafel wilt u"))   # kiestafel = input welke tafel wilt u 
for x in range(1,11):                        # range in loop is 1,10 
     antwoord = tafel(x,kiestafel)           # antwoord = tafel 10 x gekozen tafel in kies tafel 
     print (antwoord)                        # hier print het perogramma de uitkomst van de gekozen tafels 
     