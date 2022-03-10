from random import randrange, shuffle

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

def ask_question():
    #It asks question and then takes input.
    #This input is the return of this function.
    print("What type of food would you like to eat?")
    choice = input("Type the beginning of that food type and press enter to see if its here:")
    return choice

#Best sorting algorithm:
def quicksort(list, start, end):
    #If start is bigger than end, return function.(Base case for recursion)
    if start >=end:
        return 
    #Pivot is randomly selected because of considering the algorithms averge complexity
    pivot_idx = randrange(start, end+1)
    pivot_element = list[pivot_idx]
    #swap random element with last element in sub-lists
    list[end], list[pivot_idx] = list[pivot_idx], list[end]

    # tracks all elements which should be to left (lesser than) pivot
    less_than_pointer = start

    for i in range(start, end):
        #We need to loop for every single element
        if list[i] < pivot_element:
            # swap element to the right-most portion of lesser elements
            list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
            less_than_pointer+=1
    # move pivot element to the right-most portion of lesser elements
    list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
    quicksort(list, start, less_than_pointer - 1)
    quicksort(list, less_than_pointer + 1, end)
