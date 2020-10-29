import random
import user_techniques
import battle_variables
import math
import enemies

def battle_sequence(name,battle):
    global enemy_health
    global user_health
    global win_or_lose
    
    turn = 1
    #resets the variables at the beginning of each battle
    battle_variables.reset_variables()
    enemy_health = enemies.enemy_tech[battle][2]
    user_health = battle_variables.user_max_health
    #prints the enemy stats and user stats
    print('{}\'s HP:{}'.format(enemies.enemy_tech[battle][0],enemy_health))
    print('{}\'s HP:{}'.format(name, user_health))
    print('\n')
    while enemy_health >= 0 and user_health >= 0:
        #print the user's attacks
        if len(user_techniques.user_tech) < 4:
            for num in range(len(user_techniques.user_tech)):
                print('{} - {:<18}'.format(num + 1, user_techniques.user_tech[num][0]),end ='')
        else:
            for num in range(3):
                print('{} - {:<18}'.format(num + 1, user_techniques.user_tech[num][0]), end ='')
            print()
            for num in range(len(user_techniques.user_tech)-3):
                print('{} - {:<18}'.format(num + 4, user_techniques.user_tech[num + 3][0]), end ='')
        print()
        try:
            attack = int(input())
            user_techniques.user_tech[attack - 1][1]()
        
        except:
            user_techniques.user_damage = 0
            user_techniques.user_heal = -0.05 * user_health
            print('{} got confused\n'.format(name))
        
        #performs an enemy attack based on the enemy
        enemies.enemy_technique(battle)
        
        #formula for enemy_health
        enemy_health = math.ceil(enemy_health - user_techniques.user_damage + enemies.enemy_heal)
        
        if enemy_health > enemies.enemy_tech[battle][2]:
            enemy_health = enemies.enemy_tech[battle][2]
        #if enemy health <= 0 then the battle ends whether the user's health is 0 or not
        if enemy_health <= 0:
            break
        
        print('{}\'s HP:{:.0f}'.format(enemies.enemy_tech[battle][0],enemy_health))
        
        #formula for user_health
        user_health = math.ceil(user_health - enemies.enemy_damage + user_techniques.user_heal)
        
        if user_health > battle_variables.user_max_health:
            user_health = battle_variables.user_max_health
        #ends the battle is the user's health is 0 and the enemy's health is not 0
        if user_health <= 0:
            break
        
        print('{}\'s HP:{:.0f}'.format(name, user_health))
        
        print('Turn:{}'.format(turn))
        turn += 1
        print('\n')
    #determines whether the user wins or lose   
    if user_health <= 0:
        print('YOU LOSE :(\n')
        battle_variables.win_or_lose = False
    else:
        print('YOU WIN!\n')
        
# the tutorial is similar to the battle_sequence function
def tutorial(name):
    global tutorial_dummy
    global tutorial_user
    turn = 1
    battle_variables.reset_variables()
    enemy_health = battle_variables.tutorial_dummy
    user_health = battle_variables.tutorial_user
    print('Defenseless Plusie HP:{}'.format(enemy_health))
    print('{}\'s HP:{}'.format(name, user_health))
    print('\n')
    while enemy_health >= 0 and user_health >= 0:
        i = 0
        for num in range(len(user_techniques.tutorial_tech)):
            i += 1
            print('{} - {}'.format(i,user_techniques.tutorial_tech[num][0]), end = '    ')
        print()
        try:
            attack = int(input())
            user_techniques.tutorial_tech[attack - 1][1]()
        
        except:
            user_techniques.user_damage = 0
            user_techniques.user_heal = -0.05 * user_health
            print('{} got confused'.format(name))
        enemy_health = math.ceil(enemy_health - user_techniques.user_damage)

        if enemy_health <= 0:
            break
        
        print('Defenseless Plusie HP:{:.0f}'.format(enemy_health))
        
        user_health = math.ceil(user_health + user_techniques.user_heal)
        
        if user_health > battle_variables.tutorial_user:
            user_health = battle_variables.tutorial_user
        
        if user_health <= 0:
            break
        
        print('{}\'s HP:{:.0f}'.format(name, user_health))
        
        print('Turn:{}'.format(turn))
        turn += 1
        
        print('\n')
    
    if user_health <= 0:
        print('YOU LOSE\n\nDr.McQuackletin: How on earth did you lose to a plusie?\nWell, that\'s not my business\n')
    
    else:
        print('YOU WIN\n\nDr.McQuackletin: Congratulations on beating up a defenseless plushie.\nI guess you are ready to take on anyone with your plushie beating skills\n')