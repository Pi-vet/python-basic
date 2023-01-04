#회원가입 - 로그인 선택 - 기본 함수 세팅
login = "로그인"
Sign_up = "회원가입"
Check_0 = "예"
Check_1 = "아니요"
login_attempt = 0
break_judgment = 0
User_id = 865826515
User_pw = 985159179
#임시 id - pw
#User_id = 'a'
#User_pw = 'a'

while True: #무한반복
    if 1 == break_judgment: #break 판단
        break
    print("'회원가입 / 로그인' 중에 선택해주십시오") #선택
    Select_Login_Way_User = input("")
    if Select_Login_Way_User != login and Select_Login_Way_User != Sign_up: #값이 둘중에 한개도 일치하지 않으면
        print("제대로 입력해주십시오\n")
        continue
    while True: #무한 반복
        
    #회원가입
        if Select_Login_Way_User == Sign_up:
            print("회원가입을 하기 위해서는 자신이 원하는 ID 와 PW 를 입력해주십시오.")
            User_id = input()   
            User_pw = input()
            print("ID - PW 설정이 끝났습니다 처음 화면으로 가시겠습니까?\n 예 / 아니오 (참고 :: 예,아니오 가 아닌 다른 대답이 입력될시 예로 판단)")
            A = input()
            if A == "아니오":
                break
                break_judgment = 1
            elif A == "예":
                break
            else:
                break
    #로그인
        if Select_Login_Way_User == login:
                    print("로그인 ID 와 PW 를 입력해주십시오.\n 처음화면으로 돌아가시려면 LOVE를 2번 입력해주세요")
                    User_Id_Enter = input()
                    User_Pw_Enter = input()
                    login_attempt = login_attempt + 1
                    if User_Id_Enter == "LOVE":
                        if User_Pw_Enter == "LOVE":
                            break
                    if User_id == User_Id_Enter and User_Pw_Enter:
                        print("로그인 성공")
                        login_attempt = 0
                        break_judgment = 1
                        break
                    else:
                        if login_attempt >= 5:
                            print(" 로그인 실패 횟수가 5번이 넘었습니다.")
                            break_judgment = 1
                            break
                        else:
                            print("로그인 실패")
                            continue