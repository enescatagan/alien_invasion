import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvation:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resouces."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        # Event Loop
        for event in pygame.event.get():
            # When player clicks window's close button
            if event.type == pygame.QUIT:
                sys.exit()

            # Check KEYDOWN Events
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            # Check KEYUP Events
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the ship to the left.
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            # Exit game
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            # Stop the ship's right movement.
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # Stop the ship's left movement.
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet position.
        self.bullets.update()

        # Get rid of bullets that have dsappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        # Make an alien for calculations
        alien = Alien(self)
        alien_width = alien.rect.width
        # Calculate how many aliens fit in horizontal space
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Create the first row of aliens.
        for alien_number in range(number_aliens_x):
            self._create_alien(alien_number)

    def _create_alien(self, alien_number):
        """Create an alien and place it in the row"""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        self.aliens.add(alien)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)

        # Draw ship
        self.ship.blitme()

        # Draw fired bullets to the screen
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Draw aliens
        self.aliens.draw(self.screen)

        # Make the most recently drawn screen visible
        pygame.display.flip()


# Run if only file called directy
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvation()
    ai.run_game()
