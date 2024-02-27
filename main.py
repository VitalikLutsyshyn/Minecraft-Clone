from ursina import*
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.sky import Sky
from ursina.shaders import lit_with_shadows_shader, basic_lighting_shader
from perlin_noise import PerlinNoise
import random
import os
import math     

app = Ursina()#cтвореня гри
from settings import*
from models import Tree,Block,Pickaxe


class Controller(Entity):
    def __init__(self):
        super().__init__()
        self.player = FirstPersonController()
        self.sky = Sky()
        self.player.y = 100
        window.fullscreen = True
        pivot = Entity()
        DirectionalLight(parent=pivot, y=2, z=3, shadows=True,rotation = (45,-45,45))

    def new_game(self):
        noise = PerlinNoise(octaves=4,seed=random.randint(100,10000))
        for x in range(-MAP_SIZE,MAP_SIZE):
            for z in range(-MAP_SIZE,MAP_SIZE):
                height = noise([x*0.02,z*0.02])
                height = math.floor(height*7.5)
                block = Block((x,height,z))
            
                rand_num = random.randint(0,100)
                if rand_num == 15:
                    tree1 = Tree((x,height+1,z),scale = random.randint(4,7))

game = Controller()
game.new_game()

app.run()