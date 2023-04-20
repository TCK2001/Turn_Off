import pygame
import silence_tk as st
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("on or off")
root.geometry("170x50")

turnoff = 1
def on_phone():
    global turnoff
    turnoff = 1

def off_phone():
    global turnoff
    turnoff= 0


on_btn = tk.Button(root, text="ON", font=("Helvetica", 16), width=5, height=1,command=on_phone)
off_btn = tk.Button(root, text="OFF", font=("Helvetica", 16), width=5, height=1,command=off_phone)
on_btn.place(x=0, y=0)
off_btn.place(x=100,y=0)


# 초기화
pygame.init()
width, height = 250, 400
# 창 크기 설정
screen = pygame.display.set_mode((width, height))

# 창 제목 설정
pygame.display.set_caption("Moving Dot")

# 케릭터 생성
dot_size = 10
dot_color = (0, 0, 0)
dot_pos = [300, 300]
# 텍스트 폰트 설정
font = pygame.font.SysFont("Arial", 20)

# 색상 설정
white = (255, 255, 255)
black = (0, 0, 0)

# 텍스트 생성
text = font.render("Turn off the phone call", True, black)
company_text = font.render("company", True, black)
now_phone = font.render("Phone alert was turn on",True, black)
off_phone = font.render("Turn on",True, black)
# 이동 속도
speed = 0.05
black = (0, 0, 0)
goal = 0
# 게임 루프
running = True
while running:

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 방향키 처리
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        dot_pos[0] -= speed
    if keys[pygame.K_RIGHT]:
        dot_pos[0] += speed
    if keys[pygame.K_UP]:
        dot_pos[1] -= speed
    if keys[pygame.K_DOWN]:
        dot_pos[1] += speed

    # 케릭터가 창 밖으로 벗어나지 않도록 제한
    if dot_pos[0] < dot_size:
        dot_pos[0] = dot_size
    elif dot_pos[0] > width - dot_size:
        dot_pos[0] = width - dot_size
    if dot_pos[1] < dot_size:
        dot_pos[1] = dot_size
    elif dot_pos[1] > height - dot_size:
        dot_pos[1] = height - dot_size
        
    # 배경 색 채우기
    screen.fill((255, 255, 255))

    # 케릭터 그리기
    pygame.draw.circle(screen, dot_color, dot_pos, dot_size)
    
   # 사각형 그리기
    pygame.draw.rect(screen, black, (0, 0, 100, 100), 2)
    pygame.draw.rect(screen, white, (2, 2, 96, 96))
    
    screen.blit(company_text, (20, 100))
    if dot_pos[0] <= 120 and dot_pos[1] <= 120:
        screen.blit(text, (0, 300))
        root.mainloop()
        
    if dot_pos[0] <= 100 and dot_pos[1] <= 100:
        if turnoff == 0:
            messagebox.showinfo("Game Clear", "You have completed the meeting with ease.")
        else:
            st.run_tk()
        running = False
        
    screen.blit(now_phone, (0, 330))
    # 화면 업데이트
    pygame.display.update()
pygame.quit()