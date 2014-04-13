'''
Created on 13.04.2014

@author: Elena

import easygui
flavour = easygui.buttonbox("wHAT IS YOUR FAVORITE ICE CREAM FLAVOUR?",
                            choices = ['Vanilla', 'Chocolate', 'Mango', 'Strawberry'] )
easygui.msgbox ("You picked " + flavour)


import easygui
flavour = easygui.choicebox("wHAT IS YOUR FAVORITE ICE CREAM FLAVOUR?",
                            choices = ['Vanilla', 'Chocolate', 'Mango', 'Strawberry'] )
easygui.msgbox ("You picked " + flavour)

import easygui
flavour = easygui.enterbox("What is your favorite ice cream flavour?")
easygui.msgbox ("You entered " + flavour)

import easygui
flavour = easygui.enterbox("WHAT IS YOUR FAVORITE ICE CREAM FLAVOUR?",
                            default = 'Vanilla')
easygui.msgbox ("You picked " + flavour)


import random, easygui

secret = random.randint (1, 99)
guess = 0
tries = 0

easygui.msgbox("""AHOY!  I'm the Dread Pirate Roberts, and I have a secret! It is a number from 1 to 99. I'll give you 6 tries.""")

while guess != secret and tries < 6:
    guess = easygui.integerbox("What is yer guess, matey?")
    if not guess: break
    if guess < secret:
        easygui.msgbox(str(guess) + " is too low, ye scurvy dog!")
    elif guess > secret:
        easygui.msgbox(str(guess) + " is too high, landlubber!")
    tries = tries + 1        
     
if guess == secret:
    easygui.msgbox("Avast! Ye got it! Found my secret, ye did!")
else:
    easygui.msgbox("No more guesses!  Better luck next time, matey!")    
    
    
import easygui
fahreinheit = easygui.integerbox("Wie viel Fahreinheit sind es?")
c = 5.0/9* (fahreinheit-32)
easygui.msgbox (str(fahreinheit)+ " sind "+ str(c)+ " Celsius")
'''
import easygui
name = easygui.enterbox("What's your name?")
strasse = easygui.enterbox("In welcher Strasse wohnst du?")
stadt = easygui.enterbox("In which town do you live?")
plz = easygui.enterbox("What's your PLZ?")
addString = name +"\n" + strasse +"\n"+ plz +" "+ stadt
easygui.msgbox(addString)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        