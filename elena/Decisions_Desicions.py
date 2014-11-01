'''
Created on 27.04.2014

@author: Elena
'''

num1 = float(raw_input("Enter the first Number: "))
num2 = float(raw_input("Enter the second number: "))
if num1 <  num2:
    print num1,  "is less than", num2
if num1 > num2:
    print num1,  "is greater than", num2
if num1 != num2:
    print num1,  "is not equal to", num2
if num1 == num2:
    print num1,  "is equal to", num2


preis = float(raw_input("Wie viele Fr. kostet das, was du kaufen willst?"))
rabat10 = preis*0.1
rabat20 = preis*0.2
if preis <= 10:
    print "Du musst", preis-rabat10, "Fr. bezahlen."
if preis > 10:
    print "Du musst", preis-rabat20, "Fr. bezahlen."

import easygui
geschlecht = easygui.buttonbox("Bist du ein Junge oder ein Maedchen?",
                               choices= ['Junge', 'Maedchen'])
if geschlecht == 'Maedchen':
    alter = float(raw_input("Wie alt bist du?"))
    if alter >= 10 and alter <= 12:
        print "Super!!! Du bist herzlich eingeladen um am 23.4 bei uns ein Testspiel zu absolvieren."
    elif alter < 10 or alter > 12:
        print "Leider kannst du bei unserem Fussballclub nicht mitspielen."
if geschlecht == 'Junge':
    print "Leider kannst du bei unserem Fussballclub nicht mitspielen."
    
tank = float(raw_input("How big is your tank, in liters?"))
voll = float(raw_input("How full is your tank in liters?"))
km = float(raw_input("How many km per liter does  your car get?"))
print "Size of tank:", tank
print "liter full:", voll
print "km per liter:", km
weiter = km*voll
print "You can go another", weiter
print "The next gas station is 200 km away."
if weiter > 200:
    print "You can wait for the next station."
if weiter <200:
    print "Get gas now!"

passwort = "ahs5ka"
was= raw_input("What is the password?")
if was == passwort:
    print "You're in!!"
if was != passwort:
    print "No the password is false! ):"




    