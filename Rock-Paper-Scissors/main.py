from CPU import CPU
from Player import Player

cpu = CPU()

player = Player()

options = ["rock", "paper", "scissors"]

draw = True

while draw:
    result = player.make_move(player, cpu, options)
    if result == "win":
        print("The Player wins!")
        draw = False
    elif result == "loose":
        print("The Computer wins!")
        draw = False
