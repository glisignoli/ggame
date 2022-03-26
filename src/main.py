from unicodedata import name


class main:
    def __init__(self):
        self.__main()

    def __main(self):
        import pygame
        from config import Config
        from gui import GUI
        from player import Player
        from gcolors import GColor

        # Read config
        config = Config().config

        # Initalise pygame and screen
        pygame.init()
        screen = pygame.display.set_mode((int(config['DEFAULT']['screen_width']), int(config['DEFAULT']['screen_height'])))

        # Initalise game objects
        gui = GUI()
        
        player1 = Player(name='Player 1', color=GColor.WHITE.tupple_format(), x_pos=700, y_pos=700, rotation=0)

        clock = pygame.time.Clock()

        # Main loop
        carryOn = True

        while carryOn:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        carryOn = False
            
            # Clear the screen
            screen.fill((0, 0, 0))

            # Update the sprites
            #gui.spritegroup.update()
            player1.spritegroup.update()

            # Draw the screen
            #gui.spritegroup.draw(screen)
            player1.spritegroup.draw(screen)

            # Replace the current screen with the new screen
            pygame.display.flip()

            clock.tick(60)

        pygame.quit()

if __name__ == '__main__':
    from main import main
    main()
