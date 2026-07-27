


#제로 게임

import random

def zero_game():
    while True:
        print("you won't play? (yes or no) :")  # 게임 참여 여부
        play =  input()
        if play == "no" :
            print("okay bye..")
            break
        elif play == "yes" :   # 게임 시작
            while True :                                     # 공, 수 정하기
                roll_num1 = random.randint(1, 6)
                roll_num2 = random.randint(1, 6)
                my_roll = random.randint(1, 6)
                print(f"친구1:{roll_num1}, 친구2:{roll_num2}, 나:{my_roll}")
                if my_roll == roll_num1 or my_roll == roll_num2 :        # 같은게 하나라도 나오면 다시
                    print("roll again!")
                elif my_roll < roll_num1 and my_roll < roll_num2:        # 공격 턴

                    print("Attack!")
                    while True:
                        num1 = random.randint(0, 5)
                        num2 = random.randint(0, 5)
                        ans = int(input())
                        x = num1 + num2
                        if ans == x:
                            print(x)
                            print("Win!")                                # 공격 승리!
                            break
                        else:
                            print(x)
                            print("Wrong!")                              # 다시 공격
                    break

                elif my_roll > roll_num1 and my_roll > roll_num2:        # 수비 턴
                    print("Defense!")
                    while True:
                        num1 = random.randint(0, 5)
                        num2 = int(input())
                        frind_ans = random.randint(0, 5)
                        x = num1 + num2
                        if frind_ans == x:
                            print(x)
                            print(frind_ans)
                            print("NOoooo~..")                           # 방어 실패
                            break
                        else:
                            print(x)
                            print(frind_ans)
                            print("again!")                              # 방어 성공!
                    break








