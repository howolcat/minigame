


#제로 게임

import random

def zero_game():
    while True:
        life = 7
        print("우리랑 같이 게임할래? (yes or no) :\n")  # 게임 참여 여부
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

                    print("Attack!\n")
                    while True:
                        if life == 0:
                            print("내가 졌어...")
                            break
                        num1 = random.randint(0, 5)
                        num2 = random.randint(0, 5)
                        ans = int(input())
                        x = num1 + num2
                        if ans > 10 or ans < 0:
                            print("제대로 해!!")
                        elif ans == x:
                            print(f"친구들 숫자합:{x}")
                            print("Win!\n")                                # 공격 승리!
                            break
                        else:
                            print(f"친구들 숫자합:{x}")
                            print("Wrong!\n")                              # 다시 공격
                            life -= 1
                    break

                elif my_roll > roll_num1 and my_roll > roll_num2:        # 수비 턴
                    print("Defense!")
                    while True:
                        if life == 0:
                            print("방어 성공!!")
                            break
                        num1 = random.randint(0, 5)
                        num2 = int(input())
                        friend_ans = random.randint(0, 5)
                        x = num1 + num2
                        if num2 > 5 or num2 < 0 :
                            print("장난 치지마!")
                        if friend_ans == x:
                            print(f"나의 합 :{x}")
                            print(f"친구의 합 :{friend_ans}")
                            print("NOoooo~..")                           # 방어 실패
                            break
                        else:
                            print(f"나의 합 :{x}")
                            print(f"친구의 합 :{friend_ans}")
                            print("again!")   # 방어 성공!
                            life -= 1
                    break
        else :
            print("할거야 말거야?")







