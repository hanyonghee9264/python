from friends.chat import send_message

def send_message():
    while True:
        choice = input('1: 친구명을 입력해주세요\n'
        '2: 메세지를 입력해주세요\n'
        '3: 프로그램을 실행합니다\n'
        '4: 프로그램 종료합니다\n'
        'input : ')
        if choice == '1':
            print('1번')
        elif choice == '2':
            print('2번')
        elif choice == '3':
            print('프로그램을 시작할께요!')
        elif choice == '4':
            break
