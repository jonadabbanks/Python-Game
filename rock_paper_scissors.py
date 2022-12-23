import random
import tkinter as tk

# Returns a random choice from 'rock', 'paper', or 'scissors'
def get_ai_choice():
  choices = ['rock', 'paper', 'scissors']
  return random.choice(choices)

# Determines the result of a game based on the two players' choices
# Returns 'Tie', 'Player 1 wins', or 'Player 2 wins'
def play_game(player1_choice, player2_choice):
  if player1_choice == player2_choice:
    return 'Tie'
  elif player1_choice == 'rock' and player2_choice == 'scissors':
    return 'Player 1 wins'
  elif player1_choice == 'scissors' and player2_choice == 'paper':
    return 'Player 1 wins'
  elif player1_choice == 'paper' and player2_choice == 'rock':
    return 'Player 1 wins'
  else:
    return 'Player 2 wins'

# GUI application class
class RockPaperScissorsApp(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title('Rock Paper Scissors')
    self.geometry('300x200')

    self.result_text = tk.StringVar()
    self.result_label = tk.Label(self, textvariable=self.result_text)
    self.result_label.pack()

    self.rock_button = tk.Button(self, text='Rock', command=lambda: self.play('rock'))
    self.rock_button.pack()
    self.paper_button = tk.Button(self, text='Paper', command=lambda: self.play('paper'))
    self.paper_button.pack()
    self.scissors_button = tk.Button(self, text='Scissors', command=lambda: self.play('scissors'))
    self.scissors_button.pack()

  # Plays a game against the AI and updates the result label
  def play(self, player_choice):
    ai_choice = get_ai_choice()
    result = play_game(player_choice, ai_choice)
    self.result_text.set(f'You chose {player_choice}, AI chose {ai_choice}\nResult: {result}')

if __name__ == '__main__':
  app = RockPaperScissorsApp()
  app.mainloop()
