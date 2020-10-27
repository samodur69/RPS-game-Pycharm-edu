import random as r


def process_result(result, string, score):
    if result == 'win':
        score += 100
        print(f'Well done. The computer chose {string} and failed')
    elif result == 'lose':
        print(f'Sorry, but computer chose {string}')
    else:
        score += 50
        print(f'There is draw ({string})')
    return score


def game_mechanic(comp, user):
    # dic: key - choice, value - key beat that options
    game_beats = {
        "rock": ["fire", "scissors", "snake", "human", "tree", "wolf", "sponge"],
        "fire": ["scissors", "snake", "human", "tree", "wolf", "sponge", "paper"],
        "scissors": ["snake", "human", "tree", "wolf", "sponge", "paper", "air"],
        "snake": ["human", "tree", "wolf", "sponge", "paper", "air", "water"],
        "human": ["tree", "wolf", "sponge", "paper", "air", "water", "dragon"],
        "tree": ["wolf", "sponge", "paper", "air", "water", "dragon", "devil"],
        "wolf": ["sponge", "paper", "air", "water", "dragon", "devil", "lightning"],
        "sponge": ["paper", "air", "water", "dragon", "devil", "lightning", "gun"],
        "paper": ["air", "water", "dragon", "devil", "lightning", "gun", "rock"],
        "air": ["water", "dragon", "devil", "lightning", "gun", "rock", "fire"],
        "water": ["dragon", "devil", "lightning", "gun", "rock", "fire", "scissors"],
        "dragon": ["devil", "lightning", "gun", "rock", "fire", "scissors", "snake"],
        "devil": ["lightning", "gun", "rock", "fire", "scissors", "snake", "human"],
        "lightning": ["gun", "rock", "fire", "scissors", "snake", "human", "tree"],
        "gun": ["rock", "fire", "scissors", "snake", "human", "tree", "wolf"]
        }
    if comp in game_beats[user]:
        return 'win'
    elif comp == user:
        return 'draw'
    else:
        return 'lose'


def process_input(act):
    if act not in choice and act != ('!exit' and '!rating'):
        print("Invalid input")
    return act


def hello():
    user = input('Enter your name:\n')
    print(f'Hello, {user}')
    return user


def read_from_file(user, score):
    f = open('rating.txt', 'r', encoding='utf-8')
    for line in f:
        line = line.replace('\n', '').split()
        if line[0] == user:
            score = int(line[1])
    f.close()
    return score


# main hello and run game
score_live = 0
username = hello()
score_live = read_from_file(username, score_live)
choice = input().split(',')
# if no input of choice - use standard options
if not choice[0]:
    choice = ['rock', 'paper', 'scissors']
print("Okay, let's start")
# main script
while True:
    computer_choice = r.choice(choice)
    action = process_input(input())
    if action in choice:
        score_live = process_result(game_mechanic(computer_choice, action), computer_choice, score_live)
    elif action == '!rating':
        print(f'Your rating: {score_live}')
    elif action == '!exit':
        print('Bye!')
        break
