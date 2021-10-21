import time 
import os 

#-----------------------------------------------------bank-----------------------------------------------------------------


verhaal_bank_2 = """---------------------------------------------------------------------------------------------------------

bank beroving gekozen. KANS OP SLAGEN = 10 %   --> TIJD PER VRAAG = 5 seconden -->  NIVAU = niet te doen 

u bnet binnen in de bank u kijkt om u heen en ziet veel kost baren dingen ook een prachtig schilderij de bekende Mona Lisa
dit schilderij is 30 miljoen waard maar het probleem is dat hij aan een zelf vernieteging machine ziet als je de verkeerde 
code invoerd word tie versnipperd en gaan allen allarmen denk goed na je heb 5 seconden om het juiste antwoord in te vullen

de vraag = wat is de echte waarde van het Mona Lisa schilderij

a = 790 miljoen
b = 23 miljoen 
c = 7 miljoen 
d = 3,2 miljard 


"""
#-----------------------------------------------------bank------------------------------------------------------------------

verhaal_bank = """----------------------------------------------------------------------------------------------------------

bank beroving gekozen. KANS OP SLAGEN = 10 %   --> TIJD PER VRAAG = 5 seconden -->  NIVAU = niet te doen 

de bank die u gaat overvallen is een extreem beveiligde bank in spanje de kans dat u hier met de voledigen 
buit van 30 miljoen weg gaat is 5 % om u heeft goed over de overval na gedacht en u denk dat u weet hoe u binnen 
komt via high tech software die u van u kennis bij de FBI heeft gekocht kunt u allen camera bewaking 
uit schakelen en de nood uitgangen open laten gaan er is allen een probleem je moet een check vraag invullen 
die allen de eigenaar vcan de bank weet 

de vraag = hoe heete de eerste opgerichte staats bank 

a = Rabo bank
b = Costa Eriverra bank
c = Monte dei Paschi di Siena
d = de koningklijke munt 

"""

#------------------------------------------------------snackbar---------------------------------------------------------------

verhaal_snackbar_2 = """-------------------------------------------------------------------------------------------------------

snackbar beroving gekozen. KANS OP SLAGEN = 70 %   --> TIJD PER VRAAG = 30 seconden -->  NIVAU = makkelijk

u bent nu binnen in de snackbar je bent het geld aan het zoeken je ziet een enorme gouden bitterbal staan
ter waarde van 2000 euro het probleem is allen dat de gouden bitterbal aan een ketting vast zit met een code
denk goed na aan de volgende op gaven wand dat is de goede combo

de vraag = welke snack uit de vorrige vraag bestaat niet 

a = bitterbal
b = broodje kipnuget
c = nasi puk
d = gefrituurd broodje inkt vis

"""



#-------------------------------------------------------snackbar----------------------------------------------------------------

verhaal_snackbar = """----------------------------------------------------------------------------------------------------------

snackbar beroving gekozen. KANS OP SLAGEN = 70 %   --> TIJD PER VRAAG = 30 seconden -->  NIVAU = makkelijk

de snackbar die u gaat overvallen is een kleinen snack bar ecrgens in het centrum de snack bar is tot 6 uur open 
de bedoeling is om na 12 uur snachts toe te slaan om deze tijd is het lekker rustig op straat om binnen te komen 
moet u een vraag beantwoorden die te maken heeft met de beroving de moelijkheid is makkelijk de kans dat u met 
het voledige bedrag weg gaat is daarom ook 70 % 

-------------------------------------------------------------------------------------------------------------------------------
VEEL SUCCES 
-------------------------------------------------------------------------------------------------------------------------------
de vraag is wat is de meest verkochte snack 

a = nasi puk
b = bitterbal 
c = frikandel
d = broodje bitterbal

"""


#--------------------------------------------------------juwelier---------------------------------------------------------------

verhaal_juwelier_2 = """--------------------------------------------------------------------------------------------------------

u keuze was juwelier  KANS OP SLAGEN = 35 %   -->  TIJD PER VRAAG = 10 seconden  -->   NIVAU = moelijk

u bent nu in de juweliers zaak u komt ziet allemaal mooien horloges liggen in de fritine je wilt dit zo stil mogelijk doen
je kan natuurlijk het glas in slaan maar dan gaan de alarmen af je ziet wel een kasje waar je een wachtwoord
moet invullen denk goed terug aan het eerste vraag het antwoord wat bij vraag a stond is de juiste code 
vul die in en de fritrines gaan zonder dat het alarm af gaat open

u kan kiezen uit de volgende code combinaties

a = China
b = Nederland
c = Mogolie 
d = Italie
e = Rusland


"""
#----------------------------------------------------------juwelier---------------------------------------------------------------

verhaal_juwelier = """------------------------------------------------------------------------------------------------------------

u keuze was juwelier  KANS OP SLAGEN = 35 %   -->  TIJD PER VRAAG = 10 seconden  -->  NIVAU = makkelijk

deze beroving heeft een niveu van van moelijk de kans dat u slaagt voor de vraag en met 1 miljoen naar huis gaat 
is 35 % juwelier die u gaat overvallen is gespesialiseerd in het horloge merk rolex dit zijn peper duure horloges
beantwoord de volgende vraag goed als u dit antwoord goed heeft gaat u met een mooi bedrag naar huis die u eerlijk heeft
verdiend de vraag gaat over het product die u gaat proberen te stelen. als u het goede antwoord kies bent u binnen zonder dat het 
alarm is af gegaan 

de vraag = welk land komt het merk rolex orspronkelijk van daan 

a = Italie
b = china 
c = Rusland
d = Zwitseland 
e = Nederland 
-------------------------------------------------------------------------------------------------------------------------------------
VEEL SUCCES !!!!!!!!!!!!!!!!!!!!!
-------------------------------------------------------------------------------------------------------------------------------------
"""




# ---------------------------------------------------------introverhaal--------------------------------------------------------------

intro_verhaal = """------------------------------------------------------------------------------------------------------------------    
-------------------------------------------------------------------------------------------------------------------------------------                                                                                                                          |
je gaat een bank beroven je heb een paar opties waar uit je kunt kiezen dit zijn opties                                                                          
voor wat je kunst stelen kies wat je leuk vind en wat je het handigst lijkt en kijk wat het lot je brengt                    
wordt je rijk of eindig je in de bak. elke beroving heeft een  bepaalde moelijkheids graad 
de hoeveel heid buit op brengst bepaald hoe moelijk het gemaakt wordt 

dit zijn de moelijkheids graden die er zijn 

- makkelijk kans op slagen is        70 % -->  30 seconde na denk tijd 
- moelijk kans op slagen is          35 % -->  10 seconde nadenk tijd
- niet te doen  kans op slagen is    10 % -->  5 seconde nadenk tijd 
               
--------------------------------------------------------------------------------------------------------------------------------------                                                                                                                                           |
a = is een juwelier de kans dat je met de volle buit van een 1 miljoen euro weg gaat is 35 procent                                                 
b = is een snack bar de kans dat je met de volle buit van 2000 euro weg gaat is 70 procent                                    
c = is de nederlandse bank de kans dat je met de volle buit weg gaat van 30 miljoen euro is 10 procent                        
--------------------------------------------------------------------------------------------------------------------------------------                   
--------------------------------------------------------------------------------------------------------------------------------------
"""

#------------------------------------------------def function juwelier----------------------------------------------------------------

def kies_beroving_a ():                                                             # def kies beroving                        
    print(intro_verhaal)
    kies_bank = input("maak u keuze")
    if kies_bank=="a":
     vraag_juwelier_1()                                                             # def vraag juwelier                  
     kies_beroving_b                                                                # def kies beroving
                     

           
      
# def vraag juwelier 1      

def vraag_juwelier_1():                                                              # def vraag juwelier 
    print(verhaal_juwelier)
    time.sleep(1)
    os.system("cls")
    kies_land = input("maak u keuze")
    if kies_land=="d":
      print("dit was het goede antwoord") + vraag_juwelier_2()
    else:
        print("dit was niet het goede antwoord u bent gepakt ")  
    

# vraag juwelier 2 

def vraag_juwelier_2():                                                               # def vraag juwelier 2   
    print(verhaal_juwelier_2)
    time.sleep(10)
    os.system("cls")
    kies_code = input("maak u keuze")
    if kies_code=="d":
        print("dit was het goede antwoord u heb de voledige buit gestolen  ")
    else:
        print("dit was de foute code u bent opgepakt")


#------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------def function snackbar-----------------------------------------------------------------



def kies_beroving_b():                                                                      # def beroving                                         
    kies_bank_2 = input("maak u keuze")
    if kies_bank_2=="b":
        vraag_snackbar_1()   
        vraag_snackbar_2()
                                                                      


def vraag_snackbar_1():                                                                     # def vraag snackbar 
    print(verhaal_snackbar)
    time.sleep(30)
    os.system("cls")
    kies_snack =input("maak u keuze")
    if kies_snack=="c":
        print("dit was het goede antwoord ") + vraag_snackbar_2()
    else:
        print("dit was het foute antwoord u bent gepakt ")


def vraag_snackbar_2():                                                                      # def vraag snack bar 2 
    print(verhaal_snackbar_2)  
    time.sleep(30)
    os.system("cls")  
    foute_snack = input("maak u keuze ")
    if foute_snack=="c":
        print("u antwoord is goed u bent ermee weg gekomen ")    
    else:
        print("u heeft het verkeerde antwoord in gevoerd u gaat de bak in ")

#---------------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------def fuction bank---------------------------------------------------------------------
 
def kies_beroving_c():                                                                         # def kies beroving
    kies_bank_3 = input("maak u keuze ")
    if kies_bank_3=="c":
        vraag_bank_1()                                                                         # def vraag bank 1
        vraag_bank_2()                                                                         # def vraag bank 2



def vraag_bank_1():                                                                            # def vraag bank 1
    print(verhaal_bank)
    time.sleep(5)
    os.system("cls")
    kies_eerste_bank = input ("maak u keuze ")
    if kies_eerste_bank=="c":
        print("dit was het goede antwoord u bent binnen ") + vraag_bank_2()
    else:
        ("dit was het foute antwoord de alarmen zijn afgegaan")

def vraag_bank_2():                                                                            # def vraag bank 2
    print(verhaal_bank_2) 
    time.sleep(5)
    os.system("cls")  
    prijs_Mona_Lisa = input ("maak u keuze ")
    if prijs_Mona_Lisa=="a":
        print ("u bent geweldig u heeft hem eerlijk gestolen")     
    else:
       print ("dit was het foute antwoord het schilderij is versnippert ! ")

#---------------------------------------------------allen fuctions in 3 aanroepen------------------------------------------------------------------------------------------------
    
                                                  
kies_beroving_a()                # aanroep als je A kiest                                                                        
kies_beroving_b()                # aanroep als je B kiest
kies_beroving_c()                # aanroep asl he c kiest








































 