from ursina import*
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.sky import Sky
import os


BASE_DIR = os.getcwd() #повертає адрежу точного файлу

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
    hit_info = raycast(Vec3(x, y, z), direction=Vec3(0, -1, 0), distance=1) 
    if hit_info.hit:
        return True 
    else:
        return False

print(textures_list)

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
        



for x in range(-10,10):
    for z in range(-10,10):
        block = Block((x,0,z))
    
player = FirstPersonController()
sky = Sky()
player.y = 30
window.fullscreen = True


app.run()