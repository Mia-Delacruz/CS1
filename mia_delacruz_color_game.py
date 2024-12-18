import random                                                                   #import random 
                                                                                # 
def colored_text(text, color_name):
    color_codes = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[37m'
    }

    print(color_codes.get(color_name) + text + color_codes.get('reset'))

name = input('Enter your name: ')
print(name, ', the goal of this game is to enter the color of the code printed...')
colors = ['black', 'red']
colors = ['green','yellow']
colors= ['blue', 'magenta']
colors= ['white', 'cyan'] 
correct = 0
rounds = 0

while True:
    text_color = random.choice(colors)
    print_color = random.choice(colors)
    colored_text(text_color, print_color)
    user_color = input('Quick! Name the color of the text: ')

    if user_color == print_color:
        print('Right!')
        correct += 1
    else:
        print('Wrong!')
    
    rounds += 1

    while True:
        play_again = input(f"You have gotten {correct} out of {rounds} right! Would you like to play again? y/n: ")

        if play_again == 'y':
            break
        elif play_again == 'n':
            exit()
        else:
            print("Invalid response")

