class Player:

    def __init__(self):
        pass

    @staticmethod
    def make_choice():
        choice = input("Please make a choice - R, P or S: ")
        if choice == "R":
            return 1
        elif choice == "P":
            return 2
        elif choice == "S":
            return 3
        else:
            return -1

    @staticmethod
    def make_move(player, cpu, options):
        choice = player.make_choice() - 1
        while choice < 0:
            print("Invalid choice!")
            choice = player.make_choice() - 1
        cpu1 = cpu.cpu_choice()
        print("Player ({}) : CPU ({})".format(options[choice], options[cpu1]))
        if options[choice] == options[cpu1]:
            return "draw"

        if options[choice] == "rock":
            if options[cpu1] == "scissors":
                return "win"
            else:
                return "loose"

        elif options[choice] == "paper":
            if options[cpu1] == "scissors":
                return "loose"
            else:
                return "win"

        else:
            if options[cpu1] == "paper":
                return "win"
            else:
                return "loose"
