import random
import pygame, sys
from pygame.locals import*

pygame.init()
DISPLAY = pygame.display.set_mode((500,650)) #디스플레이(윈도우) 크기 설정
pygame.display.set_caption('RANDOM LUNCH')   #디스플레이 이름 설정(상태바에 표시)


btn = pygame.image.load("button_1.png") #버튼 이미지 불러오기
btn1_rect = btn.get_rect(center=(250,250)) #이미지로 불러온 버튼 좌표
btn2_rect = btn.get_rect(center=(250,320))
btn3_rect = btn.get_rect(center=(250,390))
btn4_rect = btn.get_rect(center=(250,460))
btn5_rect = btn.get_rect(center=(250,530))

font = pygame.font.Font('NanumSquareRoundB.ttf',20) #텍스트 폰트 설정
font2 = pygame.font.Font('NanumSquareRoundB.ttf',50)
font3 = pygame.font.Font('NanumSquareRoundB.ttf',22)

text =[font.render('한식',True,(255,255,255)),font.render("일식",True,(255,255,255)),
       font.render('중식',True,(255,255,255)),font.render('양식',True,(255,255,255)),
       font.render('기타',True,(255,255,255))]

text_2 = [font.render('Random',True,(255,103,129)),font2.render('점심 메뉴 뽑기!',True,(0,0,0)),
          font3.render('아래의 메뉴 중',True,(0,0,0)),font3.render('하나를 눌러주세요',True,(0,0,0))]

textmenu_rect = [text[0].get_rect(center=(250,250)),text[0].get_rect(center=(250,320)), #텍스트 좌표 설정
             text[0].get_rect(center=(250,390)),text[0].get_rect(center=(250,460)),
             text[0].get_rect(center=(250,530))]

textmain_rect = [text[0].get_rect(center=(70,40)),text[0].get_rect(center=(110,65)),
                 text[0].get_rect(center=(200,135)),text[0].get_rect(center=(185,165))]

while True:
    for event in pygame.event.get(): #이벤트 설정

        if event.type == QUIT: #종료 이벤트 설정
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:      #마우스버튼 누르고 띄었을 때 이벤트 발생
            if btn1_rect.collidepoint(event.pos):   #각 버튼마다 이벤트 설정
                pass
            # import pygame_2
            # pygame_2.select(pi)
            if btn2_rect.collidepoint(event.pos):
                pass
            if btn3_rect.collidepoint(event.pos):
                pass
            if btn4_rect.collidepoint(event.pos):
                pass
            if btn5_rect.collidepoint(event.pos):
                pass

    DISPLAY.fill((255,255,255))         #디스플레이(윈도우창)색깔 설정
    DISPLAY.blit(text_2[0],textmain_rect[0])
    DISPLAY.blit(text_2[1],textmain_rect[1])
    DISPLAY.blit(text_2[2],textmain_rect[2])
    DISPLAY.blit(text_2[3],textmain_rect[3])

    DISPLAY.blit(btn,btn1_rect)         #1번 버튼 만들기
    DISPLAY.blit(text[0],textmenu_rect[0])  #1번 버튼위에 텍스트 입히기
    DISPLAY.blit(btn,btn2_rect)         #2번 버튼 만들기
    DISPLAY.blit(text[1],textmenu_rect[1])  #2번 버튼위에 텍스트 입히기
    DISPLAY.blit(btn,btn3_rect)         #3번 버튼 만들기
    DISPLAY.blit(text[2],textmenu_rect[2])  #3번 버튼위에 텍스트 입히기
    DISPLAY.blit(btn,btn4_rect)         #4번 버튼 만들기
    DISPLAY.blit(text[3],textmenu_rect[3])  #4번 버튼위에 텍스트 입히기
    DISPLAY.blit(btn,btn5_rect)         #5번 버튼 만들기
    DISPLAY.blit(text[4],textmenu_rect[4])  #5번 버튼위에 텍스트 입히기

    pygame.draw.rect(DISPLAY, (255, 103, 129), (42, 5, 415, 600), 2) #화면 테두리 상자

    pygame.display.update()             #실행명령









#############################################################################################
# select_m = []
# select_m = ['한식','일식','중식','양식','기타']
# k_food = ['비빔밥','제육덮밥','김치찌개','된장찌개','냉면','돼지불백','칼국수','수제비','부대찌개','고등어조림','보쌈','뼈해장국','순대국']
# j_food = ['초밥','우동','스끼야끼','냉모밀','냉우동','도미조림','규동','가츠동','오니기리','라멘','오야꼬동']
# c_food = ['짜장면','짬뽕','탕수육','마파두부','깐풍기','라조기','마라탕','마라샹궈','고추잡채','볶음밥','양장피']
# w_food = ['오믈렛','오므라이스','스테이크','햄버거','치킨커틀릿','포크커틀릿','까르보나라','비프스튜','토마토파스타','바베큐폭립']
# etc_food = ['순대','떡볶이','김밥','라면','쌀국수','분짜','인도커리','팟타이','슈바인학센','다이어트는 어때...?','삼각김밥','편의점 도시락']
#
# name = []
# menu = []
# name = input('이름을 입력해 주세요 : ')
#
# def RandLunch():
#     while True:
#         ko = random.sample(k_food, 5)
#         ja = random.sample(j_food, 5)
#         ch = random.sample(c_food, 5)
#         we = random.sample(w_food, 5)
#         etc = random.sample(etc_food, 5)
#         menu = input('메뉴를 선택해 주세요\n''1.한식(korean)\n2.일식(Japanese)\n3.중식(Chinese)\n'
#                      '4.양식(Western)\n5.기타(etc)\n입력 : ')
#
#         if '한식' == menu:
#             print('%s님께 추천드리는 메뉴는...!!!' % name)
#             print(ko, '입니다!')
#             break
#
#         elif '일식' == menu:
#             print('%s님께 추천드리는 메뉴는...!!!' % name)
#             print(ja, '입니다!')
#             break
#
#         elif '중식' == menu:
#             print('%s님께 추천드리는 메뉴는...!!!' % name)
#             print( ch, '입니다!')
#             break
#
#         elif '양식' == menu:
#             print('%s님께 추천드리는 메뉴는...!!!' % name)
#             print(we,'입니다!')
#             break
#
#         elif '기타' == menu:
#             print('%s님께 추천드리는 메뉴는...!!!' % name)
#             print(etc, '입니다!')
#             break
#
# def ReTry():
#     while True:
#         retry = input('다시 뽑으시겠습니까? 예/아니오 : ')
#         if '예' == retry:
#             RandLunch()
#
# RandLunch()
# ReTry()