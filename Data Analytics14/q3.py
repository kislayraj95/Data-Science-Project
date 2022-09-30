import random
import sys

players = []

def start():
    global players
    choice = int(input("Enter no of players: "))
    if choice <= 1:
        print("Please enter atleast 2 players")
        start()
    else:
        players = getPlayers(choice)
        operators = ['+','-']

        print(players)
        print()

        for i in range(0,100):
            print("-- Level {} --".format(i+1))
            start_level(level=1, operator=operators[int(i/4)])


def getExpression(level, operator):
    num1=0
    num2=0
    ans=0
    if level == 1:
        num1 = random.randint(0,10)
        num2 = random.randint(1,10)
        eq = "{} {} {}".format(num1,operator,num2)
        ans = eval(eq)
        return eq,ans
    else:
        num1 = random.randint(10,500)
        num2 = random.randint(10,500)
        eq = "{} {} {}".format(num1,operator,num2)
        ans = eval(eq)
        return eq,ans

def getPlayers(no):
    players_ = []
    initial = 65
    for i in range(no):
        players_.append(chr(initial))
        initial += 1
    return players_


def count_eliminated_players():
    count = 0
    for p in players:
        if p == 'Eliminated!':
            count = count + 1
    return count


def get_players_for_next_level():
    plyers = []
    for p in players:
        if p != 'Eliminated!':
            plyers.append(p)
    return plyers


def start_level(level,operator):
    global players
    eliminited_players = []
    for i in range(0,len(players)):
        p = players[i]
        eq,ans = getExpression(1,operator)
        print()
        player_ans = int(input("Player {}, {} = : ".format(p,eq)))
        if player_ans == ans:
            print("Correct!")
        else:
            print("Incorrect! Player {} eliminated.".format(p))
            eliminited_players.append(players[i])
            players[i] = "Eliminated!"
    if count_eliminated_players() == len(players):
        players = eliminited_players
        print("Players {} will challange same level 2 again.".format(eliminited_players))
    else:             
        print("Players {} progress to the level {}".format(get_players_for_next_level(), level+1))
        players = get_successfull_players()
    
    if len(players) == 1:
        print("Player {} is the winner!".format(players[0]))
        sys.exit()    

def get_successfull_players():
    successfull_players = []
    for player in players:
        if player != 'Eliminated!':
            successfull_players.append(player)
    return successfull_players


if __name__ == '__main__':
    start()

# Problem in when all players enter the incorrect ans, and now they need to play
# that level again. getting results ['Eliminated!','Eliminated!'] instead of [A,B]