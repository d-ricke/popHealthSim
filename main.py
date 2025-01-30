import sys
import pygame
from person import Person


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

    


if __name__ == "__main__":
    main()