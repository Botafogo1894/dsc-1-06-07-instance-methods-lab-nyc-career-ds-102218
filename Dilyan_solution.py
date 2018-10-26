 #Creating classes Driver and Passenger
class Driver:
    def greeting(self):
        return "Hey, how are you?"

    def ask_for_destination(self):
        return "Where would you like to go today?"

class Passenger:

    def reply_greeting(self):
        return "I am doing well! Thanks for picking me up today!"

    def in_a_hurry(self):
        return "Punch it! They're on our tail!"
#2.Creating two instances for each class

daniel = Driver()
meryl = Driver()
niky = Passenger()
terrance = Passenger()

#Drivers and passengers communicating
polite_greeting = daniel.greeting()
print(polite_greeting)

no_time_to_talk = niky.in_a_hurry()
print(no_time_to_talk)

class Lion:
    def speak(self):
        return """In the jungle, the mighty jungle
The lion sleeps tonight"""

class Tiger:
    def speak(self):
        return """I got the eye of the tiger, a fighter
Dancing through the fire
Cause I am a champion, and you're gonna hear me roar
Louder, louder than a lion
Cause I am a champion, and you're gonna hear me roar!"""

class Elephant:
    def speak(self):
        return """Nellie the Elephant packed her trunk
And said goodbye to the circus
Off she went with a trumpety-trump
Trump, trump, trump"""

simba = Lion()
tony = Tiger()
dumbo = Elephant()

zoo = [simba, tony, dumbo]

for animal in zoo:
    print(animal.speak())
