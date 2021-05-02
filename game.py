# 게임 설명 - 갤러그 게임
# 1. 적을 몇 마리 잡을 것인지 목표를 입력합니다. (함수사용)
# 2. 적 비행기의 위치를 알려주고 그에 맞는 대응을 한다. (리스트, 반복문 사용)
# 3. 대응이 올바른 경우와 잘못된 경우 다른 메시지를 띄워준다. (딕셔너리 사용)
# 4. 목표만큼 적을 잡고 대응이 끝난 후  평균대응 시간을 계산한 기록을 출력한다.  

# 기록 확인을 위한 선언
import time


# 목표를 입력한다.
def start():
    print("갤러그 게임 시작")
    return int(input("오늘은 몇마리의 적을 처치할 것인가요?(1~9마리) : "))

hope = start()

# 시작 시간 측정
time0 = time.time()

# 간단한 조작 설명 출력
print("조작은 [1]입력 : 왼쪽 발사,   [2]입력 : 오른쪽 발사] 입니다. ")

# 적 비행기 위치 : 리스트 사용
location = ["왼쪽", "오른쪽", "오른쪽", "왼쪽", "왼쪽", "오른쪽", "왼쪽", "왼쪽", "오른쪽"]

# 대응 : 딕셔너리
action1 = {
    "1" : "왼쪽",
    "2" : "오른쪽"
    }

# 대응에 대한 반응 : 딕셔너리 사용
action2 = {
    "성공" : "--------격추 성공 했습니다.--------",
    "실패" : "격추 실패 했습니다. 다시 발사 하세요.",
    "목표" : "목표를 완수 했습니다."
    }

# 입력한 목표수 만큼 반복 : for, while, 딕셔너리
for i in range(0,hope):

    print(location[i]+"에 적이 출현했습니다. 대응하세요.")
    number = input()
    while(True) :
       
        if (number!='1' and number!='2') :        #키를 잘못 입력 했을때를 위한 코드
            print("키를 잘못 입력했습니다.")
            number = input()
        else :
            while (True):                       # 정상 실행
                if action1[number] == location[i] :
                    print(action2["성공"])
                    break
                else :
                    print(action2["실패"])
                    number = input()
            break

# 결과 시간을 소수 둘째자리까지만 기록하기
result0 = round(((time.time()-time0) / hope),2)

#결과 출력
print(action2["목표"])
print('평균 격추 시간은 ' , result0, '초 입니다.')




