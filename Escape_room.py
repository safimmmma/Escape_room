import time
from colorama import Fore, Style, init

# Initialize colorama for colored text
init(autoreset=True)

def print_header():
    print(Fore.CYAN + r"""
   ____                            _   _       _   _                 
  / ___|_   _ _ __   ___ _ __     | \ | | ___ | |_(_)_ __   __ _ ___ 
 | |  _| | | | '_ \ / _ \ '__|____|  \| |/ _ \| __| | '_ \ / _` / __|
 | |_| | |_| | |_) |  __/ | |_____| |\  | (_) | |_| | | | | (_| \__ \
  \____|\__,_| .__/ \___|_|       |_| \_|\___/ \__|_|_| |_|\__, |___/
             |_|                                           |___/     
    """)
    print(Fore.YELLOW + "Welcome to the Number Wizard's Tower! 🏰🔢")
    print(Fore.YELLOW + "Solve the puzzles to escape before the wizard returns!\n")

def print_puzzle_header(puzzle_number, title):
    print(Fore.MAGENTA + f"\n🔒 Puzzle {puzzle_number}: {title}")
    print(Fore.MAGENTA + "=" * (len(title) + 14) + "\n")

def print_correct():
    print(Fore.GREEN + "✅ Correct! You're one step closer to escaping...\n")

def print_wrong():
    print(Fore.RED + "❌ Wrong answer! Try again or type 'hint' for a clue.\n")

def escape_room():
    print_header()
    start_time = time.time()  # Start the timer

    # Puzzle 1: Number Riddle
    print_puzzle_header(1, "The Enchanted Lock")
    print(Fore.WHITE + "I am a three-digit number. My hundreds digit is the square root of 16.")
    print(Fore.WHITE + "My tens digit is the product of my ones digit and 3.")
    print(Fore.WHITE + "The sum of all my digits is 14. What number am I?")
    while True:
        answer1 = input(Fore.CYAN + "Your answer: ").strip()
        if answer1 == "452":
            print_correct()
            break
        elif answer1.lower() == "hint":
            print(Fore.BLUE + "💡 Hint: The hundreds digit is 4 (since √16 = 4). The sum of all digits is 14.")
        else:
            print_wrong()

    # Puzzle 2: Algebra & Logic
    print_puzzle_header(2, "The Hidden Chest")
    print(Fore.WHITE + "Three coins sum to 42. The first coin is half the second,")
    print(Fore.WHITE + "and the third is 6 more than the second. What is the second coin's value?")
    while True:
        answer2 = input(Fore.CYAN + "Your answer: ").strip()
        if answer2 == "12":
            print_correct()
            break
        elif answer2.lower() == "hint":
            print(Fore.BLUE + "💡 Hint: Let the second coin be x. Then, the first coin is x/2, and the third is x + 6. Their sum is 42.")
        else:
            print_wrong()

    # Puzzle 3: Geometry
    print_puzzle_header(3, "The Shifting Tiles")
    print(Fore.WHITE + "I am a quadrilateral with only one pair of parallel sides.")
    print(Fore.WHITE + "My smallest area is 24 square units, with a height of 6.")
    print(Fore.WHITE + "What is my average base length?")
    while True:
        answer3 = input(Fore.CYAN + "Your answer: ").strip()
        if answer3 == "8":
            print_correct()
            break
        elif answer3.lower() == "hint":
            print(Fore.BLUE + "💡 Hint: The shape is a trapezoid. Area = (average base length) × height.")
        else:
            print_wrong()

    # Puzzle 4: Number Sequence
    print_puzzle_header(4, "The Magic Portal")
    print(Fore.WHITE + "3, 6, 11, 18, __, 38. What is the missing number?")
    while True:
        answer4 = input(Fore.CYAN + "Your answer: ").strip()
        if answer4 == "27":
            print_correct()
            break
        elif answer4.lower() == "hint":
            print(Fore.BLUE + "💡 Hint: Look at the differences between the numbers: 3, 5, 7, 9, ...")
        else:
            print_wrong()

    # Calculate time taken
    end_time = time.time()
    total_time = int(end_time - start_time)
    print(Fore.GREEN + f"\nCongratulations! You've escaped the Number Wizard's Tower in {total_time} seconds! 🎊")
    print(Fore.YELLOW + r"""
   _____                         _       _ 
  |  __ \                       | |     | |
  | |  \/ __ _ _ __ ___   ___   | | __ _| |
  | | __ / _` | '_ ` _ \ / _ \  | |/ _` | |
  | |_\ \ (_| | | | | | |  __/  | | (_| | |
   \____/\__,_|_| |_| |_|\___|  |_|\__,_|_|
    """)

# Start the game
escape_room()