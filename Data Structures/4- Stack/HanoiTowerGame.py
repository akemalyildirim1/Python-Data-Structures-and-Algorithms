from Stack import Stack
"""
At the beginning of the game, all disks are placed in to the left stack.
And the game will end when the all disks are came to the right stack.
"""

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
#Every stacks are initilaized here and then they are appended to a list called stacks.
stacks=[]
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks+=[left_stack,middle_stack,right_stack]


#Set up the Game
#If the number of the disk is less than 3, hanoi tower will be meaningless.
num_disks=int(input("\nHow many disks do you want to play with?\n"))
while num_disks<3:
  num_disks=int(input("Enter a number greater than or equal to 3\n"))

for i in range(num_disks,0,-1):
  #all disks are pushed into the left stackfrom stack import Stack
  left_stack.push(i)
print("\nLet's play Towers of Hanoi!!")

#Get User Input
def get_input():
  #We only want the first letter of the stack names.
  choices = [stack.get_name()[0] for stack in stacks]
  #stack.get_name gives "left", "Middle", "Right". But we want to get "L" "M" "R"

  while True:
    #firstly users need to know their options 
    for i in range(len(stacks)):
      name=stacks[i].get_name()
      letter=choices[i]
      print(f"Enter {name} for {letter}")
    user_input=input("")

    if user_input in choices:
      #if the input is correct then the function return the chosen stack
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]
      
        
#Play the Game

num_user_moves=0
#to compare the performance of the user with optimal move number, program stored the move number of the player
while right_stack.get_size() != num_disks:
  #when the all disks came to the right disk, loop will end.
  print("\n\n\n...Current Stacks...")
  for stack in stacks:
    #player need to see the  current place of the disks
    print(stack.print_items())
  
  while True:
    #this part is about the interaction between user input and program
    print("\nWhich stack do you want to move from?\n")
    from_stack=get_input()
    print("\nWhich stack do you want to move to?\n")
    to_stack=get_input()
    #program needs to understand whether input is correct or not.
    #due to get_input function, it can understand.
    
    if from_stack.is_empty():
      print("\n\nInvalid Move. Try Again")
      
    elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
      disk=from_stack.pop()
      to_stack.push(disk)
      num_user_moves+=1
      break
      
    else:
      print("\n\nInvalid Move. Try Again")
  
print(f"\n\nYou completed the game in {num_user_moves} moves, and the optimal number of moves is {num_optimal_moves}")
  left_stack.push(i)

