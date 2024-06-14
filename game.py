import random

turn = True

PLAYER_LOCATION = (0,0)
EXIT_LOCATION = (0,0)
MAP_SIZE = 0

movement_number = 0

l_0 = "Time is ticking... What do you do?\n"
l_1 = "The Python approaches... Move with haste!\n"
l_2 = "You hear a slither across the halls... A shiver passes down your spine...\n"
l_3 = "Your hands shiver in the emptiness of the halls... What do you do?\n"
l_4 = "All you see is darkness... The void surrounds you...\n"
l_5 = "Your fate draws near... What do you do?\n"

l_Choices = "Move: f - forward | b - Move back | l - Move left | r - Move right"

def main_menu():
    print("THE PYTHON")
    print("1 - Start Game")
    print("2 - Quit")
    choice = input("Choose an option: ")
    if choice == "1":
        get_difficulty() 
    elif choice == "2":
        quit()
    else:
        print("Invalid choice, please try again.")
        main_menu()

def game_start():
    PLAYER_LOCATION == (random.randint(-MAP_SIZE, MAP_SIZE), random.randint(-MAP_SIZE, MAP_SIZE))
    EXIT_LOCATION == (random.randint(-MAP_SIZE, MAP_SIZE), random.randint(-MAP_SIZE, MAP_SIZE))
    print("You wake up in a dark room... You can't remember how you got here...")
    print("Something is lurking in the shadows... You can feel it...")
    print("You must find your way out...")
    player_turn()

def get_difficulty():
    difficulty = input("Choose your map size: Easy, Medium, Hard\n")
    if difficulty.lower() == "easy":
        MAP_SIZE == 20
        game_start()
    elif difficulty.lower() == "medium":
        MAP_SIZE == 40
        game_start()
    elif difficulty.lower() == "hard":
        MAP_SIZE == 60
        game_start()
    else:
        print("Invalid difficulty, please try again.")
        get_difficulty()

def get_location():
    if PLAYER_LOCATION.x != +-MAP_SIZE.x and PLAYER_LOCATION.y != +-MAP_SIZE.y:
        l_Choices == "Move: f - Move forward | b - Move back | l - Move left | r - Move right"
        movement_number == 1
    elif PLAYER_LOCATION.x == -MAP_SIZE.x and PLAYER_LOCATION.y != +-MAP_SIZE.y:
        l_Choices == "Move: f - Move forward | b - Move back | l - Move left"
    elif PLAYER_LOCATION.x == MAP_SIZE.x and PLAYER_LOCATION.y != +-MAP_SIZE.y:
        l_Choices == "Move: f - Move forward | b - Move back | r - Move right"
    elif PLAYER_LOCATION.x != +-MAP_SIZE.x and PLAYER_LOCATION.y == -MAP_SIZE.y:
        l_Choices == "Move: f - Move forward | l - Move left | r - Move right"
    elif PLAYER_LOCATION.x != +-MAP_SIZE.x and PLAYER_LOCATION.y == MAP_SIZE.y:
        l_Choices == "Move: b - Move back | l - Move left | r - Move right"

def player_turn():
    global turn
    if turn:
        start_line = random.randint(0, 5)
        print(globals()["l_" + str(start_line)])
        print(l_Choices)
        turn = not turn

main_menu()