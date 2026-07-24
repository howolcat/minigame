import random

def up_downgame():
    while True:
        x = input("나랑 게임하나 할래?(y/n)")
        if x == "y" or x == "Y":
            f_ans = (int(random.randint(1, 51)))
            while True:
                p_ans = int(input("뭐라고 할까?(1~50)"))
                if p_ans == f_ans:
                    print("정답이야!")
                    break
                elif p_ans > 50 :
                    print("DOWN! 내가 1부터 50이라고 말 안했던가...?")
                elif p_ans > f_ans:
                    print("DOWN!")
                else :
                    print("UP")



        elif x == "n" or x == "N":
            print("알았어 다음에보자~")
            break
        else:
            print("하자는거야 말자는거야...?")