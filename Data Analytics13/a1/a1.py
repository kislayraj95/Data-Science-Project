"""
Wordle

"""

from operator import le
from string import ascii_lowercase
from typing import Optional

from a1_support import (
    load_words,
    choose_word,
    VOCAB_FILE,
    ANSWERS_FILE,
    CORRECT,
    MISPLACED,
    INCORRECT,
    UNSEEN,
)




# Add your functions here

def match_words(guess, original):
    ans_cols = ""
    if len(guess) == len(original):
        for i in range(len(guess)): 
            if guess[i] == original[i]:
                ans_cols += "🟩"
            elif original.__contains__(guess[i]) and guess[i] != original[i]:
                ans_cols += "🟨"
            else:
                ans_cols += "⬛"
        return ans_cols
    else:
        return None

def print_dict(dic):
    for i,j in dic.items():
        print(i+" ",j)        

def merge_key_vals(dic):
    lst = []
    for i,j in dic.items():
        lst.append(str(i)+" : "+j)
    return lst

def keyboard_info(original):
    print("Keyboard information")
    print("------------")
    dic1 = {"a":"⬛","c":"⬛","e":"⬛","g":"⬛","i":"⬛","k":"⬛","m":"⬛",
    "o":"⬛","q":"⬛","s":"⬛","u":"⬛","w":"⬛","y":"⬛","b":"⬛","d":"⬛",
    "f":"⬛","h":"⬛","j":"⬛","l":"⬛","n":"⬛","p":"⬛","r":"⬛","t":"⬛",
    "v":"⬛","x":"⬛","z":"⬛"}
    
    for i in original: 
        dic1[i] = "🟩"
    
    res1 = merge_key_vals(dict(list(dic1.items())[len(dic1)//2:]))
    res2 = merge_key_vals(dict(list(dic1.items())[:len(dic1)//2]))

    for i in range(len(res1)):
        print(res2[i]+"\t"+res1[i])
    



def main():
    words = load_words("answers.txt")
    games_won = {"1 moves":0,"2 moves":0,"3 moves":0,"4 moves":0,"5 moves":0,"6 moves":0, "Games lost":0}

    while True:
        current_word = choose_word(words)
        guess_no = 1
        while True:
            if guess_no <= 6:
                print("---------------")
                guess = input("Enter guess {}: ".format(guess_no))
                if guess == "k":
                    keyboard_info(current_word)
                else:
                    ans = match_words(guess, current_word)
                    if ans is not None:
                        print("\t\t{}".format(ans))
                        if ans == len(ans) * "🟩":
                            print("Correct! You won in {} guesses!".format(guess_no))
                            games_won["{} moves".format(guess_no)] = games_won["{} moves".format(guess_no)] + 1
                            print_dict(games_won)
                            break
                        print("")
                        guess_no += 1
                    else:
                        print("Lenght of the guess does not match with the original word!")
            else:
                print("You lose! The answer was: {}".format(current_word))
                games_won["Games lost"] = games_won["Games lost"] + 1
                print_dict(games_won)
                break
        choice = input("Would you like to play again (y/n)? ")
        if choice == "y":
            guess_no = 0
            continue
        else:
            break


def has_won(guess: str, answer: str) -> bool:
    if len(guess) == 6 and len(answer) == 6:
        if guess == answer:
            return True
    return False

def has_lost(guess_number: int) -> bool:
    if guess_number >= 6:
        return True
    return False

if __name__ == "__main__":
    main()