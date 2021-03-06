# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define me     = Character("Me")

# Main Characters
define sa     = Character("Samsara")
define av     = Character("Avi")
define jo     = Character("Joseph")
define gw     = Character("GW Person")

# Background Characters
define part_0 = Character("Participant 0")
define part_1 = Character("Participant 1")
define part_2 = Character("Participant 2")

# Game variables
default done_flashback = False
default weeb_mode      = False
default score          = 0

# The game starts here. Joseph says he's looking for the best volunteer at GWU
label start:
    scene bg hackital
    
    show joseph happy
    
    jo "Hello there! My name is Joseph Schiarizzi, and I am looking for the best volunteer at Hackital."
#    jo "I am one of the organisers and would love for someone to just appear in front of me..."
    jo "I am looking for Top Tier Volunteers"
    
    jo "Before we begin... are you a weeb?"
    
    menu:
        "Hai hai!":
            $ weeb_mode = True
        "What's a weeb?":
            $ weeb_mode = False

    jump pre_0

# Signing up for Hackital as a participant
label pre_0:

    scene bg dorm
    
    "Last month..."
    
    me "Oh boy, I am so excited to sign up to participate in Hackital!"

    jump pre_1
    
# You getting a red shirt instead of a black shirt / flashback
label pre_1:

    scene bg registration
    
    "The morning of Hackital, I commuted from my dorm bulding on campus so that I could be the first to show up."
    "I'm so glad that they gave me travel reimbursement for that 2-block trip!"
    
    show samsara happy
    with fade
    
    sa "What size shirt?"
    
    menu:
        "Small":
            pass
        "Medium":
            pass
        "Large":
            pass
        "Extra-Large":
            pass
        "Any size is fine...":
            pass
            
    sa "Okay awesome, here you go! Don't forget to make a hack for Hack Harassment!"
    
    jump realisation

label realisation:
    
    "I look down at the shirt... It's red, unlike the pile of black shirts on the table."
    "Not sure what that means..."

    if done_flashback:
        $ done_flashback = False
        jump pre_5

    jump pre_2

# Joseph pitching Hackital to OS
label pre_2:

    "At my operating systems class two weeks ago..."
    
    scene bg os
    show joseph happy
    with fade
    
#    jo "Hey everyone, in case you didn't know, Hackital is in two weeks. So register at hackital.io."
    jo "We are NERDS, want to meet more people like us !!!"
    jo "Come to Hackital, SIGN UP !" 
    
    me "Hackital what is that?"
    jo "Hacking the Capital"
    jo "Hackital !!!"
    me "That sounds awesome"

    "For some reason this pitch sounded familiar."

    jump pre_3

# Joseph pitching Hackital to GWTC
label pre_3:

    "At Tech Collective four weeks ago..."
    
    scene bg tech
    show joseph helmet
    with fade
    
    jo "We are NERDS, want to meet more people like us !!!"
    jo "Come to Hackital, SIGN UP !" 
    
    "Joseph was very passionate about getting people to sign up for Hackital. He's pitched it to me at least 10 times now!"
    "Of course, that might have to do with him organising this event."

    jump pre_4

# Joseph realises he needs more volunteers
label pre_4:

    "Six months ago..."
    
    scene bg os
    show joseph happy
    with fade
    jo "... And that is why you should host Hackital again this year."
    jo "(Starring into the void)"
    
    show joseph happy
    jo "I just realized that I am short staffed"
    
    hide joseph
    show samsara neutral
    sa "I can ask some people to come and help" 

    $ done_flashback = True
    jump realisation
    
# Joseph telling you that you are a volunteer
label pre_5:

    scene bg registration
    
    "Joseph approaches the table."
    
    show joseph happy
    with fade
    
    jo "Hey there, how's my newest volunteer?"
    
    if weeb_mode:
        me "Nani????"
        jo "Omae wa mo shinderu..."
    
    me "I didn't ask for this..."
    
    jo "What do you mean? You wanted to volunteer."
    
    me "Oh, you're right..."
    
    "Was he though? I don't remember even realising that hackathons needed volunteers."

    jump sam_0

# Samsara asking if you'll be making a #HackHarassment hack
label sam_0:

    scene bg registration

    sa "Sorry to interrupt, but just checking, even if you are volunteering you should be aware that you can still submit a hack to the HackHarassment challenge."

    if done_flashback:
        $ done_flashback = False
        jump job
        
    "Now that I think about it, I've heard a lot about HackHarassment."

    jump sam_1

# Making posters at 3am (with foreshadowing)
label sam_1:

    "The previous night..."
    
    scene bg dorm
    show samsara neutral
    with fade

    sa "(Exhausted)"    

    sa "Thank you so much for helping with these posters."
    
    me "Yeah, no problem. I wasn't doing anything anyways."
    
    sa "If you're having fun now, wait until tomorrow! You're gonna really enjoy it."
    
    me "Yeah I hope so."
    
    if weeb_mode: 
        me "I'm putting off 9001 essays for this." 
        sa "You should write an essay about your #HackHarassment submission."
    
    sa "Anyways, I got to go get 2 hours of sleep. See you at 7am tomorrow!"
    
    me "See you tomorrow!"
    
    "Wait... Isn't Hackital supposed to start at 10am? Must have made a last minute schedule change..."
    
    scene bg registration
    with fade
    
    "Back to Hackital..."
    $ done_flashback = True

    jump sam_0

# Joseph gives you a choice what you want to do
label job:

    show joseph happy
    
    jo "(Feeling the hype)"
    jo "We have 3 main station that we need people at"
    jo "Registration , MLH Hardware Checkout and Event Coordinator"
    jo "I need help in one of them"

    jo "Hey you still there? I was explaining the different volunteer positions you can do."
    
    "Eh, not like I need to know them anyways. I'm not volunteering."
    
    jo "So which one do you want to do?"
    
    "Oh, guess I am..."

    menu:
        "I want to do registration.":
            jump reg_0
        "I want to do hardware checkout.":
            jump har_0
        "I want to help run events.":
            jump eve_0

label reg_0:
    scene bg registration
    with fade
    
    "Welp, guess I should make the most of it and work the registration table."
    
    show samsara happy
    
    sa "Thanks for helping us with registration"
    sa "Take a computer and help people check-in"
    me "Do they need to sign the form"
    sa "Absolutely, even if they are over 18"
    sa "If you have any questions ask Nam, Adrian or Sebastian"

    "(You see a participant approach Samsara)"

    sa "Her group needs a proficient programmer, who should I ask?"
    
    me "Thinking"

    menu:
        "Brandon":
            jump reg_1
        "Sebastian":
            jump reg_1
        "Nam, because he's top-tier":
            jump reg_1
        "Me, because I’m the best":
            $ score -= 1
            jump reg_1
        "Everyone, we need to work together":
            $ score += 1
            jump reg_1    

# Registration event 1
label reg_1:
    scene bg registration
    with fade

    "You figure out that the Registration Desk became the Front Desk"
    
    show avi happy
    
    sa "Nam and Sebastian are helping out people"
    sa "Can you point them to the room where the Git Workshop is located"
    
    "You approach the person"

    me "Hey, the Git Workshop that Samsara and Nam are leading is in"

    menu:
        "Room 302, it’s to the left of the MLH Desk":
            $ score += 1
            jump reg_2
        "Room 433, look at the map next to the Stairwell":
            jump reg_2
        "Leave the building, look for the Building called District House":
            me "Go to the 10th Floor and look for a person called Tad Miller"
            $ score -= 3
            jump reg_2

# Registration event 2
label reg_2:
    scene bg registration
    with fade

    "You accross a group that needs your help"

    me "You need help?"

    "They answer yes"
    "You debate if you should answer"

    menu:
        "No, I don’t like you":
            $score -= 1
        "(Drops Everything) Definetly, I can help you":
            $score += 1
        "Not right now, but ask Brandon or Nam"
          
    if score == 3:
        jump reg_pass
    else:
        jump reg_fail

# Registration pass event
label reg_pass:
    scene bg registration
    with fade

    show samsara happy
    sa "You are awesome"
    sa "Thanks for all your help"
    sa "You have helped Hack Harrasment"

    "Talking the human controlling this game"

    sa "Every Hackital team can take part in the challenge:"
    sa "creating a tech tool to help make the Internet a more inclusive place."
    sa "The top 3 teams with the coolest products will win prizes."
    sa "Competing teams will have access to online harassment and"
    sa "cyberbullying statistics and articles and informational workshops."
    sa "Sponsored by Hack Harassment, Intel, the Born This Way Foundation,"
    sa "and the Silicon Valley Community Foundation."
    # This ends the game.
    return

# Registration fail event
label reg_fail:
    scene bg registration
    with fade

    show samsara sad
    sa "Thanks for trying your best"
    sa "But a lot of people told me that you’ve disrespectfull and inconsiderate"
    sa "I though you could represent Hack Harrasment"
    sa "I will ask you to turn in your red shirt"

    "Talking the human controlling this game"

    sa "I am crying inside a bit, you might to talk to me outside of this game"
    sa "Every Hackital team can take part in the challenge:"
    sa "creating a tech tool to help make the Internet a more inclusive place."
    sa "The top 3 teams with the coolest products will win prizes."
    sa "Competing teams will have access to online harassment and"
    sa "cyberbullying statistics and articles and informational workshops."
    sa "Sponsored by Hack Harassment, Intel, the Born This Way Foundation,"
    sa "and the Silicon Valley Community Foundation."
    
    "Maybe you should try again..."
    
    menu:
        "Okay":
            pass
        "I'll do better":
            pass

   # This ends the game.
    jump reg_0

label har_0:

    scene bg hardware
    with fade
    
    "Welp, guess I should make the most of it and help manage the hardware."
    
    show avi happy
    
    "Someone approaches my desk"

    av "This participant needs a Microcontroller for my project."
    av "I think the name rhymes with amino"

    me "What does he needs"

    menu:
        "Arduino":
            $ score = score + 1
            jump har_1
        "Dell(R) XPS13":
            jump har_1
        "Rasperry PI":
            jump har_1
        "Alienware Laptop":
            jump har_1

# Hardware event 1
label har_1:

    scene bg hardware
    with fade
    
#Flashback

    show avi neutral    

    av "Someone needs Soylent"
    me "(Remembers) Avi told me that we have more people than expected"
    me "We don't have enought Soylent for everyone, but they have been working so hard"
    me "What should I answer ???"
    menu:
        "No, I am sorry":
            $score = score + 1
            jump har_2

        "Yes, Take one":
            jump har_2

# Hardware event 2
label har_2:

    scene bg hardware
    with fade

    show joseph happy

    jo "She needs a Qualcomm(R) Dragon Board"
    jo "You need to make sure that the board is returned after use"
    me "Yes, Sir !!!"

    "What should I do to ensure the board is returned ?"

    menu:
        "Ask for ID":
            pass
        "Ask for $5":
            pass
        "Trust":
            $score = score + 1

    if score == 3:
        jump har_pass
    else:
        jump har_fail

# Hardware pass event
label har_pass:

    scene bg hardware
    with fade

    show avi happy

    av "Excellent job !!"
    av "You look so tired"
    av "Go home, you have earned it"


    # This ends the game.
    return

# Hardware fail event
label har_fail:

    scene bg hardware
    with fade

    "After a long weekend volunteering @ Hackital"
    "I take one last look at the Hardware room..."
    "Everything is missing, everyone has gone home"
    "You look back at Avi"

    show avi sad

    av "You messed up, we need to find all the hardware if not MLH is not endorsing us again"
    av "Hackital will not happen next year"

    jump har_0
    # This ends the game.
    #return
    
# Events event 0
label eve_0:
    
    scene bg hackital
    with fade

    "Welp, guess I should make the most of it and help run events."
    
    show joseph happy
    
    jo "Well hello again. Guess you're helping me with running events."
    
    menu:
        "Yep!":
            pass
        "Yeah...":
            pass
            
            
    jo "Well first, we have a cup stacking tournament. So just wondering, do you know the best cup stack configuration?"
    
    menu:
        "One thin line...":
            jo "Uh... no."
        "Just stack the cups into each other!":
            jo "I mean I guess it won't fall, but your stack will be too short..."
        "Some kind of pyramid thingy.":
            jo "Exactly! Who knew that having a wide base would make your stack stable? Physics."
            $ score += 1
            
    "You and Joe watch the cup stacking event go down (in some cases literally). Everyone is super hype."

    jump eve_1

# Events event 1
label eve_1:
    scene bg hackital
    
    jo "Okay, the cup stacking event was pretty good, but some people want to play video games. What game should they play?"
    
    menu:
        "Super Smash Bros Melee":
            jo "Great choice; Avi was going to lead that already. So it was a trick question. Good thing I didn't fool you!"
            $ score += 1
        "Wii Sports Resort":
            jo "We don't even own a Wii... At least you chose a multiplayer game."
        "The Elder Scrolls: Skyrim":
            jo "Great game, but it's single-player and we wouldn't even get past the first objective due to side-quests."
            
    jo "Well, I'm going home to sleep... Have fun figuring out where the nap room is!"
    
    "I look at my watch. It's 2am. Who even would play video games at this hour? I thought people studied instead."

    jump eve_2

# Events event 2
label eve_2:
    scene bg hackital
    
    jo "Hey, I know that you are working on event running, but a team is having an issue with merge conflicts on their visual novel."
    jo "Can you help them?"
    
    menu:
        "I don't know Git but I can try...":
            jo "Oh haha they are using SVN, so Git doesn't help anyways."
            "You try your best to help the group, but they are unable to use much of your assistance."
        "I don't know how to do that, but I can find someone that does.":
            jo "That's a great answer, I'm sure you can find ONE person that knows how to do software at a hackathon."
            $ score += 1
            "You walk away to go ask around for help."

    if score == 3:
        jump eve_pass
    else:
        jump eve_fail

# Events pass event
label eve_pass:
    
    scene bg hackital
    
    show joseph happy
    
    jo "Hey there, how's my favourite volunteer?"
    
    menu:
        "Fine":
            pass
        "Great":
            pass
            
    jo "I have been hearing only great things about your event running this Hackital."
    
    jo "So listen, I am graduating this year. I need someone to take my place."
    
    jo "Would you like to be the next head organiser of Hackital?"
    
    menu:
        "Yeah I would love to!":
            jo "Awesome, I'm sure you'll do amazingly."
        "No, I have to focus on school...":
            jo "That's a shame, you would have made Hackital legend - wait for it - dary."
        "I don't go to GW, is that okay?":
            jo "Wait what? Oh haha I mean I guess that might be fine..."
            
    "You smile as you Joseph shakes your hand for a job well done."

    # This ends the game.
    return

# Events fail event
label eve_fail:

    
    show joseph happy
    
    jo "Hey listen, we appreciate you trying to help but maybe this just wasn't for you."
    
    me "What do you mean?"
    
    scene bg hackital
    jo "You kind of ran mediocre or horrible events. Most of the participants are looking for something higher tier."
    
    jo "I am graduating next year, and I hope I can find someone to run Hackital... Definitely not you though."
    
    jo "Maybe I'll just let it go."
    
    "You hang your head in disappointment. But then again, you didn't really want to volunteer in the first place."

    # This ends the game.
    return
