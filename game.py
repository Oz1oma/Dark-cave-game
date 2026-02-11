import time
import random
inventory=[]
def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()    

def intro():
    slow_print("Welcome to Dark Cave Adventure!\n")
    name=input("Can i get your name, you brave explorer?'_' ")
    slow_print(f"Hello {name}. You find yourself standing at the mouth of a dark cave....")
    time.sleep(1)
    choice1(name)

def choice1(name):
    slow_print("Do you want to ENTER the cave or RUN away?")
    choice=input("Type 'enter' or 'run': ").lower()

    if choice == 'enter':
        slow_print("You barely step into the darkness..\n")
        find_item()
        choice2(name)
    elif choice == 'run':
        slow_print("You run away safely but you'll never know what could've been. GAME OVER....")
    else:
        slow_print("I didn't understand that.")
        choice1(name)

def choice2(name):
    slow_print("Inside, you see two tunnels: one to the LEFT and one on the RIGHT.")
    decision=input("Type 'left' or 'right': ").lower()

    if decision=="left":
        slow_print("Oh no! You walked straight into a pit of snakes!")
        slow_print("You're out of the game.")
        slow_print("GAME OVER!")    
    elif decision=='right':
        slow_print("You find a chest with gold!")
        combat()
        slow_print(f"Congratulations, {name}! You win!")
    else:
        slow_print("Try again...") 
        choice2(name)      

def find_item():
    chances=random.randint(2,12)
    if chances<5:
        slow_print("You've found a rusty sword on the ground.")
        sword_choice=input("Do you want to pick it up?(yes/no) ").lower()
        if sword_choice=="yes":
            inventory.append("sword")
            print("You picked up the sword")
        else:    
            print("You've left the sword behind.")
    elif chances>5 and chances<10:
        slow_print("You've found a torchlight.")
        torch_choice=input("Do you want to pick it up?(yes/no) ").lower()
        if torch_choice=="yes":
            inventory.append("torch")
            print("You've picked up the torch.")
        else:
            print("You've left the torch behind.")
    else:
        slow_print("You've found a key")
        key_choice=input("Do you want to pick it up?(yes/no) ").lower()
        if key_choice=="yes":
            inventory.append("key")
            print("You.ve picked up the key.")
        else:
            print("You've left the key behind.")


def combat():
    slow_print("\nA wild monster starts appearing in front of you...")
    if "sword" in inventory:
        slow_print("You draw your sword and fight bravely...")
        print("You've defeated the moster")
    else:
        chance=random.randint(2,9)
        if chance<4:
            slow_print("You've successfully defeated the monster by a random luck")
        else:
            print("The monster defeats you...Game over!")
            
intro()   
