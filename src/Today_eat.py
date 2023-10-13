
'''
숭실대 고민사거리에 있는 음식과 식당을 추천해주고 해당 식당의 정보를 보여주는 프로그램
무엇을 먹고 싶은지부터 선택하면서 최종적으로 음식과 식당선정
파이썬으로 작성된 코드입니다.
'''
# 오픈소스 기초설계 과제 commit, push해보기

import webbrowser
from tkinter import *

# [식당정보]

#식당정보 딕셔너리(식당이름:url)
restaurant_info = {
    '찌개대학부대과': 'https://naver.me/GGUXGiYN',
    '스몰하우스': 'https://naver.me/xD6a8Lar',
    '김가네': 'https://naver.me/FU9viIpX',
    '파라다이스': 'https://naver.me/FGec3VOp',
    '내가찜한닭': 'https://naver.me/GNUkKv7R',
    '청운음식점': 'https://naver.me/5s3euRLw',
    '고기마을 찌개나라': 'https://naver.me/FM6l90CI',
    '백채김치찌개': 'https://naver.me/FsKBoCta',
    '더진국': 'https://naver.me/G8t2fOhI',
    '뚝배기스파게티': 'https://naver.me/x3irclhr',
    '도코라멘3900': 'https://naver.me/FU9viTld',
    '고추동제면소': 'https://naver.me/5UGSggpo',
    '취향': 'https://naver.me/FLKrE7mC',
    '우마이': 'https://naver.me/5OGHeHGA',
    '초밥이야기': 'https://naver.me/FJ63RZrJ',
    '나비루': 'https://naver.me/GCutJzfi',
    '서브웨이': 'https://naver.me/5jjtXoAl',
    '맥도날드': 'https://naver.me/FhdZukIH'
}

# 식당정보를 url로 연결하여 알려주는 함수
def open_url(restaurant_name):
    url = restaurant_info.get(restaurant_name) # 딕셔너리의 값(식당정보url)을 불러옴
    if url: # url이 있는 경우 실행
        webbrowser.open(url)
    else: #url이 없는 경우 실행
        print('식당 정보를 찾을 수 없습니다.')


# [식당추천] 설명은 food01에 있습니다. 다른 함수들은 버튼 개수와 버튼 텍스트를 제외하고 동일합니다.

def food21(): # 한식 덮밥 --> 스몰하우스 / win37
    global win37
    win16.withdraw()
    win37 =Toplevel()
    win37.title("오늘 뭐 먹지?")
    win37.geometry("800x600")
    win37.option_add("*Font","맑은고딕 25")

    label1 = Label(win37)
    label1.config(text="선택한 음식: 덮밥")
    label1.place(x=240,y=100)
    label2 = Label(win37)
    label2.config(text="추천식당")
    label2.place(x=320,y=250)

    btn1 = Button(win37)
    btn1.config(width=7,height=2,text="스몰하우스",command=lambda:open_url("스몰하우스"))
    btn1.place(x=300,y=330)
    btn = Button(win37)
    btn.config(width=6,height=2,text="종료",command=win37.destroy)
    btn.place(x=330,y=450)

def food20(): # 한식 김밥 --> 김가네 / win36
    global win36
    win16.withdraw()
    win36 =Toplevel()
    win36.title("오늘 뭐 먹지?")
    win31.geometry("800x600")
    win35.option_add("*Font","맑은고딕 25")

    label1 = Label(win36)
    label1.config(text="선택한 음식: 김밥")
    label1.place(x=240,y=100)
    label2 = Label(win36)
    label2.config(text="추천식당")
    label2.place(x=320,y=250)

    btn1 = Button(win36)
    btn1.config(width=7,height=2,text="김가네",command=lambda:open_url("김가네"))
    btn1.place(x=280,y=330)
    btn = Button(win36)
    btn.config(width=6,height=2,text="종료",command=win36.destroy)
    btn.place(x=330,y=450)

def food19(): # 한식 김치볶음밥 --> 파라다이스 / win35
    global win35
    win16.withdraw()
    win35 =Toplevel()
    win35.title("오늘 뭐 먹지?")
    win31.geometry("800x600")
    win35.option_add("*Font","맑은고딕 25")

    label1 = Label(win35)
    label1.config(text="선택한 음식: 김치볶음밥")
    label1.place(x=240,y=100)
    label2 = Label(win35)
    label2.config(text="추천식당")
    label2.place(x=320,y=250)

    btn1 = Button(win35)
    btn1.config(width=10,height=2,text="파라다이스",command=lambda:open_url("파라다이스"))
    btn1.place(x=280,y=330)
    btn = Button(win35)
    btn.config(width=6,height=2,text="종료",command=win35.destroy)
    btn.place(x=330,y=450)

def food18(): # 한식 찜닭 --> 내가 찜한 닭 / win34
    global win34
    win15.withdraw()
    win34 =Toplevel()
    win34.title("오늘 뭐 먹지?")
    win34.geometry("800x600")
    win34.option_add("*Font","맑은고딕 25")

    label1 = Label(win34)
    label1.config(text="선택한 음식: 찜닭")
    label1.place(x=240,y=100)
    label2 = Label(win34)
    label2.config(text="추천식당")
    label2.place(x=320,y=250)

    btn1 = Button(win34)
    btn1.config(width=12,height=2,text="내가 찜한 닭",command=lambda:open_url("내가찜한닭"))
    btn1.place(x=240,y=330)
    btn = Button(win34)
    btn.config(width=6,height=2,text="종료",command=win34.destroy)
    btn.place(x=330,y=450)

def food17(): # 한식 삼겹살 --> 청운음식점 / win33
    global win33
    win15.withdraw()
    win33 =Toplevel()
    win33.title("오늘 뭐 먹지?")
    win33.geometry("800x600")
    win33.option_add("*Font","맑은고딕 25")

    label1 = Label(win33)
    label1.config(text="선택한 음식: 삼겹살")
    label1.place(x=240,y=100)
    label2 = Label(win33)
    label2.config(text="추천식당")
    label2.place(x=320,y=250)

    btn1 = Button(win33)
    btn1.config(width=10,height=2,text="청운음식점",command=lambda:open_url("청운음식점"))
    btn1.place(x=280,y=330)
    btn = Button(win33)
    btn.config(width=6,height=2,text="종료",command=win33.destroy)
    btn.place(x=330,y=450)

def food16(): # 한식 제육 --> 고기마을 찌개나라 / win32
    global win32
    win15.withdraw()
    win32 =Toplevel()
    win32.title("오늘 뭐 먹지?")
    win32.geometry("800x600")
    win32.option_add("*Font","맑은고딕 25")

    label1 = Label(win32)
    label1.config(text="선택한 음식: 제육")
    label1.place(x=240,y=100)
    label2 = Label(win32)
    label2.config(text="추천식당")
    label2.place(x=320,y=250)

    btn1 = Button(win32)
    btn1.config(width=12,height=2,text="고기마을 찌개나라",command=lambda:open_url("고기마을 찌개나라"))
    btn1.place(x=240,y=330)
    btn = Button(win32)
    btn.config(width=6,height=2,text="종료",command=win32.destroy)
    btn.place(x=330,y=450)

def food15(): # 한식 김치찌개 --> 백채김치찌개 / win31
    global win31
    win14.withdraw()
    win31 =Toplevel()
    win31.title("오늘 뭐 먹지?")
    win31.geometry("800x600")
    win31.option_add("*Font","맑은고딕 25")

    label1 = Label(win31)
    label1.config(text="선택한 음식: 김치찌개")
    label1.place(x=240,y=100)
    label2 = Label(win31)
    label2.config(text="추천식당")
    label2.place(x=320,y=250)

    btn1 = Button(win31)
    btn1.config(width=10,height=2,text="백채김치찌개",command=lambda:open_url("백채김치찌개"))
    btn1.place(x=280,y=330)
    btn = Button(win31)
    btn.config(width=6,height=2,text="종료",command=win31.destroy)
    btn.place(x=330,y=450)

def food14(): # 한식 부대찌개 --> 찌개대학부대과 / win30
    global win30
    win14.withdraw()
    win30 =Toplevel()
    win30.title("오늘 뭐 먹지?")
    win30.geometry("800x600")
    win30.option_add("*Font","맑은고딕 25")

    label1 = Label(win30)
    label1.config(text="선택한 음식: 부대찌개")
    label1.place(x=240,y=100)
    label2 = Label(win30)
    label2.config(text="추천식당")
    label2.place(x=320,y=250)

    btn1 = Button(win30)
    btn1.config(width=12,height=2,text="찌개대학부대과",command=lambda:open_url("찌개대학부대과"))
    btn1.place(x=260,y=330)
    btn = Button(win30)
    btn.config(width=6,height=2)
    btn.config(width=6,height=2,text="종료",command=win30.destroy)
    btn.place(x=330,y=450)

def food13(): # 한식 국밥 --> 더진국 / win29
    global win29
    win14.withdraw()
    win29 =Toplevel()
    win29.title("오늘 뭐 먹지?")
    win29.geometry("800x600")
    win29.option_add("*Font","맑은고딕 25")
    
    label1 = Label(win29)
    label1.config(text="선택한 음식: 국밥")
    label1.place(x=240,y=100)
    label2 = Label(win29)
    label2.config(text="추천식당")
    label2.place(x=320,y=250)

    btn1 = Button(win29)
    btn1.config(width=7,height=2,text="더진국",command=lambda:open_url("더진국"))
    btn1.place(x=320,y=330)
    btn = Button(win29)
    btn.config(width=6,height=2,text="종료",command=win29.destroy)
    btn.place(x=330,y=450)

def food12(): # 양식 파스타 --> 뚝배기스파게티 / win28
    global win28
    win13.withdraw()
    win28 =Toplevel()
    win28.title("오늘 뭐 먹지?")
    win28.geometry("800x600")
    win28.option_add("*Font","맑은고딕 25")

    label1 = Label(win28)
    label1.config(text="선택한 음식: 파스타")
    label1.place(x=240,y=100)
    label2 = Label(win28)
    label2.config(text="추천식당")
    label2.place(x=320,y=250)

    btn1 = Button(win28)
    btn1.config(width=10,height=2,text="뚝배기스파게티",command=lambda:open_url("뚝배기스파게티"))
    btn1.place(x=280,y=330)
    btn = Button(win28)
    btn.config(width=6,height=2,text="종료",command=win28.destroy)
    btn.place(x=330,y=450)

def food11(): # 일식 소바 --> 도쿄라멘3900 / win27
    global win27
    win12.withdraw()
    win27 =Toplevel()
    win27.title("오늘 뭐 먹지?")
    win26.geometry("800x600")
    win26.option_add("*Font","맑은고딕 25")

    label1 = Label(win27)
    label1.config(text="선택한 음식: 소바")
    label1.place(x=240,y=100)
    label2 = Label(win27)
    label2.config(text="추천식당")
    label2.place(x=320,y=250)

    btn1 = Button(win27)
    btn1.config(width=10,height=2,text="도쿄라멘3900",command=lambda:open_url("도쿄라멘3900"))
    btn1.place(x=280,y=330)
    btn = Button(win27)
    btn.config(width=6,height=2,text="종료",command=win27.destroy)
    btn.place(x=330,y=450)

def food10(): # 일식 라멘 --> 도쿄라멘3900 / win26
    global win26
    win12.withdraw()
    win26 =Toplevel()
    win26.title("오늘 뭐 먹지?")
    win26.geometry("800x600")
    win26.option_add("*Font","맑은고딕 25")

    label1 = Label(win26)
    label1.config(text="선택한 음식: 라멘")
    label1.place(x=240,y=100)
    label2 = Label(win26)
    label2.config(text="추천식당")
    label2.place(x=320,y=250)

    btn1 = Button(win26)
    btn1.config(width=10,height=2,text="도쿄라멘3900",command=lambda:open_url("도쿄라멘3900"))
    btn1.place(x=280,y=330)     
    btn = Button(win26)
    btn.config(width=6,height=2,text="종료",command=win26.destroy)
    btn.place(x=330,y=450)

def food09(): # 중식 짬뽕 --> 취향 / win25
    global win25
    win11.withdraw()
    win25 =Toplevel()
    win25.title("오늘 뭐 먹지?")
    win25.geometry("800x600")
    win25.option_add("*Font","맑은고딕 25")

    label1 = Label(win25)
    label1.config(text="선택한 음식: 짬뽕")
    label1.place(x=240,y=100)
    label2 = Label(win25)
    label2.config(text="추천식당")
    label2.place(x=320,y=250)

    btn1 = Button(win25)
    btn1.config(width=7,height=2,text="취향",command=lambda:open_url("취향"))
    btn = Button(win25)
    btn.config(width=6,height=2,text="종료",command=win25.destroy)
    btn.place(x=330,y=450)

def food08(): # 중식 짜장면 --> 취향 / win24
    global win24
    win11.withdraw()
    win24 =Toplevel()
    win24.title("오늘 뭐 먹지?")
    win24.geometry("800x600")
    win24.option_add("*Font","맑은고딕 25")

    label1 = Label(win24)
    label1.config(text="선택한 음식: 짜장면")
    label1.place(x=240,y=100)
    label2 = Label(win24)
    label2.config(text="추천식당")
    label2.place(x=320,y=250)

    btn1 = Button(win24)
    btn1.config(width=7,height=2,text="취향",command=lambda:open_url("취향"))
    btn1.place(x=320,y=330)  
    btn = Button(win17)
    btn.config(width=6,height=2,text="종료",command=win24.destroy)
    btn.place(x=330,y=450)

def food07(): # 한식 국수 --> 고추동제면소 / win23
    global win23
    win10.withdraw()
    win23 =Toplevel()
    win23.title("오늘 뭐 먹지?")
    win23.geometry("800x600")
    win23.option_add("*Font","맑은고딕 25")

    label1 = Label(win23)
    label1.config(text="선택한 음식: 국수")
    label1.place(x=240,y=100)
    label2 = Label(win23)
    label2.config(text="추천식당")
    label2.place(x=320,y=250)

    btn1 = Button(win23)
    btn1.config(width=10,height=2,text="고추동제면소",command=lambda:open_url("고추동제면소"))
    btn1.place(x=280,y=330)
    btn = Button(win23)
    btn.config(width=6,height=2,text="종료",command=win23.destroy)
    btn.place(x=330,y=450)

def food06(): # 중식 볶음밥 --> 취향 / win22
    global win22
    win08.withdraw()
    win22 =Toplevel()
    win22.title("오늘 뭐 먹지?")
    win22.geometry("800x600")
    win22.option_add("*Font","맑은고딕 25")
    
    label1 = Label(win22)
    label1.config(text="선택한 음식: 볶음밥")
    label1.place(x=240,y=100)
    label2 = Label(win22)
    label2.config(text="추천식당")
    label2.place(x=320,y=250)

    btn1 = Button(win22)
    btn1.config(width=7,height=2,text="취향",command=lambda:open_url("취향"))
    btn1.config(text="취향")
    btn1.config(command=open_url("취향"))
    btn1.place(x=320,y=330)    
    btn = Button(win22)
    btn.config(width=6,height=2,text="종료",command=win22.destroy)
    btn.place(x=330,y=450)

def food05(): # 일식 카레 --> 우마이 / win21
    global win21
    win07.withdraw()
    win21 =Toplevel()
    win21.title("오늘 뭐 먹지?")
    win21.geometry("800x600")
    win21.option_add("*Font","맑은고딕 25")

    label1 = Label(win21)
    label1.config(text="선택한 음식: 카레")
    label1.place(x=240,y=100)
    label2 = Label(win21)
    label2.config(text="추천식당")
    label2.place(x=320,y=250)

    btn1 = Button(win21)
    btn1.config(width=7,height=2,text="우마이",command=lambda:open_url("우마이"))
    btn1.place(x=320,y=330)
    btn = Button(win21)
    btn.config(width=6,height=2,text="종료",command=win21.destroy)
    btn.place(x=330,y=450)

def food04(): # 일식 초밥 --> 초밥이야기 / win20
    global win20
    win07.withdraw()
    win20 =Toplevel()
    win20.title("오늘 뭐 먹지?")
    win20.geometry("800x600")
    win20.option_add("*Font","맑은고딕 25")

    label1 = Label(win20)
    label1.config(text="선택한 음식: 초밥")
    label1.place(x=240,y=100)
    label2 = Label(win20)
    label2.config(text="추천식당")
    label2.place(x=320,y=250)

    btn1 = Button(win20)
    btn1.config(width=7,height=2,text="초밥이야기",command=lambda:open_url("초밥이야기"))
    btn1.place(x=320,y=330)
    btn = Button(win20)
    btn.config(width=6,height=2,text="종료",command=win20.destroy)
    btn.place(x=330,y=450)

def food03(): # 일식 덮밥 --> 나비루 / win19
    global win19
    win07.withdraw()
    win19 =Toplevel()
    win19.title("오늘 뭐 먹지?")
    win19.geometry("800x600")
    win19.option_add("*Font","맑은고딕 25")

    label1 = Label(win19)
    label1.config(text="선택한 음식: 덮밥")
    label1.place(x=240,y=100)
    label2 = Label(win19)
    label2.config(text="추천식당")
    label2.place(x=320,y=250)

    btn1 = Button(win19)
    btn1.config(width=7,height=2,text="나비루",command=lambda:open_url("나비루"))
    btn1.place(x=320,y=330)
    btn = Button(win19)
    btn.config(width=6,height=2,text="종료",command=win19.destroy)
    btn.place(x=330,y=450)

def food02(): # 샌드위치 --> 서브웨이 / win18
    global win18
    win04.withdraw()
    win18 =Toplevel()
    win18.title("오늘 뭐 먹지?")
    win18.geometry("800x600")
    win18.option_add("*Font","맑은고딕 25")

    label1 = Label(win18)
    label1.config(text="선택한 음식: 햄버거")
    label1.place(x=240,y=100)
    label2 = Label(win18)
    label2.config(text="추천식당")
    label2.place(x=320,y=250)

    btn1 = Button(win18)
    btn1.config(width=7,height=2,text="서브웨이",command=open_url("서브웨이"))
    btn1.place(x=320,y=330)
    
    btn = Button(win18)
    btn.config(width=6,height=2,text="종료",command=win18.destroy)
    btn.place(x=330,y=450)

def food01(): # 햄버거 --> 맥도날드 / win17
    global win17 # 현재화면 전역변수 선언, 다른 함수에서 조작 가능하게 함
    win04.withdraw() # 이전화면 없애기
    # 화면 기본 설정
    win17 =Toplevel() # 새 화면 선언
    win17.title("오늘 뭐 먹지?") # 화면 제목
    win17.geometry("800x600") # 화면 크기 설정
    win17.option_add("*Font","맑은고딕 25") # 폰트설정

    label1 = Label(win17) # 설명 텍스트 1
    label1.config(text="선택한 음식: 햄버거")
    label1.place(x=240,y=100)
    label2 = Label(win17)
    label2.config(text="추천식당") # 설명 텍스트 2
    label2.place(x=320,y=250)

    btn1 = Button(win17)
    btn1.config(width=7,height=2,text="맥도날드",command=lambda:open_url("맥도날드"))
    btn1.place(x=320,y=330)
 # lambda의 역할, 함수가 인수를 가지고 있기 때문에 익명함수를 설정한 뒤 동작하게 하여 오류가 발생하지 않게 함

    btn = Button(win17)
    btn.config(width=6,height=2,text="종료",command=win17.destroy) # 종료버튼, 누를시 프로그램 종료
    btn.place(x=330,y=450)

# [메뉴추천] 설명은 go_win01에 있습니다. 다른 함수들은 버튼 개수와 버튼 텍스트를 제외하고 동일 합니다.

def go_win16(): # 밥 한식 국물X 고기X 선택시 이동 (다음 선택지: 김치볶음밥, 김밥, 덮밥) / 식당 추천 완료 food19~21
    global win16
    win06.withdraw()
    win16=Toplevel()
    win16.title("오늘 뭐 먹지?")
    win16.geometry("800x600")
    win16.option_add("*Font","맑은고딕 25")

    label1 = Label(win16)
    label1.config(text="다음 중 먹고 싶은 것은?")
    label1.place(x=220,y=100)    

    btn1 = Button(win16)
    btn1.config(width=6,height=2,text="김치볶음밥",command=food19)
    btn1.place(x=140,y=350)

    btn2 = Button(win16)
    btn2.config(width=6,height=2,text="김밥",command=food20)
    btn2.place(x=340,y=350)

    btn3 = Button(win16)
    btn3.config(width=6,height=2,text="덮밥",command=food21)
    btn3.place(x=540,y=350)

def go_win15(): # 밥 한식 국물X 고기 선택시 이동 (다음 선택지: 제육, 삼겹살, 찜닭) / 식당 추천 완료 food16~18
    global win15
    win09.withdraw()
    win15=Toplevel()
    win15.title("오늘 뭐 먹지?")
    win15.geometry("800x600")
    win15.option_add("*Font","맑은고딕 25")

    label1 = Label(win15)
    label1.config(text="다음 중 먹고 싶은 것은?")
    label1.place(x=220,y=100)    

    btn1 = Button(win15)
    btn1.config(width=6,height=2,text="제육",command=food16)
    btn1.place(x=140,y=350)

    btn2 = Button(win15)
    btn2.config(width=6,height=2,text="삼겹살",command=food17)
    btn2.place(x=340,y=350)

    btn3 = Button(win15)
    btn3.config(width=6,height=2,text="찜닭",command=food18)
    btn3.place(x=540,y=350)

def go_win14(): # 밥 한식 국물 선택시 이동 (다음 선택지: 국밥, 부대찌개, 김치찌개) / 식당 추천 완료 food13~15
    global win14
    win06.withdraw()
    win14=Toplevel()
    win14.title("오늘 뭐 먹지?")
    win14.geometry("800x600")
    win14.option_add("*Font","맑은고딕 25")

    label1 = Label(win14)
    label1.config(text="다음 중 먹고 싶은 것은?")
    label1.place(x=220,y=100)    

    btn1 = Button(win14)
    btn1.config(width=6,height=2,text="국밥",command=food13)
    btn1.place(x=140,y=350)

    btn2 = Button(win14)
    btn2.config(width=6,height=2,text="김치찌개",command=food15)
    btn2.place(x=340,y=350)

    btn3 = Button(win14)
    btn3.config(width=6,height=2)
    btn3.config(text="부대찌개")
    btn3.config(command=food14)
    btn3.place(x=540,y=350) 

def go_win13(): # 밥X 면 양식 선택시 이동 (다음 선택지: 파스타) / 식당 추천 완료 food12
    global win13
    win05.withdraw()
    win13 =Toplevel()
    win13.title("오늘 뭐 먹지?")
    win13.geometry("800x600")
    win13.option_add("*Font","맑은고딕 25")
    
    label1 = Label(win13)
    label1.config(text="다음 중 먹고 싶은 것은?")
    label1.place(x=220,y=100)    

    btn1 = Button(win13)
    btn1.config(width=6,height=2,text="파스타",command=food12)
    btn1.place(x=380,y=350)

def go_win12(): # 밥X 면 일식 선택시 이동 (다음 선택지: 라멘, 소바) / 식당 추천 완료 food10~11
    global win12
    win05.withdraw()
    win12 =Toplevel()
    win12.title("오늘 뭐 먹지?")
    win12.geometry("800x600")
    win12.option_add("*Font","맑은고딕 25")
    label1 = Label(win12)
    label1.config(text="다음 중 먹고 싶은 것은?")
    label1.place(x=220,y=100)

    btn1 = Button(win12)
    btn1.config(width=6,height=2,text="라멘",command=food10)
    btn1.place(x=240,y=350)

    btn2 = Button(win12)
    btn2.config(width=6,height=2,text="소바",command=food11)
    btn2.place(x=440,y=350)

def go_win11(): # 밥X 면 중식 선택시 이동 (다음 선택지: 짜장면, 짬뽕) / 식당 추천 완료 food08~09
    global win11
    win05.withdraw()
    win11 =Toplevel()
    win11.title("오늘 뭐 먹지?")
    win11.geometry("800x600")
    win11.option_add("*Font","맑은고딕 25")
    label1 = Label(win11)
    label1.config(text="다음 중 먹고 싶은 것은?")
    label1.place(x=220,y=100)

    btn1 = Button(win11)
    btn1.config(width=6,height=2,text="짜장면",command=food08)
    btn1.place(x=240,y=350)

    btn12 = Button(win11)
    btn12.config(width=6,height=2,text="짬뽕",command=food09)
    btn12.place(x=440,y=350)

def go_win10(): # 밥X 면 한식 선택시 이동 (다음 선택지: 국수) / 식당 추천 완료 food07
    global win10
    win05.withdraw()
    win10 =Toplevel()
    win10.title("오늘 뭐 먹지?")
    win10.geometry("800x600")
    win10.option_add("*Font","맑은고딕 25")
    label1 = Label(win10)
    label1.config(text="다음 중 먹고 싶은 것은?")
    label1.place(x=220,y=100)    

    btn1 = Button(win10)
    btn1.config(width=6,height=2,text="국수",command=food07)
    btn1.place(x=340,y=350)

def go_win09(): # 밥 한식 국물X 선택시 이동 (다음 선택지: 고기, 고기X)
    global win09
    win06.withdraw()
    win09 =Toplevel()
    win09.title("오늘 뭐 먹지?")
    win09.geometry("800x600")
    win09.option_add("*Font","맑은고딕 25")
    label1= Label(win09)
    label1.config(text="다음 중 먹고 싶은 것은?")
    label1.place(x=220,y=100)

    btn1 = Button(win09)
    btn1.config(width=6,height=2,text="고기",command=go_win15)
    btn1.place(x=240,y=350)

    btn2 = Button(win09)
    btn2.config(width=6,height=2,text="고기X",command=go_win16)
    btn2.place(x=440,y=350)        

def go_win08(): # 밥 중식 선택시 이동 (다음 선택지: 볶음밥) / 식당 추천 완료 food06
    global win08
    win02.withdraw()
    win08=Toplevel()
    win08.title("오늘 뭐 먹지?")
    win08.geometry("800x600")
    win08.option_add("*Font","맑은고딕 25")

    label1 = Label(win08)
    label1.config(text="다음 중 먹고 싶은 것은?")
    label1.place(x=220,y=100)    

    btn1 = Button(win08)
    btn1.config(width=6,height=2,text="볶음밥",command=food06)
    btn1.place(x=380,y=350)

def go_win07(): # 밥 일식 선택시 이동 (다음 선택지: 덮밥, 초밥, 카레) / 식당 추천 완료 food03~05
    global win07
    win02.withdraw()
    win07=Toplevel()
    win07.title("오늘 뭐 먹지?")
    win07.geometry("800x600")
    win07.option_add("*Font","맑은고딕 25")

    label1 = Label(win07)
    label1.config(text="다음 중 먹고 싶은 것은?")
    label1.place(x=220,y=100)    

    btn1 = Button(win07)
    btn1.config(width=6,height=2,text="덮밥",command=food03)
    btn1.place(x=140,y=350)

    btn2 = Button(win07)
    btn2.config(width=6,height=2,text="카레",command=food05)
    btn2.place(x=340,y=350)

    btn23 = Button(win07)
    btn23.config(width=6,height=2,text="초밥",command=food04)
    btn23.place(x=540,y=350)    

def go_win06(): # 밥 한식 선택시 이동 (다음 선택지: 국물, 국물X)
    global win06
    win02.withdraw()
    win06 =Toplevel()
    win06.title("오늘 뭐 먹지?")
    win06.geometry("800x600")
    win06.option_add("*Font","맑은고딕 25")
    label1 = Label(win06)
    label1.config(text="다음 중 먹고 싶은 것은?")
    label1.place(x=220,y=100)

    btn1 = Button(win06)
    btn1.config(width=6,height=2,text="국물",command=go_win14)
    btn1.place(x=240,y=350)

    btn2 = Button(win06)
    btn2.config(width=6,height=2,text="국물X",command=go_win09)
    btn2.place(x=440,y=350)    

def go_win05(): # 밥X 면 선택시 이동 (다음 선택지: 한식, 중식, 일식, 양식)
    global win05
    win03.withdraw()
    win05 =Toplevel()
    win05.title("오늘 뭐 먹지?")
    win05.geometry("800x600")
    win05.option_add("*Font","맑은고딕 25")
    label1 = Label(win05)
    label1.config(text="다음 중 먹고 싶은 것은?")
    label1.place(x=220,y=100)

    btn1 = Button(win05)
    btn1.config(width=6,height=2,text="한식",command=go_win10)
    btn1.place(x=40,y=350)

    btn2 = Button(win05)
    btn2.config(width=6,height=2,text="중식",command=go_win11)
    btn2.place(x=240,y=350)

    btn3 = Button(win05)
    btn3.config(width=6,height=2,text="일식",command=go_win12)
    btn3.place(x=440,y=350)

    btn4 = Button(win05)
    btn4.config(width=6,height=2,text="양식",command=go_win13)
    btn4.place(x=640,y=350)  

def go_win04(): # 밥X 빵 선택시 이동 (다음 선택지: 햄버거, 샌드위치) / 식당 추천 완료 food01~02
    global win04
    win03.withdraw()
    win04 =Toplevel()
    win04.title("오늘 뭐 먹지?")
    win04.geometry("800x600")
    win04.option_add("*Font","맑은고딕 25")
    label1 = Label(win04)
    label1.config(text="다음 중 먹고 싶은 것은?")
    label1.place(x=220,y=100)

    btn1 = Button(win04)
    btn1.config(width=6,height=2,text="햄버거",command=food01)
    btn1.place(x=240,y=350)

    btn2 = Button(win04)
    btn2.config(width=6,height=2,text="샌드위치",command=food02)
    btn2.place(x=440,y=350)    

def go_win03(): # 밥X 선택시 이동 (다음 선택지: 면, 빵)
    global win03
    win01.withdraw()
    win03=Toplevel()
    win03.title("오늘 뭐 먹지?")
    win03.geometry("800x600")
    win03.option_add("*Font","맑은고딕 25")
    label1 = Label(win03)
    label1.config(text="다음 중 먹고 싶은 것은?")
    label1.place(x=220,y=100)

    btn1 = Button(win03)
    btn1.config(width=6,height=2,text="면",command=go_win05)
    btn1.place(x=240,y=350)

    btn2 = Button(win03)
    btn2.config(width=6,height=2,text="빵",command=go_win04)
    btn2.place(x=440,y=350)

def go_win02(): # 밥 선택시 이동 (다음 선택지: 한식, 일식, 중식)
    global win02
    win01.withdraw()
    win02=Toplevel()
    win02.title("오늘 뭐 먹지?")
    win02.geometry("800x600")
    win02.option_add("*Font","맑은고딕 25")

    label1 = Label(win02)
    label1.config(text ="다음 중 먹고 싶은 것은?")
    label1.place(x=220,y=100)    

    btn1 = Button(win02)
    btn1.config(width=6,height=2,text="한식",command=go_win06)
    btn1.place(x=140,y=350)

    btn2 = Button(win02)
    btn2.config(width=6,height=2,text="중식",command=go_win08)
    btn2.place(x=340,y=350)

    btn3 = Button(win02)
    btn3.config(width=6,height=2,text="일식",command=go_win07)
    btn3.place(x=540,y=350)

def go_win01(): # 시작 선택시 이동 (다음 선택지: 밥, 밥X)
    global win01 # 화면 전역변수 선언, 다른 함수에서 조작가능하게 함
    win00.withdraw() # 이전 화면 지우기
    win01=Toplevel() # 새 화면 선언
    win01.title("오늘 뭐 먹지?") # 화면 제목
    win01.geometry("800x600") # 화면 크기
    win01.option_add("*Font","맑은고딕 25") # 폰트 설정

    label01 = Label(win01) # 설명 텍스트
    label01.config(text="다음 중 먹고 싶은 것은?") # 텍스트 내용
    label01.place(x=220,y=100) # 텍스트 위치 설정

    btn1 = Button(win01) # 버튼1
    btn1.config(width=6,height=2,text="밥",command=go_win02) # 버튼설정 및 이벤트, go_win02 함수 실행
    btn1.place(x=240,y=350) # 버튼1 위치 설정

    btn2 = Button(win01) # 버튼2
    btn2.config(width=6,height=2,text="밥X",command=go_win03) # 버튼설정 및 이벤트, go_win03 함수 실행
    btn2.place(x=440,y=350) # 버튼2 위치 설정

# 시작화면

# 화면 기초 설정(제목,크기,폰트)
win00=Tk()
win00.title("오늘 뭐 먹지?")
win00.geometry("800x600")
win00.option_add("*Font","맑은고딕 25")

# 선택지 설명 텍스트
label1 = Label(win00)
label1.config(text="오늘 뭐 먹지?",font=("맑은고딕",50))
label1.place(x=200,y=190)

# 선택지 버튼
b1 = Button(win00)
b1.config(width=6,height=2,text="시작",command=go_win01) # 버튼을 누르면 새창으로 이동
b1.place(x=230,y=400) # 시작 버튼 배치

b2 = Button(win00)
b2.config(width=6,height=2,text="종료",command=win00.destroy) # 버튼을 누르면 종료
b2.place(x=430,y=400) # 종료 버튼 배치

# 화면 실행
win00.mainloop()
