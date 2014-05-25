'''
Created on 25.05.2014

@author: Elena
'''
for looper in [1, 2, 3, 4, 5]:
    print "hello"
    
for looper in [1, 2, 3, 4, 5]:
    print looper
    
for looper in [1, 2, 3, 4, 5]:
    print looper, "times 8 =", looper * 8
    
for looper in range (1, 11):
    print looper, "times 8 =", looper * 8
    
for cool_guy in ["Spongebob", "Spiderman", "Justin Timberlake", "My Dad"]:
    print cool_guy, "is the coolest guy ever!"
    
print "Type 3 to continue, anything else to quit."
someInput = raw_input()
while someInput  == '3':
    print "Thank you for the 3. Very kind of you."
    print "type 3 to continue, anything else to quit."
    someInput = raw_input()
print "That's not 3, so I'm, quitting now."

for i in range (1, 6):
    print 
    print 'i =', i,
    print 'hello, how',
    if i == 3:
        continue
    print 'are you today?'

print "Which multiplication table would you like?"
nummer = int(raw_input ())
print "Here's your table:"
for looper in range (1, 11):
    print looper, "x ", nummer, "= ", nummer * looper

print "Which multiplication table would you like?"
nummer = int(raw_input ())
print "How high do you want to go?"
high = int(raw_input())
print "Here's your table:"
for looper in range (1, high):
    print looper, "x ", nummer, "= ", nummer * looper











    
