import pygame, sys
from pygame.locals import*
# def select(pi):
pygame.init()
DISPLAY = pygame.display.set_mode((500,650)) #디스플레이(윈도우) 크기 설정
pygame.display.set_caption('RANDOM LUNCH')   #디스플레이 이름 설정(상태바에 표시)

btn = pygame.image.load("button_1.png") #버튼 이미지 불러오기
btn1_rect = btn.get_rect(center=(250,250)) #이미지로 불러온 버튼 좌표
btn2_rect = btn.get_rect(center=(250,320))
btn3_rect = btn.get_rect(center=(250,390))
btn4_rect = btn.get_rect(center=(250,460))
btn5_rect = btn.get_rect(center=(250,530))

btn1 = pygame.image.load("button_2.png")
Rebtn_rect = btn.get_rect(center=(365,570))

#-----------------------------------------------------------------------------------
font = pygame.font.Font('NanumSquareRoundB.ttf',20) #텍스트 폰트 및 크기설정
font2 = pygame.font.Font('NanumSquareRoundB.ttf',37)
font3 = pygame.font.Font('NanumSquareRoundB.ttf',22)

text = [font.render('한식',True,(255,255,255)),font.render("일식",True,(255,255,255)), #텍스트,텍스트 색깔 설정
        font.render('중식',True,(255,255,255)),font.render('양식',True,(255,255,255)),
        font.render('기타',True,(255,255,255)),font.render('다시뽑기',True,(255,255,255))]

text_2 = [font2.render('당신에게 추천하는 음식은',True,(0,0,0)),
          font2.render('이 5가지 입니다!',True,(0,0,0))]

textmenu_rect = [text[0].get_rect(center=(250,250)),text[0].get_rect(center=(250,320)), #텍스트 좌표 설정
             text[0].get_rect(center=(250,390)),text[0].get_rect(center=(250,460)),
             text[0].get_rect(center=(250,530)),text[0].get_rect(center=(235,615))]

textmain_rect = [text[0].get_rect(center=(70,80)),text[0].get_rect(center=(130,130))]

#-----------------------------------------------------------------------------------
while True:
    for event in pygame.event.get(): #이벤트 설정

        if event.type == QUIT: #종료 이벤트 설정
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:      #마우스버튼 누르고 띄었을 때 이벤트 발생
            if Rebtn_rect.collidepoint(event.pos):   #각 버튼마다 이벤트 설정
                pass


    DISPLAY.fill((255,255,255))         #디스플레이(윈도우창)색깔 설정
    DISPLAY.blit(text_2[0], textmain_rect[0])
    DISPLAY.blit(text_2[1], textmain_rect[1])


    pygame.draw.rect(DISPLAY, (255, 103, 129), (42, 5, 415, 600), 2)

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
    DISPLAY.blit(btn1,Rebtn_rect)
    DISPLAY.blit(text[5],textmenu_rect[5])

    pygame.display.update()             #실행명령