#first game 1.0
import random
import time

class Player:
	def __init__(self, name, maxhp, hp, lv):
        self.name = name
        self.maxhp = maxhp
        self.hp = hp
        self.lv = lv

    def stat(self):
        time.sleep(1)
        print('*'*10)
        print('{}' .format(self.name))
        print('HP = {}/{}' .format(self.maxhp,self.hp))
        print('LV = {}' .format(self.lv))
        print('Your code is {}' .format(str(self.name)+str(self.maxhp)+str(self.hp)+str(self.lv)))
        print('*'*10)

    def heal(self):
        if 

    def Basic_Attack_Player

class Pet(Player):
    def __init__(self, name, hp, lv):
        super().__init__(name, ,weight, height)
    def Basic_Attack_Pet(self, player):
        if random.randint(0,100) <= 10:
            Player.hp -= random.randint(5,10)*2
        else:
            Player.hp -= random.randint(5,10)
        
class Entity:
    def __init__(self, name, hp, lv):
        self.name = name
        self.hp = hp
        self.lv
    def Attack(self, player)
        randomatk(10,int(self.lv*1.2+5),int(self.lv*1.2+10))

def randomatk(chance,x,y)
    if random.randint(0,100) <= chance:
        Player.hp -= random.randint(x,y)*2
    else:
        Player.hp -= random.randint(x,y)

def fight(lv)
    global c
    mob_t1 = ['Zombie', 'Skeleton']
    mob_t2 = ['Boss_Zombie', 'Pun']
    mob_t3 = ['FaithNJ']

    print('You just walk into the wild...')
    time.sleep(1)

    lvmob = abs(random.randint(lv-2,lv+2))
    hp = random.randint(lvmob+1*5,lvmob*5+4)

    if lv < 5
        enemy = Entity(mob_t1[random.randint(0,1)],hp,lvmob)
    elif 5 <= lv < 10
        enemy = Entity(mob_t2[random.randint(0,1)],hp,lvmob)
    elif lv >= 10
        enemy = Entity(mob_t3[0],hp,lvmob)
    print('You find {}!' .format(enemy))
    
    while enemy.hp > 0:
        c = input('What should you do? (fight, pet, eat, run) : ')
        if c == 'fight'
            c2 = input('What move you want to use? ({}, {}) : '.format()) 


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
    name = 'FaithNJ'
    ans = 'y'
    if ans == 'y':
        time.sleep(1)
        print('DONE! your name is {}' .format(name))
        p = Player(name,10,0,1)

print('{}\nWelcome to the wild!\n{}'.format('*'*20,'*'*20))
while True:
    c = input('Enter command: ')
    if c == 'login':
        print('Enter your code: ')

    elif c == 'fight' or 'f':
        
    elif c == 'start':
        time.sleep(0.5)
        start()

    elif c == 'stat':
        try:
            p
        except NameError:
            print('start first!')
        else:
            if p.name == name:
                p.stat()

    else:
        print('Error! PLease try again! ')
    
