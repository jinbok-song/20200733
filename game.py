for i in range(3):
    print("갤러그 게임 시작")
    print("적 비행기 발생")
    print("1. 발사  2. 오른쪽 이동  3. 왼쪽 이동")
    number = int(input("숫자를 입력하세요 : "))
    print("당신의 입력값?", number)

    # 1번을 입력하면 총알 발사
    if number == 1 :
        print("------------")
        print("총알 발사")
        print("------------")
    # 2번을 입력하면 오른쪽 이동
    if number == 2 :
        print("------------")
        print("오른쪽 이동")
        print("------------")
    # 3번을 입력하면 왼쪽 이동
    if number == 3 :
        print("------------")
        print("왼쪽 이동")
        print("------------")