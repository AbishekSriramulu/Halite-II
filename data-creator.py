import os
import time

ship_requirement = 10
damage_requirement = 1000


def get_ships(data):
    return int(data.split("producing ")[1].split(" ships")[0])


def get_damage(data):
    return int(data.split("dealing ")[1].split(" damage")[0])


def get_rank(data):
    return int(data.split("rank #")[1].split(" and")[0])


player_1_wins = 0
player_2_wins = 0

for num in range(5000):
    try:
        print("Currently on: {}".format(num))
        if player_1_wins > 0 or player_2_wins > 0:
            p1_pct = round(player_1_wins / (player_1_wins + player_2_wins) * 100.0, 2)
            p2_pct = round(player_2_wins / (player_1_wins + player_2_wins) * 100.0, 2)
            print("Player 1 win: {}%; Player 2 win: {}%.".format(p1_pct, p2_pct))

        os.system('halite.exe -d "360 240" "python MyBot.py" "python MyBot2.py" >> data.gameout')

        with open('data.gameout', 'r') as f:
            contents = f.readlines()
            AbishekSriramulu1 = contents[-4]
            AbishekSriramulu2 = contents[-3]
            print(AbishekSriramulu1)
            print(AbishekSriramulu2)

            AbishekSriramulu1_ships = get_ships(AbishekSriramulu1)
            AbishekSriramulu1_dmg = get_damage(AbishekSriramulu1)
            AbishekSriramulu1_rank = get_rank(AbishekSriramulu1)

            AbishekSriramulu2_ships = get_ships(AbishekSriramulu2)
            AbishekSriramulu2_dmg = get_damage(AbishekSriramulu2)
            AbishekSriramulu2_rank = get_rank(AbishekSriramulu2)

            print("AbishekSriramulu1 rank: {} ships: {} dmg: {}".format(AbishekSriramulu1_rank, AbishekSriramulu1_ships, AbishekSriramulu1_dmg))
            print("AbishekSriramulu2 rank: {} ships: {} dmg: {}".format(AbishekSriramulu2_rank, AbishekSriramulu2_ships, AbishekSriramulu2_dmg))

        if AbishekSriramulu1_rank == 1:
            print("c1 won")
            player_1_wins += 1
            if AbishekSriramulu1_ships >= ship_requirement and AbishekSriramulu1_dmg >= damage_requirement:
                with open("c1_input.vec", "r") as f:
                    input_lines = f.readlines()
                with open("train.in", "a") as f:
                    for l in input_lines:
                        f.write(l)

                with open("c1_out.vec", "r") as f:
                    output_lines = f.readlines()
                with open("train.out", "a") as f:
                    for l in output_lines:
                        f.write(l)

        elif AbishekSriramulu2_rank == 1:
            print("c2 won")
            player_2_wins += 1
            if AbishekSriramulu2_ships >= ship_requirement and AbishekSriramulu2_dmg >= damage_requirement:
                with open("c2_input.vec", "r") as f:
                    input_lines = f.readlines()
                with open("train.in", "a") as f:
                    for l in input_lines:
                        f.write(l)

                with open("c2_out.vec", "r") as f:
                    output_lines = f.readlines()
                with open("train.out", "a") as f:
                    for l in output_lines:
                        f.write(l)

        time.sleep(2)
    except Exception as e:
        print(str(e))
        time.sleep(2)