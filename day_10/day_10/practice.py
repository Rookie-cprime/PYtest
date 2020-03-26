"""
碰撞检测
pygame的sprite（动画精灵）模块就提供了对碰撞检测的支持
为了制造出更多的小球，我们可以通过对鼠标事件的处理
在点击鼠标的位置创建颜色、大小和移动速度都随机的小球
，我们可以把之前学习到的面向对象的知识应用起来
"""

from enum import Enum,unique
from math import sqrt
from random import randint

import pygame

@unique
class Color(Enum):
    RED = (255,0,0)
    GREEN=(0,255,0)
    BLUE = (0,0,255)
    BLACK=(0,0,0)
    WHITE=(255,255,255)
    GRAY=(242,242,242)

    @staticmethod
    def random_color():
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)

class Ball(object):

    def __init__(self,x,y,radius,sx,sy,color = Color.RED):
        self._x = x
        self._y = y
        self._radius = radius
        self._sx = sx
        self._sy = sy
        self._color = color
        self._alive = True
    def move(self,screen):
        self._x += self._sx
        self._y += self._sy
        if self._x - self._radius <= 0 or self._x + self._radius >= screen.get_width():
            self._sx    =   -self._sx
        if self._y - self._radius <= 0 or self._y + self._radius >= screen.get_height():
            self._sy    =   -self._sy
    def eat(self,other):
        if self._alive and other._alive and self != other:
            dx,dy=self._x - other._x,self._y - other._y
            distance = sqrt(dx**2+dy**2)
            if distance < self._radius + other._radius and self._radius > other._radius:
                other._alive = False
                self._radius = int(other._radius*0.16) + self._radius
    def draw(self,screen):
        pygame.draw.circle(screen,self._color,(self._x,self._y),self._radius,0)
def main():
    # 定义用来装所有球的容器
    balls = []
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('big eat small')
    running = True
     # 开启一个事件循环处理发生的事件
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running == False
         # 处理鼠标事件的代码
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # 获得点击鼠标的位置
                x,y = event.pos
                radius = randint(10,100)
                sx, sy = randint(-10, 10), randint(-10, 10)
                color = Color.random_color()
                ball = Ball(x,y,radius,sx,sy,color)
                 # 将球添加到列表容器中
                balls.append(ball)
        screen.fill((255,255,255))
         # 取出容器中的球 如果没被吃掉就绘制 被吃掉了就移除
        for ball in balls:
            if ball._alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        pygame.display.flip()
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            for other in balls:
                ball.eat(other)

if __name__ == '__main__':
    main()


