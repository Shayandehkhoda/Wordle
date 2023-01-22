## How to Run

- Clone the repo.
- Install the requirements by running `pip install -r requirements.txt`.
- In your terminal, run `export PYTHONPATH=$PYTHONPATH:$(pwd)` to add the current directory to your `PYTHONPATH`.
- Run `python src/main.py` to start the game.
- You can change number of tries.

## Rules

- enter a random 5-letter word.
- If the random word is the word to be guessed, then you win.
- If the random word isn’t the word to be guessed, the player is informed about whether the right letter is at the right place and if some of the letters are in the word but wrongly placed.
- Based on this, the player has 6 tries to guess the word.
