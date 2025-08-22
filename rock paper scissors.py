import pygame
import random
import sys

pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")
font = pygame.font.SysFont(None, 40)

# Choices and buttons
choices = ["rock", "paper", "scissors"]
buttons = [pygame.Rect(80 + i * 160, 280, 130, 60) for i in range(3)]

# Game state
player_choice = ""
computer_choice = ""
result = ""

def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    rules = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
    return "You win!" if rules[player] == computer else "Computer wins!"

# Main game loop
while True:
    screen.fill((245, 245, 245))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for i, button in enumerate(buttons):
                if button.collidepoint(event.pos):
                    player_choice = choices[i]
                    computer_choice = random.choice(choices)
                    result = get_winner(player_choice, computer_choice)

    # Title
    title = font.render("Rock Paper Scissors", True, (0, 0, 128))
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 40))

    # Draw buttons
    for i, button in enumerate(buttons):
        pygame.draw.rect(screen, (200, 200, 200), button, border_radius=10)
        choice_text = font.render(choices[i].capitalize(), True, (0, 0, 0))
        text_rect = choice_text.get_rect(center=button.center)
        screen.blit(choice_text, text_rect)

    # Show results if player has played
    if player_choice:
        pc_text = font.render(f"You: {player_choice.capitalize()}", True, (0, 128, 0))
        cc_text = font.render(f"Computer: {computer_choice.capitalize()}", True, (128, 0, 0))
        result_text = font.render(result, True, (0, 0, 0))

        screen.blit(pc_text, (50, 150))
        screen.blit(cc_text, (50, 190))
        screen.blit(result_text, (50, 230))

    pygame.display.flip()
