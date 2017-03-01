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
    credit = False
    
    #Fonts
    MainFont = pygame.font.SysFont("futura",200)
    SubFont = pygame.font.SysFont("futura",50)
    TFont = pygame.font.SysFont("futura",100)
    TFont.set_underline(1)
    InfoFont = pygame.font.SysFont("futura",36)
    GLFont = pygame.font.SysFont("futura",100)

    #Words and Rendering
    SpaceTitle1 = MainFont.render("Space",True,White)
    SpaceTitle2 = MainFont.render("Invaders", True, White)
    Names = SubFont.render("By Dylan, Matt and Jackson",True, White)
    Info = SubFont.render("Press I for Game Info",True,White)
    Credits = SubFont.render("Press C for Credits",True,White)
    Start = SubFont.render("Press Space to Play", True, White)
    Exit = SubFont.render("Press Q to Quit",True,White)
    ITitle = TFont.render("Info", True, White)
    AL1Info = InfoFont.render("Shoot for 100 Points", True, White)
    AL2Info = InfoFont.render("Shoot for 20 Points", True, White)
    AL3Info = InfoFont.render("Shoot for 40 Points", True, White)
    SHIPInfo = InfoFont.render("Left and Right Arrows to move, Up Arrow to shoot", True, White)
    BarInfo = InfoFont.render("Hide behind your barriers, any bullets will slowly break them.", True, White)
    Info1 = InfoFont.render("Shoot all Aliens to end the round,", True, White)
    Info2 = InfoFont.render("you will gain a life every round.",True, White)
    Info3 = InfoFont.render("Try to get a large score before losing.", True, White)
    GL = GLFont.render("Good Luck", True, White)
    RETURN = InfoFont.render("Press R to return to Main menu",True, White)
    
    #Sprites
    AL1a = pygame.image.load("Alien1a.png") #64x64
    AL1b = pygame.image.load("Alien1b.png") #64x64
    AL2a = pygame.image.load("Alien2a.png") #96x64
    AL2b = pygame.image.load("Alien2b.png") #96x64
    AL3a = pygame.image.load("Alien3a.png") #88x64
    AL3b = pygame.image.load("Alien3b.png") #88x64
    SHIP = pygame.image.load("SpaceGun.png")

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
    SIW = SHIPInfo.get_width()
    BIW = BarInfo.get_width()
    GunW = SHIP.get_width()

    AClock = pygame.time.Clock() #Clock variables
    ACount = 0

    num = -1
    bx1 = 150
    bx2 = 350
    bx3 = 550
    bx4 = 750
    by = 400
    barrier1 = []
    barrier2 = []
    barrier3 = []
    barrier4 = []
    Gunx = 435
    Guny = 250
    Gundx = 5
    
    barrier = [
        "WWWWWWWWWWWWWWWWWWWW",
        "WWWWWWWWWWWWWWWWWWWW",
        "WWWWWWWWWWWWWWWWWWWW",
        "WWWWW          WWWWW",
        ]

    for row in barrier:
        for col in row:
            if col == "W":
                wallR1 = pygame.Rect(bx1,by,5,10)
                barrier1.append(wallR1)
                wallR2 = pygame.Rect(bx2,by,5,10)
                barrier2.append(wallR2)
                wallR3 = pygame.Rect(bx3,by,5,10)
                barrier3.append(wallR3)
                wallR4 = pygame.Rect(bx4,by,5,10)
                barrier4.append(wallR4)
            bx1 += 5
            bx2 += 5
            bx3 += 5
            bx4 += 5
        by += 10
        bx1 = 150
        bx2 = 350
        bx3 = 550
        bx4 = 750
        
    while title:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                title = False
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    terminate()
                elif event.key == pygame.K_i:
                    info = True
                elif event.key == pygame.K_c:
                    credit = True
                elif event.key == pygame.K_SPACE:
                    title = False

        ACount = ACount + AClock.tick() #using clock to determing variables
        if ACount >= 500:
            num = num * -1
            ACount = 0
                    
        screen.fill(Black) #All the drawing and such
        screen.blit(SpaceTitle1,((500 - ST1W / 2), 100))
        screen.blit(SpaceTitle2,((500 - ST2W / 2),100 + ST1H))
        screen.blit(Names,((500 - NW / 2), 100 + ST1H + ST2H))
        screen.blit(Start,((500 - SW / 2), 200 + ST1H + ST2H))
        screen.blit(Info,((500 - IW / 2), 200 + ST1H + ST2H + SH))
        screen.blit(Exit,((500 - EW / 2), 200 + ST1H + ST2H + SH + IH))
        if num <= 0:
            screen.blit(AL1a, (75,100))
            screen.blit(AL2a, (59,200))
            screen.blit(AL3a, (64,300))
            screen.blit(AL1a, (75,400))
            screen.blit(AL2a, (59,500))
            screen.blit(AL3a, (64,600))
            screen.blit(AL1a, (861,100))
            screen.blit(AL2a, (845,200))
            screen.blit(AL3a, (848,300))
            screen.blit(AL1a, (861,400))
            screen.blit(AL2a, (845,500))
            screen.blit(AL3a, (848,600))
            
        elif num >=0:
            screen.blit(AL1b, (75,100))
            screen.blit(AL2b, (59,200))
            screen.blit(AL3b, (64,300))
            screen.blit(AL1b, (75,400))
            screen.blit(AL2b, (59,500))
            screen.blit(AL3b, (64,600))
            screen.blit(AL1b, (861,100))
            screen.blit(AL2b, (845,200))
            screen.blit(AL3b, (848,300))
            screen.blit(AL1b, (861,400))
            screen.blit(AL2b, (845,500))
            screen.blit(AL3b, (848,600))
        pygame.display.update()
        
        while info:
            ACount = ACount + AClock.tick() #clock stuff
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        info = False
                        
            if ACount >= 500: #more clock
                num = num * -1
                ACount = 0

            Gunx = Gunx + Gundx

            if Gunx <= 10 or Gunx >= 790 + GunW - 35:
                Gundx = Gundx * -1
                
            screen.fill(Black)
            screen.blit(ITitle,((500 - ITW / 2), 30))
            if num < 0:
                screen.blit(AL1a,(100,125))
                screen.blit(AL2a,(450,125))
                screen.blit(AL3a,(800,125))
            if num > 0:
                screen.blit(AL1b,(100,125))
                screen.blit(AL2b,(450,125))
                screen.blit(AL3b,(800,125))
            screen.blit(AL1Info,(25, 200))
            screen.blit(AL2Info,(375,200))
            screen.blit(AL3Info,(725,200))
            screen.blit(SHIP,(Gunx,Guny))
            screen.blit(SHIPInfo,((500 - SIW / 2),330))
            for WALL1 in barrier1:
                pygame.draw.rect(screen,Green,WALL1,0)
            for WALL2 in barrier2:
                pygame.draw.rect(screen,Green,WALL2,0)
            for WALL3 in barrier3:
                pygame.draw.rect(screen,Green,WALL3,0)
            for WALL4 in barrier4:
                pygame.draw.rect(screen,Green,WALL4,0)
            screen.blit(BarInfo,((150),475))
            screen.blit(Info1,(300,525))
            screen.blit(Info2,(315,550))
            screen.blit(Info3,(275,575))
            screen.blit(GL,(325,625))
            screen.blit(RETURN,(25,700))
            pygame.display.update()
