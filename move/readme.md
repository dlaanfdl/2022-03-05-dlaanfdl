# 물리융합 코딩예제

### pygame 세팅

> 🔥 `pygame`을 현재 python 파일에 적용하는 방법

```python
import pygame

pygame.init()
```

### Screen 세팅

> 🔥 `Screen`에 원 그려넣기

```python
SCREEN_WIDTH = 1080   📝가로길이
SCREEN_HEIGHT = 720   📝세로길이

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True
while run:
    screen.fill((70, 150, 255)📝Screen색깔)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.circle(screen, (255, 255, 255), (xpos, ypos), 60)

    pygame.display.update()
```

### 등속도 운동

> 🔥 원을 등속도 운동시키기

```
xpos = 0
ypos = SCREEN_HEIGHT

xspeed = SCREEN_WIDTH * 0.0001    📝x방향 속도
yspeed = SCREEN_HEIGHT * -0.0001  📝y방향 속도

run = True
while run:
    screen.fill((30, 150, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.circle(screen, (255, 255, 255), (xpos, ypos), 60)

    xpos = xpos + xspeed   📝등속도 운동하기 위해 좌표에 속도더하기
    ypos = ypos + yspeed

    pygame.display.update()
```

### 등가속도 운동

> 🔥 원을 등가속도 운동시키기(낙하)

```
SCREEN_WIDTH = 340
SCREEN_HEIGHT = 720

xpos = SCREEN_WIDTH/2
ypos = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True
while run:
    screen.fill((70, 150, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    yspeed += gravity
    ypos += yspeed

    pygame.draw.circle(screen, (255, 255, 255), (xpos, ypos), 20)

    pygame.display.update()
```

> ➕ 공기저항 추가하기

```
✅ yspeed = 0.001
✅ gravity = 0.0001
✅ resist = 0.9998

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True
while run:
    screen.fill((70, 150, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

✅  gravity *= resist
    yspeed += gravity
    ypos += yspeed

    pygame.draw.circle(screen, (255, 255, 255), (xpos, ypos), 20)

    pygame.display.update()
```
