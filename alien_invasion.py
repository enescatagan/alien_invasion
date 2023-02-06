import sys

import pygame


class AlienInvation:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resouces."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # Set the background color.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Event Loop
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                # When player clicks window's close button
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible
            pygame.display.flip()


# Run if only file called directy
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvation()
    ai.run_game()
