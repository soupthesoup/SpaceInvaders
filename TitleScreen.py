import pygame
import sys

pygame.init()

size = (1000,800)
screen = pygame.display.set_mode(size)

White = (255,255,255)
Black = (0,0,0)
Red = (255,51,51)
Green = (0,255,0)
Blue = (0,0,255)

def terminate():
    pygame.quit()
    sys.exit()

def TitleScreen():
    title = True 
    info = False
    start = False
    
    #Fonts
    MainFont = pygame.font.SysFont("futura",200)
    SubFont = pygame.font.SysFont("futura",50)
    TFont = pygame.font.SysFont("futura",100)
    TFont.set_underline(1)

    #Words and Rendering
    SpaceTitle1 = MainFont.render("Space",True,White)
    SpaceTitle2 = MainFont.render("Invaders", True, White)
    Names = SubFont.render("By Dylan, Matt and Jackson",True, White)
    Info = SubFont.render("Press I for Game Info",True,White)
    Credits = SubFont.render("Press C for Credits",True,White)
    Start = SubFont.render("Press Space to Play", True, White)
    Exit = SubFont.render("Press Q to Quit",True,White)
    ITitle = TFont.render("Info", True, White)

    #Sprites
    AL1a = pygame.image.load("Alien1a.png")
    AL1b = pygame.image.load("Alien1b.png")
    AL2a = pygame.image.load("Alien2a.png")
    AL2b = pygame.image.load("Alien2b.png")
    AL3a = pygame.image.load("Alien3a.png")
    AL3b = pygame.image.load("Alien3b.png")

    ST1H = SpaceTitle1.get_height() #Title measurements
    ST1W = SpaceTitle1.get_width()  
    ST2H = SpaceTitle2.get_height() 
    ST2W = SpaceTitle2.get_width()  
    NW = Names.get_width() 
    SH = Start.get_height()
    SW = Start.get_width()
    IH = Info.get_height()
    IW = Info.get_width()
    CH = Credits.get_height()  #You can do CreditsPosition = Credits.get_rect(center(1000/2, 800/2))   1000 being screen width, 800 being screen hieght. This will center
    CW = Credits.get_width() #the text and you can add value to those devisions to move it up/down left/right easily and still be centered.
    EH = Exit.get_height()
    EW = Exit.get_width()
    ITW = ITitle.get_width()

    AClock = pygame.time.Clock() #Clock variables
    ACount = 0

    num = -1 
    
    while title:
        AClock = pygame.time.Clock()
        ACount = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                title = False
                terminate()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    terminate()
                elif event.key == pygame.K_i:
                    info = True
                    
        screen.fill(Black)
        screen.blit(SpaceTitle1,((500 - ST1W / 2), 100))
        screen.blit(SpaceTitle2,((500 - ST2W / 2),100 + ST1H))
        screen.blit(Names,((500 - NW / 2), 100 + ST1H + ST2H))
        screen.blit(Start,((500 - SW / 2), 200 + ST1H + ST2H))
        screen.blit(Info,((500 - IW / 2), 200 + ST1H + ST2H + SH))
        screen.blit(Credits,((500 - CW / 2), 200 + ST1H + ST2H + SH + IH))
        screen.blit(Exit,((500 - EW / 2), 200 + ST1H + ST2H + SH + IH + CH))
        pygame.draw.rect(screen, White, (0,0,1000,800), 10)
        pygame.display.update()
        
        while info:
            ACount = ACount + AClock.tick()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        info = False
                        
            if ACount >= 1000:
                num = num * -1
                print num
                ACount = 0
                
            screen.fill(Black)
            screen.blit(ITitle,((500 - ITW / 2), 30))
            if num < 0:
                screen.blit(AL1a,(50,50))
            if num > 0:
                screen.blit(AL1b,(50,50))
            #pygame.draw.rect(screen, White, (0,0,1000,800), 10) #what's the point of filling the screen with black and then filling it with white?
            pygame.display.update()
                    

TitleScreen()       
        
    
    
