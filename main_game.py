import battle_variables
import battle_sequence
import user_techniques

#All the text here is just filler for the game
print('???: Welcome traveler!\n')

print('???: You may not know it yet but you are in the one and only...\n')

print('???: BATTLE COLOSSEUM!\n')

print('???: You might be asking yourself,\"What is the battle colosseum?\"\nThat is why I, Dr.McQuackletin the Great, am here to show the ropes\n')

print('Dr.McQuackletin?\n')

print('Dr.McQuackletin: YES, DR.QUACKLETIN IS MY NAME\nI\'m not even sure your name is as impressive. What is it, Snoogle Fooggle?\n')

#Makes the user enter a name that is 3 to 13 characters long and capitalizes the name
user_name = input('My name is actually...(Probably 3 to 13 characters long)\n')
while len(user_name) < 3 or len(user_name) > 13:
    if len(user_name) < 3:
        user_name = input('Dr.McQuackletin: I bet your name has more letters than your IQ has numbers\n')
    else:
        user_name = input('Dr.McQuackletin: I need a name, not a sentence\n')        
user_name = user_name.capitalize()

print('Dr.McQuackletin: {}?, I bet that name won\'t help you win\n'.format(user_name))

print('{}: Ugh, so what is the battle colosseum about anyway?\n'.format(user_name))

print('Dr.McQuackletin: Well, It\'s quite simple actually.\nYou fight opponents with the use of modern science, arcane magic and superhuman strength.\nWhen you\'ve defeated all opponents you may leave the colosseum\n' )

print('{}: That\'s cool, apart from the part about science, magic and strength.\nAs you can see, I lack all of those.\n'.format(user_name))

print('Dr.McQuackletin: Don\'t worry about it.\nAs you advance throught the colosseum, you\'ll pick up some traits along the way.\n')

print('{}: That\'s a relief. Time to start beating up baddies.\n'.format(user_name))

print('Dr.McQuackletin: Hold it there.\nFirstly, no one here is bad, everyone just wants to go home.\nSecondly, Don\'t you think you need some practice before you go off?\n')

print('{}: Fine. Where do we start?\n'.format(user_name))

#Runs a tutorial for the user to get the feel of the game
print('Dr.McQuackletin: Let\'s start with that plushie over there.\n')
battle_sequence.tutorial(user_name)
                
print('Dr.McQuackletin: Well lemme take my equipment back and I\'ll be on my way\n')

print('{}: Wait, what am I meant to start with then!?\n'.format(user_name))

print('Dr.MCQuackletin: You can punch, can\'t you?\nHere, take these crystals for your healing problems\n')

print('{}: Really, you\'re a doctor and you\'re giving me healing crystals!?\nAre you sure your name is not McQuackletin for a reason?\n'.format(user_name))

print('Dr.McQuackletin: Ay, watch it kid. Good stuff is expensive around here\nBy the way, I think those crystals are the least of your problems\nHere comes your first opponent\n')
    
print('{}: Yikes!, He\'s coming fast. Lemme see what I\'m working with\n'.format(user_name))

print('Flop\nIt\'s not the best I can do but it does something\nDamage:5% of max HP     Success Rate:100%\n')

print('Healing Crysatls\nVaccinations are better\nHealing:7% of max HP     Success Rate:100%\n')

print('Fleeting Punches\nFighting can be exhausting sometimes\nDamage:15% of HP      Success Rate:100%\n')

#Makes the user battle 10 enemies and if the user loses, the sequence of battles ends
level = 0
while level < 10:
    print('Level {}:\n'.format(level + 1))
    battle_sequence.battle_sequence(user_name,level)
    if battle_variables.win_or_lose == False:
        break
    level += 1
    battle_variables.user_max_health += 100
    user_techniques.move_learning(user_name, level)

#Text is user loses
if battle_variables.win_or_lose == False:
    print('Dr.McQuackletin: Better luck next time kiddo.\n')
else:
    #Runs a Boss Battle for the user
    print('Dr.McQuackletin: Wow you actually did it.\nLet\'s see if you\'re worth my time\n')
    print('Level 11: BOSS BATTLE\n')
    battle_variables.user_max_health = 1000
    battle_sequence.battle_sequence(user_name,10)
    if battle_variables.win_or_lose == False:
        print('Dr.McQuackletin: I told you that you won\'t win with a name like that\nyou lose.')
    else:
        print('Dr.McQuackletin: I don\'t know how you did it kid, you actually beat me.\nWell, seeing as you defeated me, I have no choice but to say...')
        print('\n{} IS HEREBY DECLARED AS THE CHAMPION OF THE BATTLE COLLOSEUM\n'.format(user_name.upper()))
        print('\nDr.McQuackletin: You did it kid, you won\n')
    
