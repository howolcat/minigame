from lotto import lotto_game
from RSP import rsp_game
from up_down import up_downgame



while True:
    print(''' =====미니게임=====
    1번: 로또뽑기
    2번: 가위바위보!
    3번: UP! DOWN!
    4번: 나가기
    ''')
    choice = input("뭐할까?(1~4) :")
    if choice == "1" :
        lotto_game()
    elif choice == "2" :
        rsp_game()
    elif choice == "3" :
        up_downgame()
    elif choice == "4" :
        break