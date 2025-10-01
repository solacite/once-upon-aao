# define chars
define p = Character("Prince Faye", color="#3366cc")
define y = Character("You", color="#cc3333")
define n = Character(None)

# general transforms
image faye small:
    "faye.png"
    zoom 0.75
    yalign 0.21

image bg small:
    "smol light bg.png"
    zoom 1.4
    yalign 0.55

# anims
transform shock_bounce:
    yoffset 0
    linear 0.06 yoffset -12
    linear 0.06 yoffset 0
    linear 0.06 yoffset -8
    linear 0.06 yoffset 0

# transforms for expressions
image faye shocked small:
    "faye shocked.png"
    zoom 0.75
    yalign 0.21

image faye sideeye small:
    "faye sideeye.png"
    zoom 0.75
    yalign 0.21

image faye confused small:
    "faye confused.png"
    zoom 0.75
    yalign 0.21

# vars
default admissions_score = 0
default bribed = False
default lied = False
default dropped_out = True

label start:

    scene bg small
    show faye small

    n "Once upon an admissions counselor, you had to hook up with princes to get into prestigious educational institutions."
    p "Oh! Welcome! I'm Prince Faye. I like numbers, but only when they dance. Also snacks."

    # backstory

    n "You dropped out of formal schooling years ago. You preferred studying people to studying books."
    n "Learning their habits by carefully examining peoples' pockets."
    n "Well...pickpocketing."
    n "Your transcript is suspicious. You're going to have to lie, improvise, and maybe bribe the princes with honeycakes."

    if dropped_out:
        n "You know the truth won't impress Faye. That means your mouth will need to be cleverer than your hands were."

    n "Your task is simple: convince Prince Faye that you are his perfect match for the prestigious academy. Academically, socially, and culinarily."

    # Round 1: Resume
    p "First: your resume! Tell me something impressive."

    menu:
            "I aced the kingdom-wide SAT and scored in the top percentile":
                $ admissions_score += 3
                p "Wow! Numbers that sparkle!"
            "I did extensive independent study and worked on a passion project":
                $ admissions_score += 3
                if dropped_out:
                    $ admissions_score -= 1
                p "Projects are living things. I like living things."
            "I faked a few grades and no one noticed":
                $ admissions_score += 3
                $ lied = True
                p "Hm? Resourceful."
    show faye small at shock_bounce
    n "Prince Faye laughs and jots something on a napkin. He seems amused rather than intimidated."

    # pitch personality
    p "Now personality. Tell me why you'd be my favorite scholar."

    menu:
            "I organized a community book drive":
                $ admissions_score += 3
                if dropped_out:
                    $ admissions_score -= 1
                p "Books are fun. Reading's fun."
                p "That's fun!"
            "I always show up early, do my work, and keep to my word":
                $ admissions_score += 1
                if dropped_out:
                    $ admissions_score -= 1
                p "Dependable! Boring in a good way."
            "I snuck into a bank and made a statue of the M*na Lisa in someone's vault out of money":
                $ admissions_score += 2
                $ lied = True
                p "Well,I admire dramatic risk."

    show faye small at shock_bounce
    n "Faye laughs so hard he almost drops his napkin."

    # bribery thru food
    p "Finally, refreshments. I have a very weak spot for snacks. Convince me with cuisine."

    menu:
            "Bake him legendary honeycakes you learned from your grandmother":
                $ admissions_score += 3
                $ bribed = True
                p "Honeycakes? You're speaking my language."
            "Offer to share your packed lunch (plain bread and cheese) but with charming commentary":
                $ admissions_score += 1
                if dropped_out:
                    $ admissions_score -= 1
                p "Hm! How cultured."
            "Slip him a shiny coin and whisper 'letter of recommendation' (clearly bribery)":
                $ admissions_score += 2
                $ bribed = True
                $ lied = True
                p "Oh ho, a classic. I accept coins, but I also accept hugs."
    n "Faye's reaction is unpredictably positive."

    # finale
    if bribed:
        p "I have to ask, though - will you be bringing snacks to our study group sometimes?"
        menu:
            "Of course, it's a lifelong culinary commitment.":
                $ admissions_score += 1
                p "Excellent. That's the kind of dedication I value."
            "I'll bake when motivated; don't count on infinite honeycakes.":
                $ admissions_score += 0
                p "Realistic. I respect your scheduling honesty."
            "I only baked that once and it was a terrible mess.":
                $ admissions_score -= 1
                $ lied = True
                p "Ah..."

    # outcome
    if dropped_out and not lied:
        $ admissions_score -= 2
        show faye sideeye small
        n "There are gaps in your paperwork. Prince Faye notices this with a frown."
    if lied and admissions_score < 5:
        jump ending_scandal_faye
    elif admissions_score >= 7:
        jump ending_faye_accepted
    elif admissions_score >= 4:
        jump ending_faye_waitlisted
    else:
        jump ending_faye_rejected

label ending_faye_accepted:

    scene bg small
    show faye small

    p "By the power vested in me, I hereby offer you a place."
    y "Do I have to bring snacks every week?"
    show faye small
    p "Only when you want to win us over."

    n "You walk away with a ridiculous acceptance."

    return

label ending_faye_waitlisted:

    scene bg small
    show faye sideeye small

    p "Hmm. I'm intrigued, but I also need more honeycakes. Consider this: a place on the waiting napkin."
    y "A waiting napkin?"
    n "Faye places your name gently under a fork and promises to think about it."

    return

label ending_faye_rejected:

    scene bg small

    p "Alas, your pitch did not align with my snack schedule. Try again after you have a better anecdote or a stronger crumble."
    y "Stronger crumble. Got it."

    n "You'll live. You will return."

    return

label ending_scandal_faye:

    scene bg small
    show faye shocked small at shock_bounce

    p "...There's a problem. Did you bribe me with a coin?"
    y "I swear I didn't mean anything by it..."

    return





