import random

def lotto_game():

    money = 10000

    while True:
        x = input("로또나 한번 뽑아 볼까...?(y/n)")
        print(f"현재 돈{money}")
        if money == 0:
            print("돈이 없다....")
            break
        elif x == "y" or x == "Y":
            money -= 1000
            lotto_num = random.sample(range(1, 51), 5)
            player_num = list(map(int,input("1~50 까지 숫자를 5개 적으시오").split()))
            if len(set(player_num)) != 5 :
                print("복권 용지로 장난치거나 실수하는건 안봐주더라...")
                continue

            match_num = len(set(lotto_num) & set(player_num))
            if match_num == 2 :
                print("4등이다...")
                money += 1000
            elif match_num == 3 :
                print("3등이다...")
                money += 5000
            elif match_num == 4 :
                print("2등이다...!")
                money += 10000
            elif match_num == 5 :
                print("1등이다!!!!!!!!!!")
                money += 100000000
        elif x == "n" or x == "N":
            print("집에가자...")
            break



