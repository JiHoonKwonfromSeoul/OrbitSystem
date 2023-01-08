import pygame
import sys
import numpy as np
import math
import os

# 게임 윈도우 크기
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080

# 색 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (34, 139, 34)
BLUE = (0, 0, 255)
SKYBLUE=(135,206,235)
DEEPBROWN=(101,67,33)

#함수:로테이션과 이동, 함수변경

def Rmat(degree):
    radian = np.deg2rad(degree)
    c = np.cos(radian)
    s = np.sin(radian)
    R = np.array( [[ c, -s, 0], [s, c, 0], [0, 0, 1] ] )
    return R

def Tmat(a,b):
    H = np.eye(3)
    H[0,2] = a
    H[1,2] = b
    return H

# Pygame 초기화
pygame.init()

# 윈도우 제목
pygame.display.set_caption("20171829Kwon_SolarSystem")

# 윈도우 생성
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 게임 화면 업데이트 속도
clock = pygame.time.Clock()

# assets 경로 설정
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')

#이미지 로드
sun_img=pygame.image.load(os.path.join(assets_path,'sun.jpg'))
sun_img=pygame.transform.scale(sun_img,(778*0.1,580*0.1))
sun_rect=sun_img.get_rect()
sun_rect.x=WINDOW_WIDTH/2
sun_rect.y=WINDOW_HEIGHT/2

# 게임 종료 전까지 반복
done = False

# poly: 4 x 3 matrix
#poly = np.array( [[0, 0, 1], [80, 20, 1], [100, 0, 1], [80, -20, 1]])
#poly = poly.T
#cor=np.array([10,10,1])
#degree=10

# 폰트 선택(폰트, 크기, 두껍게, 기울기)
font = pygame.font.SysFont('arial', 20, True, True)

# 게임 반복 구간
while not done:
# 이벤트 반복 구간
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True



    # 윈도우 화면 채우기
    screen.fill(BLACK)
    screen.blit(sun_img,sun_rect)

    # 이미지 그리기


    # 화면 업데이트
    pygame.display.flip()
    clock.tick(60)

# 게임 종료
pygame.quit()
