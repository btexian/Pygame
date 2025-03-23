import pygame
import random
import math

# Game Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 500
BOX_COUNT = 5
FRUIT_IMAGES = ["apple.png", "banana.png", "orange.png"]
IMAGE_SIZE = (30, 30)  # Adjusted image size
FONT_SIZE = 36

# Box settings
BOX_SIZE = 100
BOX_PADDING = 30

class KidCountingGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Kid Counting Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, FONT_SIZE)

        self.load_images()
        self.new_round()

    def load_images(self):
        """Load and resize images."""
        self.images = {file: pygame.transform.scale(pygame.image.load(f"images/{file}"), IMAGE_SIZE) for file in FRUIT_IMAGES}

    def new_round(self):
        """Start a new game round with random object counts."""
        self.object_name = random.choice(FRUIT_IMAGES)
        self.object_image = self.images[self.object_name]
        self.box_counts = [random.randint(1, 5) for _ in range(BOX_COUNT)]
        self.correct_index = random.randint(0, BOX_COUNT - 1)
        self.correct_answer = self.box_counts[self.correct_index]

        # Generate answer options
        self.options = sorted(set(self.box_counts + [random.randint(1, 5) for _ in range(4)]))[:4]

    def draw_game(self):
        """Render the game UI."""
        self.screen.fill((240, 248, 255))  # Light Blue Background

        # Draw Game Title
        title_text = self.font.render("Kids Counting Game", True, (0, 0, 0))
        self.screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 20))

        # Draw Category Text
        category_text = self.font.render("Category: Fruits", True, (0, 0, 0))
        self.screen.blit(category_text, (SCREEN_WIDTH // 2 - category_text.get_width() // 2, 60))

        # Draw Boxes with Objects
        for i, count in enumerate(self.box_counts):
            box_x, box_y = 100 + i * 140, 150
            color = (172, 198, 79) if i == self.correct_index else (255, 255, 255)  # Green for red-box
            pygame.draw.rect(self.screen, color, (box_x, box_y, BOX_SIZE, BOX_SIZE), 0, 10)
            pygame.draw.rect(self.screen, (0, 0, 0), (box_x, box_y, BOX_SIZE, BOX_SIZE), 3, 10)

            # Arrange images inside the box
            cols = 3  # Max 3 images per row
            rows = math.ceil(count / cols)  # Number of rows needed

            for j in range(count):
                row, col = divmod(j, cols)
                img_x = box_x + 10 + col * (IMAGE_SIZE[0] + 5)  # Space images evenly
                img_y = box_y + 10 + row * (IMAGE_SIZE[1] + 5)
                self.screen.blit(self.object_image, (img_x, img_y))

        # Draw Answer Options
        for i, option in enumerate(self.options):
            button_x, button_y, button_w, button_h = 180 + i * 100, 350, 60, 50
            pygame.draw.rect(self.screen, (173, 216, 230), (button_x, button_y, button_w, button_h), 0, 5)
            pygame.draw.rect(self.screen, (0, 0, 0), (button_x, button_y, button_w, button_h), 2, 5)

            option_text = self.font.render(str(option), True, (0, 0, 0))
            self.screen.blit(option_text, (button_x + 20, button_y + 10))

        pygame.display.flip()

    def check_answer(self, mouse_x, mouse_y):
        """Check if the clicked answer is correct."""
        for i, option in enumerate(self.options):
            button_x, button_y, button_w, button_h = 180 + i * 100, 350, 60, 50
            if button_x <= mouse_x <= button_x + button_w and button_y <= mouse_y <= button_y + button_h:
                if option == self.correct_answer:
                    print("Correct!")
                else:
                    print("Try Again!")
                self.new_round()

    def run(self):
        """Main game loop."""
        running = True
        while running:
            self.screen.fill((240, 248, 255))
            self.draw_game()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    self.check_answer(mouse_x, mouse_y)

            self.clock.tick(30)

        pygame.quit()

if __name__ == "__main__":
    game = KidCountingGame()
    game.run()
