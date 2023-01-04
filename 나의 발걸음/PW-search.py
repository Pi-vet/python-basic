print("회원가입 진행\n이메일과 비밀번호를 설정해주세요")
Email = input()
PW = input()
break_judgement = 0
while True:
    if int(break_judgement) == 1:
        break
    print("' 로그인 / 비밀번호 찾기 / 이메일 찾기 ' 중에 선택해주세요.\n(참고 :: 입력한 단어가 아무것도 일치하지 않을시 로그인 화면으로 자동으로 전환합니다.")
    User_Select = input()
    if User_Select == '이메일 찾기':
        while True:
            print("이메일을 찾으시려면 비밀번호'만' 을 입력해주세요.")
            PW_User_Email_Search = input()
            if PW == PW_User_Email_Search:
                print(Email)
                break
            else:
                print("비밀번호가 일치하지 않습니다")
                continue
            
    elif User_Select == '비밀번호 찾기':
        while True:
            print("비밀번호를 찾으시려면 이메일'만' 입력해주세요.")
            Email_User_Pw_search = input()
            if Email == Email_User_Pw_search:
                print(PW)
                break
            else:
                print("이메일이 일치하지 않습니다.")
                continue
                 
    elif User_Select == '로그인':
        while True:
            print("로그인을 하시려면 이메일과 비번을 입력해주세요.")
            Email_Enter = input()
            PW_Enter = input()
            if Email_Enter == Email and PW_Enter == PW:
                print("로그인 성공")
                break_judgement = 1
                break  
            else:
                print("일치하지 않습니다.")
                continue
    else:
        while True:
            print("로그인을 하시려면 이메일과 비번을 입력해주세요.")
            Email_Enter = input()
            PW_Enter = input()
            if Email_Enter == Email and PW_Enter == PW:
                print("로그인 성공")
                break_judgement = 1
                break
            else:
                print("일치하지 않습니다.")
                continue
                
        