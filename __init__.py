import pygame,os,random,time
def message_diaplay(text):
    largeText=pygame.font.SysFont('SimHei',32)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((1000/2),(500/2))
    scr.blit(TextSurf, TextRect)
    pygame.display.update()
    global overd
    pygame.display.update()
def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,155))
    return textSurface, textSurface.get_rect()
pygame.init()
scr=pygame.display.set_mode([1000,500],pygame.FULLSCREEN)
message_diaplay('无论何时，按任意键即可退出。准备，开始！')
time.sleep(2)
scr.fill((255,255,255))
pygame.display.update()
overd=False
jifen=0
def outside(pos):
    return pos[0]==0 or pos[0]==999 or pos[1]==499 or pos[1]==0
try:
    while True:
        for i in pygame.event.get():
            if i.type==pygame.KEYDOWN:
                pygame.quit()
                break
            if i.type==pygame.MOUSEMOTION:
                if outside(pygame.mouse.get_pos()):
                    if not overd:
                        message_diaplay('Game over!积分为'+str(jifen))
                        overd=True
                else:
                    jifen+=sum(map(abs,pygame.mouse.get_rel()))
except:
    pass
