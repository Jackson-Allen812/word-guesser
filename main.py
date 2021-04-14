from bs4 import BeautifulSoup
import requests

# this is a simple game that picks a word from a list and asks the player to guess what it is
# the player has 5 guesses and each incorrect guess gives the player a clue
# the clues are, in order, description, number of letters, first letter, and last letter

def get_word():

    url = "https://randomword.com/"
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")

    word = soup.find("div", id="random_word").text
    description = soup.find("div", id="random_word_definition").text

    info = [word,
            description,
            word[0],
            word[-1],
            len(word)]

    return info


def game():
    
    game_loop = True
    attempts = 5

    info = get_word()

    while game_loop:

        if attempts == 5:
            print("I'm thinking of a word, can you guess what it is?\nThe description of the word is:\n" + info[1])
        elif attempts == 4:
            print("No, that wasn't right. Here's another hint, the number of letters in the word is: " + str(info[4]))
        elif attempts == 3:
            print("Nope, here's another hint. The first letter of the word is: " + info[2].capitalize())
        elif attempts == 2:
            print("You're almost out of guesses, so here's another hint. The last letter of the word is: " + info[3].capitalize())
        elif attempts == 1:
            print("This is your last guess, and there's no more hints. Think real hard about what it could be, and good luck.")
        elif attempts == 0:
            print("GAME OVER\nThe word was: " + info[0].capitalize())
            game_loop = False
            break
        
        guess = input("You have " + str(attempts) + " remaining: ")

        if guess.lower() != info[0].lower():
            attempts -= 1
        elif guess.lower() == info[0].lower():
            print("Congrats! That was the word!")
            game_loop = False



if __name__ == "__main__":
    game()
