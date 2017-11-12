﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define me     = Character("Me")

# Main Characters
define sa     = Character("Samsara")
define se     = Character("Avi")
define jo     = Character("Joseph")

# Background Characters
define part_0 = Character("Participant 0")
define part_1 = Character("Participant 1")
define part_2 = Character("Participant 2")


# The game starts here. Joseph says he's looking for the best volunteer at GWU
label start:

    jump pre_0

# Signing up for Hackital as a participant
label pre_0:

    jump pre_1

default done_flashback = False
    
# You getting a red shirt instead of a black shirt / flashback
label pre_1:

    if done_flashback:
        $ done_flashback = False
        jump pre_5

    jump pre_2

# Joseph pitching Hackital to OS
label pre_2:

    jump pre_3

# Joseph pitching Hackital to GWTC
label pre_3:

    jump pre_4

# Joseph books the Hackital venue and realises he needs more volunteers
label pre_4:

    $ done_flashback = True
    jump pre_1
    
# Joseph telling you that you are a volunteer
label pre_5:

    jump sam_0

# Samsara asking if you'll be making a #HackHarassment hack
label sam_0:

    if done_flashback:
        $ done_flashback = False
        jump job

    jump sam_1

# Making posters at 3am (with foreshadowing)
label sam_1:

    jump sam_2

# Samsara explaining what #HackHarassment is
label sam_2:

    $ done_flashback = True
    jump sam_0

# Joseph gives you a choice what you want to do
label job:

    # This ends the game.
    return

# Registration event 0
label reg_0:

    # This ends the game.
    return

# Registration event 1
label reg_1:

    # This ends the game.
    return

# Registration event 2
label reg_2:

    # This ends the game.
    return

# Registration pass event
label reg_pass:

    # This ends the game.
    return

# Registration fail event
label reg_fail:

    # This ends the game.
    return

# Hardware event 0
label har_0:

    # This ends the game.
    return

# Hardware event 1
label har_1:

    # This ends the game.
    return

# Hardware event 2
label har_2:

    # This ends the game.
    return

# Hardware pass event
label har_pass:

    # This ends the game.
    return

# Hardware fail event
label har_fail:

    # This ends the game.
    return

# Events event 0
label eve_0:

    # This ends the game.
    return

# Events event 1
label eve_1:

    # This ends the game.
    return

# Events event 2
label eve_2:

    # This ends the game.
    return

# Events pass event
label eve_pass:

    # This ends the game.
    return

# Events fail event
label eve_fail:

    # This ends the game.
    return
