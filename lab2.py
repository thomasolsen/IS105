# -*- coding: latin-1 -*-
#
#  IS-105 LAB2 Thomas B. Pedersen, Håkon Bergem, Thomas Olsen
#
#  lab2.py - kildekode som inneholder studentenes løsning.
#         
#
#
import sys

# Skriv inn fullt navn på gruppemedlemene (erstatte '-' med navn slikt 'Kari Trå')
gruppe = {  'student1': 'Thomas B. Pedersen', \
			'student2': 'Håkon Bergem', \
            'student3': 'Thomas Olsen', \
}

#
#  Oppgave 1
#    Leke med utskrift 
#    Skriv ut følgende "ascii art" i en funksjon
#    Funksjonen skal hete ascii_fugl() og skal være uten argumenter og uten returverdier
#    Den skal skrive ut følgende når den brukes ascii_fugl
#
#       \/_
#  \,   /( ,/
#   \\\' ///
#    \_ /_/
#    (./
#     '` 
# Using tripple double is the preferred way to do this.
def ascii_fugl():
	pass
	print"""
            \/_
   \,   /( ,/
    \\\' ///
     \_ /_/
     (./
     '
    """	

# 
#  Oppgave 2
#    'return 2' - 2 skal erstattes med en korrekt returverdi, 2 er kun en stedsholder
#    bitAnd - x&y
#    Eksempel: bitAnd(6, 5) = 4
#
def bitAnd(x, y):
  return x & y

#
#  Oppgave 4
#    bitXor - x^y
#    Eksempel: bitXor(4, 5) = 1
#
def bitXor(x, y):
  return x ^ y

#
#  Oppgave 5
#    bitOr - x|y
#    Eksempel: bitOr(0, 1) = 1
#
def bitOr(x, y):
  return x | y

#
#  Oppgave 6
#    ascii8Bin - ta et tegn som argument og returnerer ascii-verdien som 8 bits streng binært
#    Eksempel: ascii8('A) = 01000001
#
#  Tips:
#    For å finne desimalverdien til et tegn bruk funksjonen ord, for eksempel
#      ord('A) , det vil gi et tall 65 i ti-tallssystemet
#    For å formattere 6 i ti-tallssystemet til 00000110 i to-tallssystemet
#      '{0:08b}'.format(6)
#      00000110
#
#    Formatteringsstrengen forklart:
#      {} setter en variabel inn i strengen
#      0 tar variabelen i argument posisjon 0
#      : legger til formatteringsmuligheter for denne variabelen (ellers hadde den 6 desimalt)
#      08 formatterer tall til 8 tegn og fuller med nuller til venstre hvis nødvendig
#      b konverterer tallet til dets binære representasjon
def ascii8Bin(bokstav):
	    bintest = ord(bokstav)
	    toBin = "{0:08b}".format(bintest)
	    print(toBin)

# 
#  Oppgave 7
#    transferBin - ta en tilfeldig streng som argument og skriver ut en blokk av 8-bits strenger
#                  som er den binære representasjon av strengen
#    Eksempel: transferBin("Hi") skriver ut: 
#                01001000
#                01101001
#
def transferBin(string):
	one = list(string)
	for c in one:
	        ascii8Bin(c)
		# skriv ut den binære representasjon av hvert tegn (bruk ascii8Bin funksjonen din)

#
#  Oppgave 8
#    transferHex - gjør det samme som transferBin, bare skriver ut representasjonen
#					av strengen heksadesimalt (bruk formattering forklart i Oppgave 6)
#					Skriv gjerne en støttefunksjon ascii2Hex, som representerer et tegn
#					med 2 heksadesimale tegn
#  
def ascii2Hex(b):
        hextest = ord(b)
        print(hextest)
        

def transferHex(string):
	    x = list(string)
	    for y in x:
	            ascii2Hex(y)
	            
print("This is a bird")
ascii_fugl()
print("This is a sngle ascii character converted to binary")
ascii8Bin("A")
print("This is a string converted to binary")
transferBin("Hi")
print("This is a string converted to hexadecimal")
transferHex("Hi")
