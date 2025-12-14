# computer_games program
#
computer_games = [
    "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
    "League of Legends", "Valorant", "Grand Theft Auto V",
    "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

computer_games.sort()
i = 0
number = 1

print("--- Sorted Computer Games List ---")

while i < len(computer_games):
    
    game_name = computer_games[i]
    print(f"{number}. {game_name}")
    i = i + 1
    number = number + 1