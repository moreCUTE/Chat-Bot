import random
import sys
import functools

def any_word_in_string(words: list[str], string: str) -> bool:
    for word in words:
        if word in string:
            return True
    return False

print("Welcome to Mo's Chatbot. What's on your mind today?")
doExit = False

Im_list = ["I'm","i'm","im","Im"]
family = ["dad", "Dad","mom", "Mom","brother", "Brother","Sister","sister"]
greeting = ["hi","hello","hoddy","wasup", "wasgood", "wagwan", "sup"]

list_of_good_emotions = []
with open("DC23-04-24_chatBot/good_emotions.txt") as read_file:
    for i in range(90):
        list_of_good_emotions.append(read_file.readline().rstrip().lower())

list_of_bad_emotions = []
with open("DC23-04-24_chatBot/bad_emotions.txt") as read_file:
    for i in range(164):
        list_of_bad_emotions.append(read_file.readline().rstrip().lower())

list_of_pets = []
with open("DC23-04-24_chatBot/pets.txt") as read_file:
    for i in range(43):
        list_of_pets.append(read_file.readline().rstrip().lower())
    

while doExit == False:
    choice = input()
    if choice == "quit":
        doExit = True
        break



    #listen and respond to feelings
    if any_word_in_string(greeting, choice):
        ran = random.randint(0,len(greeting))
        print(greeting[ran])
    if any_word_in_string(list_of_bad_emotions, choice):
        print("I'm sorry to hear you're feeling that way.")
    elif any_word_in_string(list_of_good_emotions, choice):
        print("That's great!")
    elif any_word_in_string(Im_list, choice): #these next three lines let you repeat the word after "I'm" back in a sentence
        word_list = choice.split(" ") #break the sentence into a list with one word per slot
        next_word = " "
        for i, word in enumerate(word_list):
            if word in Im_list:
                next_word = word_list[i+1] #find the word after "I'm"
            if next_word == "a":
                next_word = "a" + word_list[i+2]
        else:
            print("Why are you", next_word+ "?")
                #repeat it back 
        #NOTE: it would be good to add an if statement here checking if the next word was "a" 
        #so if someone says "I'm a frog", it doesn't say back, "Why are you a?"

    #listen and respond to specific topics
    elif any_word_in_string(family, choice):
        print("Tell me more about your family.")

    elif any_word_in_string(list_of_pets, choice):
        print("I'd like to hear more about this pet.")

    else: #randomize last statement so it's not too repetetive 
        num = random.randrange(1, 100)
        if num <50:
            print("Can you tell me more?")
        else:
            print("What does that suggest to you?")
