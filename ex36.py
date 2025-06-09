## Talk to cook to start or not to end.
# Ask for items. start quests?
# Get items:
# Bucket
#   Milk
# Egg
# Pot
#   Flour
# Deliver

from sys import exit

def start():
    print("You notice a troubled cook in the kitchen.")
    print("Do you want to talk to him?")
    print("Options available: YES | NO")
    
    while True:        
        talk_to_cook = input("> ")
        
        if talk_to_cook.upper() == "YES":
            speakToCook()
        elif talk_to_cook.upper() == "NO":
            endQuest(1)
        else:
            print("Enter a valid option.")


def endQuest(ending):
    if ending == 1:
        print("You leave the cook stressed...")
    elif ending == 2:
        print("Player: No, I don't feel like it. Maybe later.")
        input("> [Press enter]")
        print("Cook: Fine. I always knew you Adventurer types were callous beasts. Go on your merry way!")
    elif ending == 0:
        print("Congratulations! Quest completed!")
        
    exit(0)


def speakToCook():
    print("Cook: What am I to do?")
    print("1. What's wrong?")
    print("2. You're a cook, why don't you bake me a cake?")
    print("3. You don't look very happy.")
    print("4. Nice hat!")
    print("Options available: 1 | 2 | 3 | 4")
    
    optionSelected = 0
    
    while True:
        try:
            optionSelected = int(input("> "))
        except ValueError:
            print("Enter a valid option.")
        else:
            if optionSelected == 1:
                whatsWrong()
            elif optionSelected == 2:
                bakeMeCake()
            elif optionSelected == 3:
                cookLook()
            elif optionSelected == 4:
                niceHat()
            else:
                print("Enter a valid option.")
      
                
def whatsWrong():
    print("Player: What's wrong?")
    input("> [Press enter]")
    print("Cook: Oh dear, oh dear, oh dear, I'm in a terrible mess! It's the Duke's birthday today, and I should be making him a lovely big birthday cake.")
    input("> [Press enter]")
    print("Cook: I've forgotten to buy the ingredients. I'll never get them in time now. He'll sack me! What will I do? I have four children and a goat to look after. Would you help me? Please?")
    print("Options available: YES | NO")
    
    while True:        
        start_quest = input("> ")
        
        if start_quest.upper() == "YES":
            startQuest()
        elif start_quest.upper() == "NO":
            endQuest(2)
        else:
            print("Enter a valid option.")
    
    
def bakeMeCake():
    print("Player: You're a cook, why don't you bake me a cake?")
    input("> [Press enter]")
    print("Cook: *sniff* Don't talk to me about cakes...")
    input("> [Press enter]")
    
    whatsWrong()
    
    
def cookLook():
    print("Player: You don't look very happy.")
    input("> [Press enter]")
    print("Cook: No, I'm not. The world is caving in around me - I am overcome by dark feelings of impeding doom.")
    print("1. What's wrong?")
    print("2. I'd take the rest of the day off if I were you.")
    print("Options available: 1 | 2")
    
    optionSelected = 0
    
    while True:
        try:
            optionSelected = int(input("> "))
        except ValueError:
            print("Enter a valid option.")
        else:
            if optionSelected == 1:
                whatsWrong()
            elif optionSelected == 2:
                dayOff()
            else:
                print("Enter a valid option.")
 
 
def niceHat():
    print("Player: Nice hat!")
    input("> [Press enter]")
    print("Cook: Err thank you. It's a pretty ordinary cooks hat really.")
    input("> [Press enter]")
    print("Player: Still suits you. The trousers are pretty special too.")
    input("> [Press enter]")
    print("It's all standard cook's issue uniform...")
    input("> [Press enter]")
    print("Player: The whole hat, apron, stripey trousers ensemble - it works. It make you looks like a real cook.")
    input("> [Press enter]")
    print("Cook: I am a real cook! I haven't got time to be chatting about Culinary Fashion. I am in desperate need of help!")
    
    whatsWrong()
   
   
def dayOff():
    print("Player: I'd take the rest of the day off if I were you.")
    input("> [Press enter]")
    print("Cook: No, that's the worst thing I could do. I'd get in terrible trouble.")
    input("> [Press enter]")
    print("Player: Well maybe you need to take a holiday...")
    input("> [Press enter]")
    print("Cook: That would be nice, but the King doesn't allow holidays for the head Chef.")
    input("> [Press enter]")
    print("Player: Hmm, why not run away to the sea and start a new life as a Pirate?")
    input("> [Press enter]")
    print("Cook: My wife gets sea sick, and I have an irrational fear of eyepatches. I don't see it working myself.")
    input("> [Press enter]")
    print("Player: I'm afraid I've run out of ideas.")
    input("> [Press enter]")
    print("Cook: I know I'm doomed.")
    input("> [Press enter]")
    
    whatsWrong()
      
      
def startQuest():
    print("Player: Yes, I'll help you.")
    input("> [Press enter]")
    print("Oh thank you, thank you. I need milk, an egg and flour. I'd be very grateful if you can get them for me.")
    input("> [Press enter]")
    print("Player: So where do I find these ingredients then?")
    askForItems() 
      
def askForItems():
    print("1. Where do I find some flour?")
    print("2. How about milk?")
    print("3. And eggs? Where are they found?")
    print("4. Go and get the items.")
    print("Options available: 1 | 2 | 3 | 4")
    
    optionSelected = 0
    
    while True:
        try:
            optionSelected = int(input("> "))
        except ValueError:
            print("Enter a valid option.")
        else:
            if optionSelected == 1:
                print("Player: Where do I find some flour?")
                input("> [Press enter]")
                print("Cook: There is a Mill fairy close, go North and then West. Mill is just off the road to Draynor. I usually get my flour from there.")
                input("> [Press enter]")
                print("Talk to Millie, she'll help, she's a lovely girl and a fine Miller. Make sure you take a pot with you for the flour though, there should be one on the table in here.")
                input("> [Press enter]")
            elif optionSelected == 2:
                print("Player: How about milk?")
                input("> [Press enter]")
                print("Cook: There is a cattle field on the other side of the river, just across the road from the Groats' Farm.")
                input("> [Press enter]")
                print("Cook: You'll need an empty bucket for the milk itself. The general store just north of the castle will sell you one for a couple of coins.")
                input("> [Press enter]")                
            elif optionSelected == 3:
                print("Player: And eggs? Where are they found?")
                input("> [Press enter]")
                print("Cook: I normally get my eggs from the Groats' Farm, on the other side of the river.")
                input("> [Press enter]")
                print("Cook: But any chicken should lay eggs.")
            elif optionSelected == 4:
                print("Player: I need to get the items, cya.")
                input("> [Press enter]")
                continueQuest()
            else:
                print("Enter a valid option.")
      
      
def continueQuest():
    print("1. Go at the mill and get the flour.")
    print("2. Grab some milk from the farm.")
    print("3. Get eggs from Groats' Farm.")
    print("4. Return with the items to the cook.")
    print("Options available: 1 | 2 | 3 | 4")
    
    optionSelected = 0
    global hasFlour
    global hasMilk 
    global hasEggs

    while True:
        try:
            optionSelected = int(input("> "))
        except ValueError:
            print("Enter a valid option.")
        else:
            if optionSelected == 1:
                print("Player: Retrieve the flour from the mill.")
                input("> [Press enter]")
                hasFlour = True
            elif optionSelected == 2:
                print("Player: Retrieve the milk from the cows in the farm.")
                input("> [Press enter]")
                hasMilk = True              
            elif optionSelected == 3:
                print("Player: Retrieve the eggs from some chikens from the Groats' Farm.")
                input("> [Press enter]")
                hasEggs = True
            elif optionSelected == 4:
                if hasFlour and hasEggs and hasMilk:
                    finishQuest()
                else:
                    print("Get all the items first. You don't want to get to the chef without the items...")
            else:
                print("Enter a valid option.")
    

def finishQuest():
    print("Cook: How are you getting on with finding the ingredients?")
    input("> [Press enter]")
    print("Player: Here's a bucket of milk.")
    input("> [Press enter]")
    print("Player: Here's a pot of flour.")
    input("> [Press enter]")
    print("Player: Here's a fresh egg.")
    input("> [Press enter]")
    print("Cook: You've brought me everything I need! I am saved! Thank you!")
    input("> [Press enter]")
    print("Player: So do I get to go to the Kings' Party?")
    input("> [Press enter]")
    print("Cook: I'm afraid not, only the big cheeses get to dine with the King.")
    input("> [Press enter]")
    print("Player: Well, maybe one day I'll be important enough to sit on the Kings' table.")
    input("> [Press enter]")
    print("Cook: Maybe, but I won't be holding my breath.")
    endQuest(0)


hasFlour = False
hasMilk = False 
hasEggs = False

   
start()