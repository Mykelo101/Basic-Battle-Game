import random
import battle_variables
import battle_sequence

#All the functions here act as the various attacks the user can pick from
# user_damage is the amount that is taken for the enemy's health
# user_heal is the amount that is added to the user's health
def pain_split():
    global user_damage
    global user_heal
    rate = random.randint(1,20)
    if rate > 17:
        user_damage = 0
        user_heal = 0
        print('Technique failed!\n')
    else:
        pain = battle_sequence.enemy_health - battle_sequence.user_health
        user_damage = pain / 2
        user_heal = pain / 2
        print('Pain Split!\n')
pain_split_bio ='Just leveling the playing field\nEffect: Share the player\'s and enemy\'s HP     Success Rate:85%\n'

def rolling_punches():
    global user_damage
    global user_heal
    global rolling_rate
    global rolling_b
    global rolling_a
    rate = random.randint(1, 200)
    if rate > battle_variables.rolling_rate:
        user_damage = 0
        user_heal = 0
        battle_variables.rolling_rate -= 6
        print('Technique failed!\n')
    else:
        user_damage = battle_variables.rolling_b + battle_variables.rolling_a
        battle_variables.rolling_a = battle_variables.rolling_b
        battle_variables.rolling_b = user_damage
        user_heal = 0
        battle_variables.rolling_rate -= 6
        print('Rolling Punch!\n')
    if battle_variables.rolling_rate < 10:
        battle_variables.rolling_rate = 10
rolling_punches_bio = 'Just keep punching, Just keep punching\nDamage:1 but increases per hit     Success Rate:100%, Decreases by 3% per use\n'
        
def life_steal():
    global user_damage
    global user_heal
    rate = random.randint(1,5)
    if rate == 5:
        user_damage = 0
        user_heal = 0
        print('Technique failed!\n')
    else:
        user_damage = 0.15 * battle_sequence.enemy_health
        user_heal = user_damage / 3
        print('Life Steal!\n')
life_steal_bio ='Not all energy has to be wasted\nDamage:15% of enemy HP     Healing:1/3 of Damage     Success Rate:80%\n'

def eye_for_an_eye():
    global user_damage
    global user_heal
    eye_for_eye = battle_sequence.user_health * 0.15
    user_heal = -1 * eye_for_eye
    rate = random.randint(2,4) / 2
    user_damage = eye_for_eye * rate
    print('Eye for an Eye!\n')
eye_for_an_eye_bio ='You gotta lose some to win some\nRecoil:15% of HP     Damage:x1 to x2 of Recoil     Success Rate:100%\n'
    
def kamikaze():
    global user_damage
    global user_heal
    rate = random.randint(1,3)
    if rate > 1:
        user_damage = 0
        user_heal = battle_variables.user_max_health * -2 / 3
        print('Technique failed!\n')
    else:
        user_heal = battle_variables.user_max_health * -2 / 3
        user_damage = user_heal * -2
        print('Kamikaze!\n')
kamikaze_bio ='Would have defeated the purpose of winning but you have some leftover health as a bonus\nRecoil:2/3 of max HP     Damage:x2 Recoil     Success Rate:33%\n'
        
def semi_kaze():
    global user_damage
    global user_heal
    rate = random.randint(1,3)
    if rate == 3:
        user_damage = 0
        user_heal = battle_variables.user_max_health * -1 / 3
        print('Technique failed!\n')
    else:
        user_heal = battle_variables.user_max_health * -1 / 3
        user_damage = user_heal * -1.5
        print('Semi_kaze!\n')
semi_kaze_bio ='Like a kamikaze...but semi\nRecoil:1/3 of max HP     Damage:x1.5 Recoil     Success Rate:66%\n'
        
def placebo_pills():
    global user_damage
    global user_heal
    rate = random.randint(1,20)
    if rate == 20:
        user_damage = 0
        user_heal = 0
        print('Technique failed!\n')
    else:
        user_damage = 0
        user_heal = 0.11 * battle_variables.user_max_health
        print('Placebo Pills\n')
placebo_pills_bio = 'It\'s better then those crystals at least\nHealing:11% of max HP     Success Rate:95%\n'

def gummy_bears():
    global user_damage
    global user_heal
    rate = random.randint(1,20)
    if rate > 17:
        user_damage = 0
        user_heal = 0
        print('Technique failed!\n')
    else:
        user_damage = 0
        user_heal = 0.23 * battle_variables.user_max_health
        print('Gummy Bears\n')
gummy_bears_bio ='Is this better or worse?\nHealing:23% of max HP     Success Rate:85%\n'

def actual_medicine():
    global user_damage
    global user_heal
    rate = random.randint(1,20)
    if rate > 13:
        user_damage = 0
        user_heal = 0
        print('Technique failed!\n')
    else:
        user_damage = 0
        user_heal = 0.49 * battle_variables.user_max_health        
        print('Finally some medicine\n')
actual_medicine_bio = 'I guess there are some real doctors here\nHealing:49% of max HP     Success Rate:65%\n'
        
def dying_punches():
    global user_damage
    global user_heal
    rate = random.randint(1,5)
    if rate == 1:
        user_damage = 0
        user_heal = 0
        print('Technique failed!\n')
    else:
        dying =((battle_variables.user_max_health - battle_sequence.user_health) * 0.11) ** 1.3
        user_damage = dying
        user_heal = 0
        print('Dying Punch!\n')
dying_punches_bio ='What doesn\'t kill you makes you stronger, gets better with higher max HP\nDamage:Increases as health Reduces     Success Rate:80%\n'
        
def gamble_shot():
    global user_damage
    global user_heal
    rate = random.randint(1,5)
    if rate != 1:
        user_damage = 0
        user_heal = -0.1 * battle_variables.enemy_max_health
        print('Technique failed!\n')
    else:
        user_damage = 0.8 * battle_variables.enemy_max_health
        user_heal = -0.1 * battle_variables.enemy_max_health
        print('Gamble Shot!\n')
gamble_shot_bio ='A little risk won\'t hurt...\nDamage:80% of enemy max HP     Recoil:10% of enemy max HP     Success Rate:20%\n'
            
def one_hit_ko():
    global user_damage
    global user_heal
    rate = random.randint(1,20)
    if rate != 1:
        user_damage = 0
        user_heal = 0
        print('Technique failed!\n')
    else:
        user_damage = battle_variables.enemy_max_health
        user_heal = 0
        print('One Hit KO!\n')
one_hit_ko_bio = 'All it takes is one punch, ONE PUNCH!\nDamage:Instant Knock Out     Success Rate:5%\n'
    
def grand_slam():
    global user_damage
    global user_heal
    rate = random.randint(1,5)
    if rate == 5:
        user_damage = 0
        user_heal = 0
        print('Technique failed!\n')
    else:
        user_damage = battle_variables.user_max_health * 0.15
        user_heal = 0
        print('Grand Slam!\n')
grand_slam_bio = 'Like Flop, just that is\'s a slam, that\'s grand\nDamage:15% of max HP     Success Rate:80%\n'
            
def reverso():
    global user_damage
    global user_heal
    rate = random.randint(1,20)
    if rate > 7:
        user_damage = 0
        user_heal = 0
        print('Technique failed!\n')
    else:
        reverso_hp = battle_sequence.enemy_health - battle_sequence.user_health
        user_heal = reverso_hp
        user_damage = reverso_hp
        print('Reverso!\n')
reverso_bio ='The ole\' Switcheroo\nEffect:Switches player\'s HP and enemy\'s HP     Success Rate:35%\n'
        
def flop():
    global user_damage
    global user_heal
    rate = random.randint(1,4)
    if rate != 1:
        user_damage = battle_variables.user_max_health * 0.05
        user_heal = 0
        print('Flop\n')
    else:
        user_damage = battle_variables.user_max_health * 0.075
        user_heal = 0
        print('Flippity Flop\n')
        
def healing_crystals():
    global user_damage
    global user_heal
    rate = random.randint(1,4)
    if rate != 1:
        user_damage = 0
        user_heal = battle_variables.user_max_health * 0.07
        print('Healing Crystals\n')
    else:
        user_damage = 0
        user_heal = battle_variables.user_max_health * 0.1
        print('I do as the crystal guides\n')
        
def fleeting_punches():
    global user_damage
    global user_heal
    user_heal = 0
    user_damage = battle_sequence.user_health * 0.15
    print('Fleet Punch\n')
        
#List of list of the current user techniques       
user_tech = [
               ['Flop', flop],
                ['Healing Crystals',healing_crystals],
                ['Fleeting Punch',fleeting_punches]]

#List of list of unlearned techniques
unlearned = [['Rolling Punches',rolling_punches,rolling_punches_bio],
                ['Placebo Pills',placebo_pills,placebo_pills_bio],
                ['Life Steal',life_steal,life_steal_bio],
                ['Kamikaze',kamikaze,kamikaze_bio],
                ['Semi-kaze',semi_kaze,semi_kaze_bio],
               ['Eye for an Eye',eye_for_an_eye,eye_for_an_eye_bio],
               ['Gummy Bears',gummy_bears,gummy_bears_bio],
                ['Pain Split',pain_split,pain_split_bio],
                ['Dying Punches',dying_punches,dying_punches_bio],
                ['Grand Slam',grand_slam,grand_slam_bio],
               ['Actual Medicine',actual_medicine,actual_medicine_bio],
               ['Gamble Shot',gamble_shot,gamble_shot_bio],
                ['One Hit KO',one_hit_ko,one_hit_ko_bio],
                ['Reverso',reverso,reverso_bio]]
                
#This is the move learning function
def move_learning(name,lev):
    if lev < 4:
        #adds a new attack to the user's attack list after the first three enemies
        print('{} learned a new technique!\n'.format(name))
        print('{}\n{}'.format(unlearned[0][0],unlearned[0][2]))
        user_tech.append(unlearned[0])
        unlearned.pop(0)
    elif lev > 3 and lev < 9:
        #gives the user the choice to learn one of two new attacks
        #the choices are the first two attacks in the unlearned attacks list
        print('{} has two techniques they can choose from!\n'.format(name))
        print('{}-1\n{}'.format(unlearned[0][0],unlearned[0][2]))
        print('{}-2\n{}'.format(unlearned[1][0],unlearned[1][2]))
        learn = input('Type 1 or 2 to choose between the two techniques\nType anything else if you do not want to learn any\n')
        if learn =='1':
            #lists the current user attacks
            print('You can only have 6 techniques at a time\n')
            for num in range(3):
                print('{} - {:<18}'.format(num + 1, user_tech[num][0]), end ='    ')
            print()
            for num in range(len(user_tech)-3):
                print('{} - {:<18}'.format(num + 4, user_tech[num + 3][0]), end ='    ')
            print()
            try:
                #switches the attack with the chosen user attack
                discard = int(input('Which technique do you want to discard?\n'))
                discard -= 1
                user_tech.pop(discard)
                user_tech.insert(discard,unlearned[0])
                unlearned.pop(0)
                unlearned.pop(0)
            except:
                print('No change was made')
                unlearned.pop(0)
                unlearned.pop(0)
        elif learn =='2':
            #lists the current user attacks
            print('You can only have 6 techniques at a time\n')
            for num in range(3):
                print('{} - {:<18}'.format(num + 1, user_tech[num][0]), end ='    ')
            print()
            for num in range(len(user_tech)-3):
                print('{} - {:<18}'.format(num + 4, user_tech[num + 3][0]), end ='    ')
            print()
            try:
                #switches the attack with the chosen user attack
                discard = int(input('Which technique do you want to discard?\n'))
                discard -= 1
                user_tech.pop(discard)
                user_tech.insert(discard,unlearned[1])
                unlearned.pop(0)
                unlearned.pop(0)
            except:
                print('No change was made')
                unlearned.pop(0)
                unlearned.pop(0)
        else:
            print('No change was made')
            unlearned.pop(0)
            unlearned.pop(0)
    elif lev == 9:
        #after the ninth enemy the user has the choice to learn the last attack
        print('{} has a technique they can learn!\n'.format(name))
        print('{}\n{}'.format(unlearned[0][0],unlearned[0][2]))
        learn = input('Type 1 if you want to learn this technique\nType anything else if you do not want to learn any\n')
        if learn =='1':
            #lists the current user attacks
            print('You can only have 6 techniques at a time\n')
            for num in range(3):
                print('{} - {:<18}'.format(num + 1, user_tech[num][0]), end ='    ')
            print()
            for num in range(len(user_tech)-3):
                print('{} - {:<18}'.format(num + 4, user_tech[num + 3][0]), end ='    ')
            print()
            try:
                #switches the attack with the chosen user attack
                discard = int(input('Which technique do you want to discard?\n'))
                discard -= 1
                user_tech.pop(discard)
                user_tech.insert(discard,unlearned[0])
                unlearned.pop(0)
            except:
                print('No change was made')
                unlearned.pop(0)
                
#functions that represent the tutorial attacks
def stab():
    global user_damage
    global user_heal
    user_damage = 10
    user_heal = 0
    
def bandaid():
    global user_damage
    global user_heal
    user_damage = 0
    user_heal = 10
    
def backstab():
    global user_damage
    global user_heal
    user_damage = 30
    user_heal = -40
    
#Lists of list of tutorial techniques
tutorial_tech = [['Stab',stab],
                 ['Band Aid', bandaid],
                 ['Back Stab',backstab]]
tutorial_attacks = [ stab,  bandaid, backstab]
tutorial_attacks_name = ['Stab', 'Band Aid', 'Back Stab']