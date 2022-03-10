from LinkedList import LinkedList
from restaurantData import types, restaurant_data

#Hello message:
def hello():
    #No input, no return. Only prints welcome message.
    print("")
    print("             *****************")
    print("*************")
    print("             *****************")
    print("Welcome to SoHo Restaurants!")
    print("             *****************")
    print("*************")
    print("             *****************")
    print("")


#To find appropriate restaurant options:
def pattern_search(list, pattern):
    result=[]
    for text in list:
        if pattern == text[0:len(pattern)]:
            result.append(text)
    return result

#If the only one available pattern, this function will be called from ask_question function.
def only_option(list):
    choice = input("The only option with those beginning letters is '{0}'. Do you want to look at {1} restaurants? Enter 'y' for yes and 'n' for no: ".format(list[0],list[0]))
    if choice == 'y' or choice == "Y":
        return True
    else:
        return False

#If the user press 'y' or "Y". Program will give one more chance to ask.
def again():
    choice = input("Do you want other restaurants? Enter 'y' for yes and 'n' for no.")
    if choice == 'y' or choice =="Y":
        print("")
        ask_question()
        
    
def ask_question():
    #It asks question and then takes input.
    #This input is the return of this function.
    print("What type of food would you like to eat?")
    choice = input("Type the beginning of that food type and press enter to see if its here:")
    option_list = pattern_search(types, choice)
    #If option_list has one element.
    if len(option_list) == 1:
        if(only_option(option_list)):
            #If this option is correct then print the result.
            print(f"The {option_list[0]} restaurants in Soho:")
            dictionary[option_list[0]].stringify_list()
            print("")
            again()
        else:
            #If this option is wrong, program will wait for new input.
            ask_question()
    else:
        #If there are more than one option.
        print(f"With those beginning letters , your choices are {option_list}")
        print("")
        ask_question()

#Restaurant Types:
german = LinkedList()
japanese = LinkedList()
vegetarian = LinkedList()
french = LinkedList()
african = LinkedList()
american = LinkedList()
barbecue = LinkedList()
czech = LinkedList()
chinese = LinkedList()
thai = LinkedList()
mexican = LinkedList()
indian = LinkedList()
cafe = LinkedList()
pizza = LinkedList() 
italian = LinkedList()

#Restaurant type dictionary:
dictionary = {"german":german, "japanese": japanese, "vegetarian": vegetarian, "french": french, "african":african, "american":american, "barbecue":barbecue, "czech":czech, "chinese":chinese, "thai": thai, "mexican":mexican, "indian": indian, "cafe":cafe, "pizza":pizza, "italian":italian   }

#Restaurant Informations:
for data in restaurant_data:
    dictionary[data[0]].insert(data[1],data[2],data[3],data[4])

#Function:
hello()
ask_question()


