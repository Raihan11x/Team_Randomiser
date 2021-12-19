from random import choice

players = []
file = open('players.txt')
players = file.read().splitlines()
print(players)

teams = []
file = open('teams.txt', 'r')
teams = file.read().splitlines()
print(teams)

teamA = []
teamB = []

while len(players) > 0:
    playerA = (choice(players))
    teamA.append(playerA)
    players.remove(playerA)

    if players == []:
        break

    playerB = (choice(players))
    teamB.append(playerB)
    players.remove(playerB)

print('''

Here are the teams:

''')

print('Team A:', teamA)
print('Team B:', teamB)