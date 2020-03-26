import  pygame
def main():
    # 初始化导入的pygame中的模块
    pygame.init()
    screen  =   pygame.display.set_mode((800,600))
     # 设置当前窗口的标题
    pygame.display.set_caption("big ball eat little ball")
    x,y =   50,50
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running == False
        screen.fill((255,255,255))
        pygame.draw.circle(screen,(255,0,0),(x,y),30,0)
        pygame.display.flip()
        # 每隔50毫秒就改变小球的位置再刷新窗口
        pygame.time.delay(50)
        x,y = x+5,y+5

if __name__ == '__main__':
    main()
