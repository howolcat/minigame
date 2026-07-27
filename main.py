from lotto import lotto_game
from RSP import rsp_game
from up_down import up_downgame
from zero import zero_game



while True:
    print(''' =====미니게임=====
    1번: 로또뽑기!
    2번: 가위바위보!
    3번: UP! DOWN!
    4번: zero game!
    5번: 종료
    ''')
    choice = input("뭐할까?(1~5) :")
    if choice == "1" :
        lotto_game()
    elif choice == "2" :
        rsp_game()
    elif choice == "3" :
        up_downgame()
    elif choice == "4" :
        zero_game()
    elif choice == "5" :
        print("bye~")
        break