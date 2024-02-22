import os
import random

# preparations
##############
INTRO = r"""
   ^                 ^     
  / \    LOCKED     / \    
 /   \             /   \   
(_____)           (_____)  
 |   |  _   _   _  |   |   
 | O |_| |_| |_| |_| O |   
 |   |   - _^_     |   |   
 |  _|    //|\\  - |   |   
 |   |   ///|\\\   |  -|   
 |-  |_  |||||||   |   |   
 |___|___|||||||___|___|   
       (         (         
        \         \        
         )         )       
         |         |       
         (         )       
         /        /       
"""
STAGES = [
    r"""
            *      `.       \   |     *     /    *      '
  .                  \      |   \          /               *
     *'  *     '      \      \   '.       |
        -._            `      \    |      /         *
  ' '      ``._   *     \     |    |             '          .      '
   *           *\*       \   * .   .      *
*  '        *    `-._                       .         _..:='        *
             .  '      *       *    *   .       _.:--'
          *           .     .     *         .-'         *
   .               '          GAME OVER   *           *         .
  *       ___.-=--..-._     *                '               '
                                  *       *
                *        _.'  .'       `.        '  *             *
     *              *_.-'   .'            `.               *
                   .'                       `._             *  '
   '       '    *         *         .       .  `.     .
       .                      *                  `
               *        '             '                          .
     .                          *        .           *  *           '
""",
    r"""






                    . : .
      ____________'.  :  .'
     /  Dynamite ./\'.:.'  .
     \___________.\/.':'.  .
                   '  :  '.
                    ' : '





""",
    r"""






                       . : .
      _____________  '.  :  .'
     /  Dynamite  /\.__'.:.'  .
     \____________\/.  .':'.  .
                     .'  :  '.
                       ' : '





""",
    r"""






                         . : .
      _____________    '.  :  .'
     /  Dynamite  /\__.__'.:.'  .
     \____________\/  .  .':'.  .
                       .'  :  '.
                         ' : '





""",
    r"""






                           . : .
      _____________      '.  :  .'
     /  Dynamite  /\____.__'.:.'  .
     \____________\/    .  .':'.  .
                         .'  :  '.
                           ' : '





""",
    r"""






                            (
      _____________         )\
     /  Dynamite  /\________{,}
     \____________\/         |
                             |






""",
]
ESCAPE = r"""
   ^                 ^     
  / \    ESCAPED    / \    
 /   \   You Win   /   \   
(_____)           (_____)  
 |   |  _   _   _  |   |   
 | O |_| |_| |_| |_| O |   
 |   |   - _^_     |   |   
 |  _|    //|\\  - |   |   
 |   |   ///|\\\   |  -|   
 |-  |_  ||   ||   |   |    
 |___|___||   ||___|___|   
       (         (         
        \         \        
         ) _O/     )       
         |   \     |       
         (   /\_   )       
         /   \  `  /       
"""
secret_words = ["circus", "goalkeeper", "workspace"]
# secret_words = ["hey"]

random_choice = random.randint(0, len(secret_words) - 1)
secret_letters = list(secret_words[random_choice])
visible_letters = list("_" * len(secret_words[random_choice]))
lives = len(STAGES)

# functions
clear = lambda: os.system("clear")

# start
clear()
print(
    "Welcome, you are locked in my castle. The only chance to escape is to guess my password right."
)
print(INTRO)

while lives >= 1:

    # print(lives)
    print('Password: "' + " ".join(visible_letters) + '"\n')
    letter = input("\nChoose a single letter: ").lower()
    clear()

    # input logic
    # wrong input
    if letter not in "abcdefghijklmnopqrstuvwxyz":
        lives -= 1
        print("The input was not a single letter. You are in danger!")
    # wrong choice
    elif letter not in secret_letters:
        lives -= 1
        print("The guess was wrong. You are in danger!")
    # similar choice
    elif letter in visible_letters:
        lives -= 1
        print("You made that guess already. You are in danger!")

    # game logic
    # correct choice
    if letter in secret_letters and letter not in visible_letters:
        for idx in range(0, len(secret_letters)):
            if secret_letters[idx] == letter:
                visible_letters[idx] = letter
        print("Your guess was correct.")
        # check if won
        if secret_letters == visible_letters:
            print(ESCAPE)
            print('Password: "' + " ".join(visible_letters) + '"\n')
            lives = 0
        elif lives == len(STAGES):
            print(INTRO)
        else:
            print(STAGES[lives])
    else:
        print(STAGES[lives])
