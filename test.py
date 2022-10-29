

user_guesses= True

grid=[
    "   _   ",
    " /   \ ",
    "   _   ",
    " \   / ",
    "  \ /  ",
    "   o   ",
    "  /|\  ",
    "  / \  "]

for i in grid:
    print(i)


while user_guesses:
    user_choice = input("y or n ?")
    if user_choice == "y" :
        for i in grid:
            print(i)

    elif user_choice == "n":
        user_guesses== False           
        grid.pop(0)
        
        for i in grid:
            print(i) 





