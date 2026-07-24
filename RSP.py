import random

def rsp_game() :

    hands = ["가위", "바위", "보"]

    while True:
        x = input("나랑 가위바위보 할래?(y/n)")
        if x == "y" or x == "Y":
            while True:
                friend = hands[random.randint(0, 2)]
                player = input("뭘 낼까?(가위,바위,보) :")

                if player not in hands:
                    print("어... 그런게 있었나..? 다시 생각해보자.")
                    continue

                print(f"친구 :{friend} / 나 :{player}")
                if player == friend :
                    print("비겼어 다시해!")
                    continue
                elif player == "가위" and friend == "보":
                    print("이겼다!")
                elif player == "바위" and friend == "가위":
                    print("이겼다!")
                elif player == "보" and friend == "바위":
                    print("이겼다!")
                else:
                    print("내가 졌어...")
                break
        elif x == "n" or x == "N":
            print("알았어 다음에보자~")
            break
        else :
            print("하자는거야 말자는거야...?")





