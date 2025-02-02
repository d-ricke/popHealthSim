import sys
import pygame
from person import Person
from medicalIssue import MedicalIssue
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


def main():
    #initialisaion
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() #not sure if we need the clock here
    #add a game date

    updatable = pygame.sprite.Group() # at least at first we'll mostly rely on updating data-only objects
    drawable = pygame.sprite.Group() #and perhaps add more of a dashboard-like interface?

    persons = pygame.sprite.Group()
    Persons.containers = (persons, updatable)

    dt = 0

    # Game Loop ----------
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for thing in updatable:
            thing.update(dt=dt)

        screen.fill("black")

        for thing in drawable:
            thing.draw(screen)
        
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()