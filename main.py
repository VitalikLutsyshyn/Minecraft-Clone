from ursina import*
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.sky import Sky
from ursina.shaders import lit_with_shadows_shader, basic_lighting_shader
from perlin_noise import PerlinNoise
import random
import os
import math     

BASE_DIR = os.getcwd() #повертає адрежу точного файлу
MAP_SIZE = 25
app = Ursina()#cтвореня гри

def get_image_list(path):
    image_names = os.listdir(path)
    image_list = []
    for image in image_names:
        image_list.append(load_texture("assets/textures_block" + os.sep + image))
    
    return image_list



textures_list = get_image_list(BASE_DIR + "/assets/textures_block")
# Функція, яка перевіряє наявність об'єкта в певній точці
def check_object(x, y, z):
    hit_info = raycast(Vec3(x, y, z), direction=Vec3(0, 0, 0), distance=0) 
    if hit_info.hit:
        return False
    else:
        return True


class Tree(Entity):
    def __init__(self,pos,scale=3, **kwargs):
        super().__init__(parent=scene,
                         model="assets/minecraft_tree/scene",
                         scale= scale,
                         position = pos,
                         origin_y = 0.6,
                         shader = basic_lighting_shader,

                           **kwargs)


class Block(Button):
    number = 1

    def __init__(self,pos,**kwargs):
        super().__init__(parent=scene,
            model="cube",
               texture= textures_list[Block.number],
               collider = "box",
               scale=1,
            position=pos,
            origin_y=0,
            color = color.color(0,0,random.uniform(0.9,1.0)),
            highlight_color = color.rgb(100,49,200),
            shader = basic_lighting_shader,
            **kwargs)
    def input(self,key):
        if self.hovered:
            if key == "left mouse down":
                destroy(self)
            elif key == "right mouse down":
                if check_object(*(self.position + mouse.normal)):
                    Block(self.position + mouse.normal)

        for i in range(10):
            if key == str(i):
                Block.number = i
        

noise = PerlinNoise(octaves=4,seed=random.randint(100,10000))

for x in range(-MAP_SIZE,MAP_SIZE):
    for z in range(-MAP_SIZE,MAP_SIZE):
        height = noise([x*0.02,z*0.02])
        height = math.floor(height*7.5)
        block = Block((x,height,z))
    
        rand_num = random.randint(0,100)
        if rand_num == 15:
            tree1 = Tree((x,height+1,z),scale = random.randint(4,7))

player = FirstPersonController()
sky = Sky()
player.y = 100
window.fullscreen = True

pivot = Entity()
DirectionalLight(parent=pivot, y=2, z=3, shadows=True,rotation = (45,-45,45))
# scene.fog_density = 0.05 
# scene.fog_color = color.rgb(153,192,255)
app.run()