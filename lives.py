for row in initialLives:
    for col in row:
        if col == "L":
            lifeRect = pygame.Rect(lx,ly,20,20)
            Lives.append(lifeRect)
        lx += 25
        
for life in initialLives:
