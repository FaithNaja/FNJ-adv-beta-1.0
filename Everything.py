#first game 1.0
import random
import time
import math

class Player:
    def __init__(self, name, maxhp, hp, lv, maxxp, xp):
        self.name = name
        self.maxhp = maxhp
        self.hp = hp
        self.lv = lv
        self.maxxp = maxxp
        self.xp = xp

    def stat(self):
        time.sleep(1)
        print('*'*10)
        print('{}' .format(self.name))
        print('HP = {}/{}' .format(self.hp,self.maxhp))
        print('LV = {} ({}/{} xp)' .format(self.lv, self.maxxp, self.xp))
        print('Your code is {}' .format(str(self.name)+str(self.maxhp)+str(self.hp)+str(self.lv)))
        print('*'*10)

    def heal(self, food):
        if food == 'apple':
            self.hp += 10
            print('You got +10 hp!')
        if food == 'poison_bottle':
            self.hp -= 10
            print('for what?')
        if food == 'exp_bottle':
            self.lv += 10
            print('You got +10 xp!')
        if food == 'lolxp':
            self.lv += 999
            print('LOL WTF +999 xp!')
        checkhp()
        checkxp()
     
   
class Pet(Player):
    def __init__(self, name, hp, lv):
        super().__init__(name, weight, height)
    def Basic_Attack_Pet(self, player):
        if random.randint(0,100) <= 10:
            Player.hp -= random.randint(5,10)*2
        else:
            Player.hp -= random.randint(5,10)
        
class Entity:
    def __init__(self, name, hp, lv):
        self.name = name
        self.hp = hp
        self.lv = lv

def eat():
    itemlist = ['apple', 'exp_bottle']
    num_item = int(input('What you want to eat? ({}, {}) : '.format('1.apple','2.exp_bottle')))
    p.heal(itemlist[num_item-1])

def randomatk(entity ,name ,hp ,chance ,x ,y): #Player pet en emy
    old_hp = hp
    if random.randint(0,100) <= chance:
        hp -= random.randint(x,y)*2
        print('Critical Damage!')
        time.sleep(0.5)
    else:
        hp -= random.randint(x,y)

    if entity == 'player':
        p.hp -= old_hp-hp
    elif entity == 'enemy':
        enemy.hp -= old_hp-hp

    print('You deal {} dmg!' .format(old_hp-hp))
    if hp < 0:
        hp = 0
    print('{} hp {}-{} = {}'.format(name, old_hp, old_hp-hp, hp))


def checkhp():
        if p.hp > p.maxhp:
            p.hp = p.maxhp

def checkxp():
    print('yeah!')
    if p.xp > p.maxxp:
        p.xp = 0
        p.lv += 1
        if p.lv >= 100:
            p.maxxp += math.ceil(10+p.lv*1.25)-p.maxxp
            print(p.maxxp)
            print('Your lv is {}!'.format(p.lv))
    elif p.xp < 0:
        p.xp = 0    
       
def fight(lv):
    global c
    global enemy
    print('*'*20)
    mob_t1 = ['Zombie', 'Skeleton']
    mob_t2 = ['Boss_Zombie', 'Pun']
    mob_t3 = ['FaithNJ']
    print('You just walk into the wild...')
    time.sleep(1)

    lvmob = abs(random.randint(lv-2,lv+2))
    hp = random.randint((lvmob+2)*5,(lvmob+2)*5+4)

    if lv < 5:
        enemy = Entity(mob_t1[random.randint(0,1)],hp,lvmob)
    elif 5 <= lv < 10:
        enemy = Entity(mob_t2[random.randint(0,1)],hp,lvmob)
    elif lv >= 10:
        enemy = Entity(mob_t3[0],hp,lvmob)
    print('You find {} lv {} ({} hp)!' .format(enemy.name ,enemy.lv ,enemy.hp))
    
    while enemy.hp > 0 and p.hp > 0:
        c = input('What should you do? (1.fight, 2.pet, 3.eat, 4.run) : ')
        if c == 'fight' or c == '1':
            randomatk('enemy' ,enemy.name ,enemy.hp,10,5,10)
            if enemy.hp > 0:
                time.sleep(1)
                randomatk('player' ,p.name ,p.hp ,10 ,enemy.lv*5 ,enemy.lv*5+5)
        time.sleep(1)
        if c == 'eat' or c == '3':
            eat()

    old_xp = p.xp
    if enemy.hp <= 0:
        print('You won!')
        time.sleep(0.5)
        p.xp += (enemy.lv+1)*1.2
        print('You got {} xp!' .format(abs(old_xp-p.xp)))
        checkxp()
    elif p.hp <= 0:
        print('You lost...')
        time.sleep(1.2)
        p.xp -= (enemy.lv+1)*2.4
        print('You lost () xp...' .format(old))
    print('*'*20)

def confirm(answer):
    if answer == 'y':
        return 'y'
    elif answer == 'n':
        print('nope')
    else:
        print('error')
    time.sleep(0.5)
 
def start():
    global name
    global p
    name = input('Enter your name: ')
    ans = confirm(input('Are you sure to use this name? (y/n) : '))
    if ans == 'y':
        time.sleep(1)
        print('DONE! your name is {}\n' .format(name))
        p = Player(name,100,100,1,10,0)

def error():
    try:
        p
    except NameError:
        print('Error!'+'\n'+'*'*6)
        run()

def run():
    while True:
        c = input('Enter command: ')
        print('')
        if c == 'login':
            print('Enter your code: ')

        elif c == 'fight' or c == 'f':
            error()
            fight(p.lv)

        elif c == 'stat':
            error()
            p.stat()

        elif c == 'eat':
            error()
            eat()

        elif c == 'start':
            time.sleep(0.5)
            start()

        else:
           print('Error! PLease try again! ')

print('{}\nWelcome to the wild!\n{}'.format('*'*20,'*'*20))
run()    
