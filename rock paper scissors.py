import  pygame,random,sys
pygame.init()
WIDTH,HEIGHT = 600,400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("rock paper scissors")  
font = pygame.font.SysFont(None, 36)
choices = [ "rock", "paper", "scissors"]
buttons = [pygame.React(80+i*160,280,130,60, choices[i]) for i in range(3)]
player_choice = ""
computer_choice = ""
result = ""
def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    rules = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    return "You win!" if rules[player] == computer else "You lose!"
while True:
    SCREEN.fill((245,245,245))
    title = font.render("Rock Paper Scissors", True, (0, 0, 128))
    SCREEN.blit(title, (WIDTH//2 - title.get_width()//2, 20))