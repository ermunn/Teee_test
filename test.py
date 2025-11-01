import pygame

pygame.init()

x = 250
y = 150


screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("My game")

clock = pygame.time.Clock()

running = True

while running:
  clock.tick(60)
  for event in pygame.event.get():
     if event.type == pygame.QUIT:
       running = False


  screen.fill((255, 255, 255))
  pygame.draw.rect(screen, (0, 255, 0), (x ,y, 100, 100))
  #pygame.draw.circle(screen, (255, 0, 0), (300, 200), 40)
  
  keys = pygame.key.get_pressed()
  if keys [pygame.K_LEFT]:
      x -= 5
      print("escape key pressed")


  pygame.display.flip()
  #if event.type == pygame.MOUSEBUTTONDOWN:
   # x, y = pygame.mouse.get_pos()
   # print(f"Mouse clicked at ({x}, {y})")
  

pygame.quit()