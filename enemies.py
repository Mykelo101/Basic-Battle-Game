import battle_sequence
import battle_variables
import random
import user_techniques

#all the enemy attack functions and their respective health's
ninja_max_health = 100
def ninjitsu():
    global enemy_damage
    global enemy_heal
    enemy_damage = 0.05 * ninja_max_health
    enemy_heal = 0
    print('Jo used Ninjitsu!\n')
    
def healing_scroll():
    global enemy_damage
    global enemy_heal
    enemy_damage = 0
    enemy_heal = 0.05 * ninja_max_health
    print('Jo used a healing scroll!\n')
    
def shuriken():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,4)
    if rate == 1:
        enemy_damage = 0
        enemy_heal = 0
        print('Jo\'s Shuriken missed!\n')
    else:
        enemy_damage = 0.1 * ninja_max_health
        enemy_heal = 0
        print('Jo used a Shuriken!\n')
        
ninja_attacks = [ninjitsu, shuriken, healing_scroll]

mini_slime_max_health = 300
def regenerate():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,5)
    if rate < 3:
        enemy_damage = 0
        enemy_heal = 0
        print('Mini Slime failed to Regenerate!\n')
    else:
        enemy_damage = 0
        enemy_heal = 0.12 * battle_sequence.enemy_health
        print('Mini Slime used Regenerate!\n')
        
def bounce():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,4)
    if rate == 1:
        enemy_damage = 0
        enemy_heal = -0.05 * battle_sequence.enemy_health
        print('Mini Slime\'s Bounce missed!\n')
    else:
        enemy_damage = 0.1 * battle_sequence.enemy_health
        enemy_heal = 0
        print('Mini Slime used Bounce!\n')

def jelly_shot():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,4)
    if rate == 1:
        enemy_damage = 0
        enemy_heal = -0.05 * battle_sequence.enemy_health
        print('Mini Slime\'s Jelly Shot missed!\n')
    else:
        enemy_damage = 0.15 * battle_sequence.enemy_health
        enemy_heal = -0.05 * battle_sequence.enemy_health
        print('Mini Slime used Jelly Shot!\n')

def healing_jel():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,5)
    if rate == 1:
        enemy_damage = 0
        enemy_heal = 0
        print('Mini Slime\'s healing jel failed!\n')
    else:
        enemy_damage = 0
        enemy_heal = 0.06 * mini_slime_max_health
        print('Mini Slime used some healing jel\n')
        
mini_slime_attacks = [regenerate, bounce, jelly_shot, healing_jel]

dr_acula_max_health = 350
def blood_transfusion():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,4)
    if rate == 1:
        enemy_damage = 0
        enemy_heal = 0
        print('Dr.Acula had an unsuccessful Blood Transfusion!\n')
    else:
        enemy_damage = 0.09 * battle_variables.user_max_health
        enemy_heal = enemy_damage / 3
        print('Dr.Acula used Blood Transfusion!\n')
        
def life_sap():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,3)
    if rate != 1:
        enemy_damage = 0
        enemy_heal = 0
        print('Dr.Acula\'s Life Sap failed!\n')
    else:
        enemy_damage = 0.18 * battle_variables.user_max_health
        enemy_heal = enemy_damage / 3
        print('Dr.Acula used Life Sap!\n')

def lunge():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,4)
    if rate == 1:
        enemy_damage = 0
        enemy_heal = -0.19 * dr_acula_max_health
        print('Dr.Acula lunged at you but missed!\n')
    else:
        enemy_damage = 0.19 * battle_sequence.enemy_health
        enemy_heal = 0
        print('Dr.Acula used Lunge!\n')

def bat_swarm():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,4)
    if rate == 1:
        enemy_damage = 0
        enemy_heal = 0
        print('Dr.Acula failed to summon a Bat Swarm!\n')
    else:
        swarm = random.randint(3,20)
        enemy_damage = swarm * battle_sequence.enemy_health / 100
        enemy_heal = 0
        print('Dr.Acula summoned a Bat Swarm of {} Bats!\n'.format(swarm))
        
def bone_saw():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,4)
    if rate != 1:
        enemy_damage = 0
        enemy_heal = -0.05 * dr_acula_max_health
        print('Dr.Acula lunged at you with a Bone Saw but missed!\n')
    else:
        enemy_damage = 0.25 * dr_acula_max_health
        enemy_heal = 0
        print('Dr.Acula used a Bone Saw!\n')

dr_acula_attacks = [blood_transfusion, life_sap, lunge, bat_swarm, bone_saw]

killa_bee_max_health = 300
def killa_stinger():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,3)
    if rate == 1:
        enemy_damage = 0
        enemy_heal = 0
        print('Killa Bee\'s Killa Stinger missed!\n')
    else:
        enemy_damage = 0.29 * killa_bee_max_health
        enemy_heal = -0.14 * killa_bee_max_health
        print('Killa Bee used Killa Stinger!\n')

def bee_swarm():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,4)
    if rate == 1:
        enemy_damage = 0
        enemy_heal = 0
        print('Killa Bee failed to summon a Bee Swarm!\n')
    else:
        b_swarm = random.randint(5,25)
        enemy_damage = b_swarm * battle_sequence.enemy_health / 100
        enemy_heal = b_swarm * battle_sequence.enemy_health / -400
        print('Killa Bee summoned a Bee Swarm of {} Bees!\n'.format(b_swarm))
        
def honey():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,4)
    if rate == 1:
        enemy_damage = 0
        enemy_heal = 0
        print('Killa Bee\'s honey expired\n')
    else:
        enemy_damage = 0
        enemy_heal = 0.22 * killa_bee_max_health
        print('Killa Bee regained health with some honey\n')
        
def sting_missiles():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,5)
    if rate == 1:
        enemy_damage = 0
        enemy_heal = 0
        print('Killa Bee\'s Sting Missiles missed!\n')
    else:
        missile = random.randint(2,7)
        enemy_damage = missile * battle_sequence.enemy_health / 100
        enemy_heal = missile * battle_sequence.enemy_health / -300
        print('Killa Bee shot {} Sting Missiles!\n'.format(missile))
        
def nectar_drain():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,4)
    if rate == 1:
        enemy_damage = 0
        enemy_heal = 0
        print('Killa Bee\'s Nectar Drain missed!\n')
    else:
        enemy_damage = 0.1 * battle_variables.user_max_health
        enemy_heal = enemy_damage / 2
        print('Killa Bee used Nectar Drain!\n')
killa_bee_attacks = [killa_stinger,bee_swarm,honey,sting_missiles,nectar_drain]

necrolancer_max_health = 500
def death_strike():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,4)
    if rate != 1:
        enemy_damage = 0
        enemy_heal = 0
        print('Necro Lancer failed to use Death Strike!\n')
    else:
        enemy_damage = 0.2 * battle_variables.user_max_health
        enemy_heal = 0
        print('Necro Lancer used Death Strike!\n')
        
def souls_of_the_damned():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,3)
    if rate == 1:
        enemy_damage = 0
        enemy_heal = 0
        print('Necro Lancer failed to summon the Souls of the Damned!\n')
    else:
        souls = random.randint(10,30)
        enemy_damage = souls * necrolancer_max_health / 100
        enemy_heal = 0
        print('Necro Lancer summon {} Souls of the Damned!\n'.format(souls))
        
def unholy_sacrifice():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,4)
    if rate == 1:
        enemy_damage = 0
        enemy_heal = -0.2 * battle_sequence.enemy_health
        print('Necro Lancer\'s Unholy Sacrifice failed!\n')
    else:
        enemy_damage = 0.35 * battle_sequence.enemy_health
        enemy_heal = -0.25 * battle_sequence.enemy_health
        print('Necro Lancer used Unholy Sacrifice!\n')
    
def undying_wish():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,4)
    if rate == 1:
        enemy_damage = 0
        enemy_heal = 0
        print('Necro Lancer\'s Undying Wish wasn\'t granted!\n')
    else:
        enemy_damage = 0
        enemy_heal = 0.3 * necrolancer_max_health
        print('Necro Lancer used Undying Wish!\n')
    
def knight_of_darkness():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,5)
    if rate != 1:
        enemy_damage = 0
        enemy_heal = -0.15 * battle_sequence.enemy_health
        print('Necro Lancer failed to be the Knight of Darkness!\n')
    else:
        enemy_damage = 0.4 * battle_sequence.enemy_health
        enemy_heal = 0.5 * battle_sequence.enemy_health
        print('Necro Lancer used Knight of Darkness!\n')
necrolancer_attacks = [death_strike,souls_of_the_damned,unholy_sacrifice,undying_wish,knight_of_darkness]

mecha_necha_max_health = 500
def reload():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,3)
    if rate != 1:
        enemy_damage = 0
        enemy_heal = 0
        print('Error 205, failed to Reload!\n')
    else:
        enemy_damage = 0
        enemy_heal = user_techniques.user_damage
        print('Mecha Necha 2.0 used Reload!\n')
        
def plasma_cannon():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,3)
    if rate == 1:
        enemy_damage = 0
        enemy_heal = 0
        print('Mecha Necha 2.0\'s Plasma Cannon missed\n')
    else:
        enemy_damage = 0.5 * battle_sequence.enemy_health
        enemy_heal = 0
        print('Mecha Necha 2.0 used Plasma Cannon!\n')
        
def short_circuit():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,4)
    if rate == 1:
        enemy_damage = 0
        enemy_heal = -0.1 * battle_sequence.enemy_health
        print('Mecha Necha 2.0 Short Circuited but missed!\n')
    else:
        enemy_damage = 0.25 * battle_sequence.enemy_health
        enemy_heal = -0.1 * battle_sequence.enemy_health
        print('Mecha Necha 2.0 Short Circuited!\n')
        
def recharge():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,4)
    if rate == 1:
        enemy_damage = 0
        enemy_heal = 0
        print('Mecha Necha 2.0 failed to Recharge!\n')
    else:
        enemy_damage = 0
        enemy_heal = 0.45 * mecha_necha_max_health
        print('Mecha Necha 2.0 Recharged!\n')
        
def assimilation():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,4)
    if rate == 1:
        enemy_damage = 0
        enemy_heal = 0
        print('Error 404, opponent not found!\n')
    else:
        enemy_damage = user_techniques.user_damage
        enemy_heal = user_techniques.user_heal
        print('Mecha Necha 2.0 used Assimilation!\n')
mecha_necha_attacks = [reload, plasma_cannon,short_circuit,recharge,assimilation]

grand_slime_max_health = 1000
def grand_regenerate():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,5)
    if rate < 3:
        enemy_damage = 0
        enemy_heal = 0
        print('Grand Slime failed to Regenerate!\n')
    else:
        enemy_damage = 0
        enemy_heal = 0.2 * battle_sequence.enemy_health
        print('Grand Slime used Regenerate!\n')
        
def grand_bounce():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,4)
    if rate == 1:
        enemy_damage = 0
        enemy_heal = 0
        print('Grand Slime\'s Bounce missed!\n')
    else:
        enemy_damage = 0.15 * battle_sequence.enemy_health
        enemy_heal = 0
        print('Grand Slime used Bounce!\n')

def grand_jelly_shot():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,4)
    if rate == 1:
        enemy_damage = 0
        enemy_heal = -0.075 * battle_sequence.enemy_health
        print('Grand Slime\'s Jelly Shot missed! \n')
    else:
        enemy_damage = 0.2 * battle_sequence.enemy_health
        enemy_heal = -0.075 * battle_sequence.enemy_health
        print('Grand Slime used Jelly Shot!\n')

def grand_healing_jel():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,5)
    if rate == 1:
        enemy_damage = 0
        enemy_heal = 0
        print('Grand Slime\'s healing jel failed!\n')
    else:
        enemy_damage = 0
        enemy_heal = 0.1 * grand_slime_max_health
        print('Grand Slime used some healing jel\n')
        
def slime_minions():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,3)
    if rate == 1:
        enemy_damage = 0
        enemy_heal = 0
        print('Grand Slime failed to summon its Slime Minions!\n')
    else:
        slimes = random.randint(20,40)
        enemy_damage = slimes * battle_sequence.enemy_health / 100
        enemy_heal = slimes * battle_sequence.enemy_health / -500
        print('Grand Slime summoned {} Slime Minions!\n'.format(slimes))
        
grand_slime_attacks = [grand_regenerate,grand_bounce,grand_jelly_shot,grand_healing_jel,slime_minions]

snipe_the_fox_max_health = 800
def no_scope():
    global enemy_damage
    global enemy_heal
    enemy_damage = battle_sequence.enemy_health / 3.6
    enemy_heal = 0
    print('Snipe did a 360 no scope!\n')
        
def ricochet():
    global enemy_damage
    global enemy_heal
    rico = random.randint(2,20)
    enemy_damage = rico * snipe_the_fox_max_health / 100
    enemy_heal = 0
    print('Snipe used Bullet Ricochet!\n')
    
def second_aid_kit():
    global enemy_damage
    global enemy_heal
    enemy_damage = 0
    enemy_heal = 0.5 * battle_sequence.enemy_health
    print('Snipe used a Second Aid Kit\n')
    
def mini_rocket_launcher():
    global enemy_damage
    global enemy_heal
    rocket = random.randint(5,50)
    enemy_damage = rocket  * 3.5
    enemy_heal = 0
    print('Snipe launched {} rockets with a Mini Rocket Launcher!\n'.format(rocket))
    
def sniper():
    global enemy_damage
    global enemy_heal
    if battle_sequence.user_health <= 100:
        enemy_damage = 1000
        enemy_heal = 0
        print('You got Sniped!\n')
    else:
        enemy_damage = 0
        enemy_heal = 0.1 * battle_sequence.enemy_health
        print('Snipe reloaded his guns\n')
        
snipe_the_fox_attacks = [no_scope, ricochet, second_aid_kit, mini_rocket_launcher, sniper]

pyro_the_mage_max_health = 800
def fireball():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,6)
    if rate == 1:
        enemy_damage = 0
        enemy_heal = 0
        print('Pyro\'s Fireball missed!\n')
    else:
        enemy_damage = 0.15 * battle_sequence.enemy_health
        enemy_heal = 0
        print('Pyro used Fireball!\n')
        
def healing_potion():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,4)
    if rate == 1:
        enemy_damage = 0
        enemy_heal = 0
        print('Pyro\'s healing potion was quack!\n')
    else:
        enemy_damage = 0
        enemy_heal = 0.2 * pyro_the_mage_max_health
        print('Pyro used a healing potion\n')
        
def dark_magic():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,5)
    if rate != 1:
        enemy_damage = 0
        enemy_heal = -0.1 * battle_sequence.enemy_health
        print('Pyro\'s Dark Magic backfired!\n')
    else:
        enemy_heal = -0.1 * battle_sequence.enemy_health
        enemy_damage = 0.4 * battle_sequence.enemy_health
        print('Pyro used Dark Magic!\n')
        
def flame_of_the_dragon():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,3)
    if rate == 1:
        enemy_damage = 0
        enemy_heal = -0.2 * battle_sequence.enemy_health
        print('Pyro got burnt by the Flame of the Dragon!\n')
    else:
        enemy_damage = 0.5 * battle_sequence.enemy_health
        enemy_heal = -0.2 * battle_sequence.enemy_health
        print('Pyro used Flame of the Dragon!\n')
        
def max_inferno():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,4)
    if rate != 1:
        enemy_damage = 0
        enemy_heal = 0
        print('Pyro failed to summon Max Inferno!\n')
    else:
        enemy_damage = 0.35 * battle_sequence.enemy_health
        enemy_heal = 0
        print('Pyro used Max Inferno!\n')

pyro_the_mage_attacks =[fireball,healing_potion,dark_magic,flame_of_the_dragon,max_inferno]

chuck_morris_max_health = 1000
def round_house_kick():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,3)
    if rate == 1:
        enemy_damage = 0
        enemy_heal = 0
        print('You somehow dodged Chuck\'s Round House Kick!\n')
    else:
        yest = random.randint(1,3)
        if yest == 1:
            enemy_damage = battle_sequence.user_techniques.user_heal
            enemy_heal = battle_sequence.user_techniques.user_damage
            print('Chuck Morris Round House Kicked you to yesterday!\n')
        else:
            enemy_damage = 0.35 * battle_sequence.enemy_health
            enemy_heal = 0
            print('Chuck Morris Round House Kicked you!\n')
            
def refuse():
    global enemy_damage
    global enemy_heal
    enemy_damage = 0
    enemy_heal = battle_sequence.user_techniques.user_damage
    print('Chuck Morris Refused to take damage!\n')
    
def third_fist():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,3)
    if rate == 1:
        enemy_damage = 0
        enemy_heal = 0
        print('You somehow dodge Chuck\'s Third Fist!\n')
    else:
        enemy_damage = 0.27 * battle_sequence.enemy_health
        enemy_heal = 0
        print('Chuck Morris punched you with his Third Fist!\n')
        
def cheat_death():
    global enemy_damage
    global enemy_heal
    if battle_sequence.enemy_health < 150:
        enemy_damage = 0
        enemy_heal = 400
        print('Death got scared on Chuck Morris!\n')
    else:
        enemy_damage = 0
        enemy_heal = 0.5 * battle_sequence.enemy_health
        print('Chuck Morris healed himself with his tears!\n')
        
def push_ups():
    global enemy_damage
    global enemy_heal
    enemy_damage = 0.4 * battle_sequence.enemy_health
    enemy_heal = -0.1 * battle_sequence.enemy_health
    print('Chuck Morris did push ups and caused an Earthquake!\n')
    
chuck_morris_attacks = [round_house_kick, refuse, third_fist, cheat_death, push_ups]

dr_mcquackletin_max_health = 1500
def sands_of_time():
    global enemy_damage
    global enemy_heal
    if battle_sequence.enemy_health < 250:
        enemy_damage = -1000000
        enemy_heal = 100000
        print('Dr.McQuackletin used Sands of Time!\n')
    else:
        enemy_damage = 0
        enemy_heal = 400
        print('Dr.McQuackletin used his Healing Factor!\n')
        
def clones():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,3)
    if rate != 1:
        enemy_damage = 0
        enemy_heal = 0
        print('Dr.McQuackletin clones went on a strike!\n')
    else:
        clones = random.randint(3,10)
        enemy_damage = clones * 0.04 * battle_sequence.enemy_health
        enemy_heal = - enemy_damage / (clones * 1.5)
        print('Dr.McQuackletin summoned {} of his clones!\n'.format(clones))
        
def lightning():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,8)
    if rate < 3:
        enemy_damage = 300
        enemy_heal = 0
        print('Dr.McQuackletin struck you with Lightning!\n')
    elif rate == 3:
        enemy_damage = 0
        enemy_heal = -300
        print('Dr.McQuackletin got struck with his own Lightning!\n')
    else:
        enemy_damage = 0
        enemy_heal = 0
        print('Dr.McQuackletin\'s Lightning missed!\n')
            
def magic_ball():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,8)
    if rate == 1:
        enemy_damage = 0
        enemy_heal = -10000
        print('Dr.McQuackletin used a Magic 8 Ball! - Your HP was restored\n')
    elif rate ==2:
        enemy_damage = 0.5 * battle_sequence.user_health
        enemy_heal = 0
        print('Dr.McQuackletin used a Magic 8 Ball! - Your HP was halved\n')
    elif rate == 3:
        enemy_damage = 0
        enemy_heal = -0.5 * battle_sequence.enemy_health
        print('Dr.McQuackletin used a Magic 8 Ball! - His HP was halved\n')
    elif rate == 4:
        enemy_damage = 0
        enemy_heal = 375
        print('Dr.McQuackletin used a Magic 8 Ball! - Quarter of his HP was restored\n')
    elif rate == 5:
        rev = battle_sequence.enemy_health - battle_sequence.user_health
        enemy_damage = rev
        enemy_heal = rev
        print('Dr.McQuackletin used a Magic 8 Ball! - Your HP was swapped\n')
    elif rate ==6:
        swp = battle_sequence.enemy_health - battle_sequence.user_health
        enemy_damage = swp / 2
        enemy_heal = swp / 2
        print('Dr.McQuackletin used a Magic 8 Ball! - Your HP was shared\n')
    else:
        enemy_damage = 0
        enemy_heal = 0
        print('Dr.McQuackletin used a Magic 8 Ball! - Nothing happened\n')
        
def uppercut():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,4)
    if rate == 1:
        enemy_damage = 0
        enemy_heal = 0
        print('You dodged Dr.McQuackletin\'s Uppercut!\n')
    else:
        enemy_damage = 0.12 * battle_sequence.enemy_health
        enemy_heal = 0
        print('Dr.McQuackletin uppercut you!\n')
        
def laser_beam():
    global enemy_damage
    global enemy_heal
    rate = random.randint(1,10)
    if rate > 6:
        enemy_damage = 0
        enemy_heal = 0
        print('You dodged Dr.McQuackletin\'s Laser Beams!\n')
    else:
        enemy_damage = 0.5 * battle_sequence.enemy_health
        enemy_heal = 0
        print('Dr.McQuackletin fired a Laser Beam!\n')
            
#AI for the boss battle            
def boss_battle():
    if battle_sequence.enemy_health > 1000:
        rate = random.randint(1,10)
        if rate > 7:
            lightning()
        elif rate > 5:
            uppercut()
        elif rate > 3:
            clones()
        elif rate > 1:
            laser_beam()
        else:
            magic_ball()
    elif battle_sequence.enemy_health > 500:
        rate = random.randint(1,10)
        if rate > 8:
            lightning()
        elif rate > 7:
            uppercut()
        elif rate > 6:
            clones()
        elif rate > 4:
            laser_beam()
        elif rate > 2:
            sands_of_time()
        else:
            magic_ball()
    else:
        rate = random.randint(1,10)
        if rate == 10:
            lightning()
        elif rate == 9:
            uppercut()
        elif rate == 8:
            clones()
        elif rate == 7:
            laser_beam()
        elif rate > 3:
            sands_of_time()
        else:
            magic_ball()

dr_mcquackletin_attacks = [boss_battle]

#list of lists of enemy stats
enemy_tech = [['Jo the Ninja',ninja_attacks,ninja_max_health],
               ['Mini Slime',mini_slime_attacks,mini_slime_max_health],
               ['Dr.Acula',dr_acula_attacks,dr_acula_max_health],
               ['Killa Bee',killa_bee_attacks,killa_bee_max_health],
               ['Necro Lancer',necrolancer_attacks,necrolancer_max_health],
               ['Mecha Necha 2.0',mecha_necha_attacks,mecha_necha_max_health],
               ['Grand Slime',grand_slime_attacks,grand_slime_max_health],
               ['Snipe the Fox',snipe_the_fox_attacks,snipe_the_fox_max_health],
               ['Pyro the Mage',pyro_the_mage_attacks,pyro_the_mage_max_health],
               ['Chuck Morris',chuck_morris_attacks,chuck_morris_max_health],
               ['Dr.McQuackletin',dr_mcquackletin_attacks,dr_mcquackletin_max_health]]
#function that performs an enemy attack based on the enemy
def enemy_technique(fight):
    attack_group = enemy_tech[fight][1]
    rate = random.randint(0, len(attack_group)-1)
    attack_techinque = attack_group[rate]()
    