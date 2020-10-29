#variables used in battle sequence
user_max_health = 100
enemy_max_health = 100
enemy_damage = 0
enemy_heal = 0
rolling_a = 0
rolling_b = 1
rolling_rate = 200
refresh_rate = 14
user_damage = 0
user_heal = 0

tutorial_dummy = 100
tutorial_user = 100

win_or_lose = True
#resets the variables when called
def reset_variables():
    global rolling_a
    global rolling_b
    global rolling_rate
    global refresh_rate
    
    enemy_damage = 0
    enemy_heal = 0
    rolling_a = 0
    rolling_b = 1
    rolling_rate = 200
    refresh_rate = 14
    user_damage = 0
    user_heal = 0
