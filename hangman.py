from time import sleep
import random
from colorama import Fore

"רשימת מילים"
animal = {"dog", "cat", "fish", "chicken"}
# הוצאה של מילה מהרשימה
secret_word = animal.pop()


def is_valid_input(Guess_a_letter1, old_letters):
    Continued1 = "V"
    if Guess_a_letter1.isalpha() is False and len(Guess_a_letter1) > 1:
        print(Fore.RED + "\nE3")
        Continued1 = "X"
    elif Guess_a_letter1.isalpha() is False:
        print(Fore.RED + "\nE2")
        Continued1 = "X"
    elif len(Guess_a_letter1) > 1:
        print(Fore.RED + "\nE1")
        Continued1 = "X"
    else:
        if Guess_a_letter1 in old_letters:
            print(Fore.RED + "\nYou already entered this signal, try again")
            Continued1 = "X"
        else:
            old_letters_guessed.append(Guess_a_letter1)
    return Continued1


"פונקציה שמשנה את אורך המילה לרשימה חדשה בלי האותיות"


def show_hidden_word(number):
    LIST = list(range(0, number))
    for i in range(len(LIST)):
        LIST[i] = "_"
    return LIST


"פונקציה להדפסת האיש תלוי בשלבי המשחק לפי מספר הפסילות"


def print_hangman(n):
    picture = n

    if picture == 1:
        print(Fore.BLACK + "x-------x")

    elif picture == 2:
        print(Fore.BLACK + """
        x-------x
        |
        |
        |
        |
        |""")

    elif picture == 3:
        print(Fore.BLACK + """
        x-------x
        |       |
        |       0
        |
        |
        |""")

    elif picture == 4:
        print(Fore.BLACK + """
        x-------x
        |       |
        |       0
        |       |
        |
        |""")
    elif picture == 5:
        print(Fore.BLACK + r"""
        x-------x
        |       |
        |       0
        |      /|\
        |
        |""")

    elif picture == 6:
        print(Fore.BLACK + r"""
        x-------x
        |       |
        |       0
        |      /|\
        |      /
        |""")

    elif picture == 7:
        print(Fore.BLACK + r"""
        x-------x
        |       |
        |       0
        |      /|\
        |      / \
        |

        you lose """)


def menu(number_of_tries, number_of_secret_word):
    # "לולאה while שלא מפסיקה עד ש-count = max_tries"
    while number_of_tries != MAX_TRIES:
        # בדיקה של אורך המילה הזוכה
        # בשביל לראות אם השחקן ניצח ויכול לצאת מהלולאה
        if number_of_secret_word == len(secret_word):
            print("\nyou win")
            break

        print(Fore.BLUE + "\n", " ".join(secret_List))
        print("The letters you used:", old_letters_guessed)
        # קבלת אות מהמשתמש
        letter_guessed = input("enter Letter: ").lower()
        Continued = is_valid_input(letter_guessed, old_letters_guessed)
        if Continued == "X":
            continue
        if letter_guessed in List_Word_Win:
            # בדיקה שהמשתמש לא לחץ על אותה אות פעמים
            if letter_guessed in secret_List:
                print(Fore.RED + "\nYou already entered this signal, try again")
                continue
            # בדיקה אם האות נכונה נכניס אותה לרשימה שיצרנו בלי האותיות
            for i in range(len(List_Word_Win)):
                if List_Word_Win[i] == letter_guessed:
                    secret_List[i] = letter_guessed
                    number_of_secret_word += 1
        # אם לא נוסיף פסילה לרשימת הפסילות
        else:
            number_of_tries += 1
            print_hangman(number_of_tries)


"השתמשתי randint למספר קבוע למי שירצה לשנות את המשתנה ללא קבוע יכול לעשות את זה בקלות"
"A_number_of_failures = random.randint(5, 10) למשל כך"
"מספר הפסילות של שיש השחקן - A_number_of_failures"
MAX_TRIES = random.randint(7, 7)
"הדפסת המילה hangman + מס' פסילות "
HANGMAN_ASCII_ART = r"""
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |   
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
"""
print(HANGMAN_ASCII_ART, MAX_TRIES)
sleep(1)
"קבלת שם לשתמש"
name = input("\nHello what your name: ")
"הסבר על כמות מס' הפסילות במשחק"
print("\nHello " + name + " You  " + str(MAX_TRIES) + " attempts to guess for the win")
"הפחת המילה לרשימה"
List_Word_Win = list(secret_word)
"קבלת אורך המילה"
Length_Word_Win = len(List_Word_Win)
"קריאה לפונקציה show_hidden_word"
secret_List = show_hidden_word(Length_Word_Win)
"רשימה של מילים שהשחקן השתמש בהם"
old_letters_guessed = []
" סיפרה של הפסילות"
num_of_tries = 0
"הסיפרה של אורך המילה הזוכה"
num_of_secret_word = 0

menu(num_of_tries, num_of_secret_word)
