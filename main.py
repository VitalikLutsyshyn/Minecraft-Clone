#ЗНАЙТИ БЛОКИ ЩЕ
from ursina import*
from ursina.prefabs.sky import Sky
from ursina.shaders import lit_with_shadows_shader, basic_lighting_shader
from perlin_noise import PerlinNoise
import random
import os
import math
import pickle     
app = Ursina()#cтвореня гри
from settings import*
from models import Tree,Block,Pickaxe,Player,axe,Fox
from ui import Menu


class Controller(Entity):
    def __init__(self):
        super().__init__()
        self.start = False
        self.player = Player()
        self.sky = Sky()
        self.player.y = 100
        self.music = Audio("music/fon_music.mp3",loop = True,volume = 0.1)

        self.music.play()
        window.fullscreen = True
        pivot = Entity()
        DirectionalLight(parent=pivot, y=2, z=3, shadows=True,rotation = (45,-45,45))
        self.menu = Menu(self)
        self.toggle_menu()
        mouse.locked = False
        mouse.visible = True
    
    def toggle_menu(self):
        application.paused = not application.paused
        self.menu.enabled =   application.paused
        self.menu.visible =  self.menu.visible
        mouse.locked = not mouse.locked
        mouse.visible = not mouse.visible
        axe.enabled = not axe.enabled

    

    def update(self):
         if self.player.y <  - 30:
            self.player.y = 100
            self.load_game()
    
    def clear_map(self):
        for block in Block.map:
            destroy(block)

        for tree in Tree.map:
            destroy(tree)

        Block.map.clear()
        Tree.map.clear()    


    def new_game(self):
        self.start = True
        self.menu.save_btn.enabled =True
        self.clear_map()
        noise = PerlinNoise(octaves=3,seed=random.randint(100,10000))
        for x in range(-MAP_SIZE,MAP_SIZE):
            for z in range(-MAP_SIZE,MAP_SIZE):
                height = noise([x*0.02,z*0.02])
                height = math.floor(height*7.5)
                block = Block((x,height,z))
                Block.map.append(block)
            
                rand_num = random.randint(0,100)
                if rand_num == 15:
                    tree1 = Tree((x,height+1,z),scale = random.randint(4,7))

                rand_num = random.randint(0,1000)
                if rand_num == 15:
                    fox = Fox((x,height+0.5,z))

        self.toggle_menu()

    def save_game(self): 
        if self.start:   
            with open("save.dat","wb") as file:
                pickle.dump(self.player.position,file)
                pickle.dump(len(Block.map),file)
                for block in Block.map:
                    pickle.dump(block.position,file)
                    pickle.dump(block.id,file)

                pickle.dump(len(Tree.map),file)
                for tree in Tree.map:
                    pickle.dump(tree.position,file)
                    pickle.dump(tree.scale,file)
            self.toggle_menu()

    def load_game(self):
        self.start = True
        self.menu.save_btn.enabled =True
        self.clear_map()
        try:
            with open("save.dat","rb") as file:
                self.player.position = pickle.load(file)
                block_count = pickle.load(file)
                for i in range(block_count):
                    pos = pickle.load(file)
                    Block.number = pickle.load(file)
                    block = Block(pos)
                    Block.map.append(block)
                tree_count = pickle.load(file)
                for i in range(tree_count):
                    pos = pickle.load(file)
                    scale = pickle.load(file)
                    tree = Tree(pos,scale)
        except:
            self.new_game()
        self.toggle_menu()
        

    def input(self,key):
        if key == "m":
            self.save_game()

        if key == "n":
            self.new_game()

        if key == "l":
            self.load_game()
        
        if key == "escape":
            self.toggle_menu()





game = Controller()
# game.load_game()

app.run()