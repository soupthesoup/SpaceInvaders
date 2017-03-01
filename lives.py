initialLives = [
    "LLL"
    ]
for row in initialLives:
    for col in row:
        if col == "L":
            lifeRect = pygame.Rect(lx,ly,20,20)
            Lives.append(lifeRect)
        lx += 25
    for alienBullet in alienBulletArray:
        if alienBullet.colliderect(shipRect):
            initialLives.remove
        
for life in initialLives:
    pygame.draw.rect(screen, White, life, 0)
        for alienBullet in alienBulletArray:
        if alienBullet.colliderect(shipRect):
            alienBullet.remove(alienBullet)
            initialLives.remove(life)
    

