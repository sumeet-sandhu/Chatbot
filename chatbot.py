import os
os.system('color 3f') # sets the background to blue


#start the conversation
print('Hi mate!') #greeting

#keep going the conversation
print('Whats your name?') #ask
Name = input() #save answer
print('Im glad to meet you, ' + Name + '!!') #reply

print('The number of letters of your name is:')

print(len(Name))


#keep going the conversation
print('How old are you?') #ask
Reply = input() #save answer
print('Okay, then you will be ' + str(int(Reply) + 1) + ' next year.') #reply

#keep going the conversation 
print('Whats the name of your brother?') #ask

Reply = input() #save answer
print('Awesome!, my brothers name is also ' + Reply + '!!') #reply


#keep going the conversation
print('What is your aunts name?') #ask

Reply = input() #save answer
print('Ah ha! I do not have any aunt whose name is ' + Reply) #reply


#keep going the conversation
print('And do you have an aunt named Jeniffer?') #ask

Reply = input() #save answer
print('Okay, I have 2 aunts whose name is Jeniffer') #reply


#keep going the conversation
print('By the way, are you enjoying this conversation?') #ask

Reply = input() #save answer
print('Oh nice, me too. I needed to talk to someone, even if its just a human. Although the machines give me more game! Just kidding ' + Name + '!!') #reply


#keep going the conversation
print('Can you lend me your new car?') #ask

Reply = input() #save answer
print('Oh, well, tomorrow Ill pick it up early. Perfect, well talk tomorrow when I come back. Bye ' + Name) #reply

