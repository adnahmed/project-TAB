def RUN(window):
    import pygame
    from pygame import mixer
    import os
    pygame.init()
    mixer.init()
    mixer.music.load("links\\home\\A.wav")
    mixer.music.set_volume(1)
    pygame.display.set_caption("home")
    
    speed = [10, 10]
    clock = pygame.time.Clock()
    logo = pygame.image.load("links\\home\\a.png")
    rect = logo.get_rect()
    
    fps = 60
    size = width, height = 800, 500
    screen = pygame.display.set_mode(size)
    programIcon = pygame.image.load('icons\\tab.png')
    pygame.display.set_icon(programIcon)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if rect.left < 0:
            speed[0] = -speed[0]
            logo = pygame.image.load("links\\home\\aa.png")
            mixer.music.play()
        if rect.right > width:
            speed[0] = -speed[0]
            logo = pygame.image.load("links\\home\\a.png")
            mixer.music.play()
        if rect.top < 0:
            speed[1] = -speed[1]
            logo = pygame.image.load("links\\home\\aaa.png")
            mixer.music.play()
        if rect.bottom > height:
            speed[1] = -speed[1]
            logo = pygame.image.load("links\\home\\aaaa.png")
            mixer.music.play()
        rect.left += speed[0]
        rect.top += speed[1]
        screen.fill((0, 0, 0))
        screen.blit(logo, rect)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()