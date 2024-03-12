from ursina import*
from ursina.shaders import lit_with_shadows_shader, basic_lighting_shader
from settings import*
import os


def get_image_list(path):
    image_names = os.listdir(path)
    image_list = []
    for image in image_names:
        image_list.append(load_texture("assets/textures_block" + os.sep + image))
    
    return image_list

textures_list = get_image_list(BASE_DIR + "/assets/textures_block")

class Pickaxe(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = "assets/minecraft_diamond-pickaxe/scene",
            scale = 0.03,
            position = Vec2(0.5,-0.4),
            rotation = Vec3(-60,85,-71),
            shader = basic_lighting_shader  
        )
        self.build_sound = Audio("music/breaking_block.mp3",autoplay = False,volume = 0.3)

    def move(self):
        self.position =Vec2(0.5,-0.3)
        self.rotation =Vec3(-60,85,-71)
        self.build_sound.play()

    def stand(self):
        self.position = Vec2(0.5,-0.4)
        self.rotation =Vec3(-60,85,-71)



class Tree(Entity):
    map = []
    def __init__(self,pos,scale=3, **kwargs):
        super().__init__(parent=scene,
                         model="assets/minecraft_tree/scene",
                         scale= scale,
                         position = pos,
                         origin_y = 0.6,
                         shader = basic_lighting_shader,

                           **kwargs)
        Tree.map.append(self)

class Block(Button):
    number = 1
    map = []
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
        
        self.id = Block.number

    def check_object(self,x, y, z):
        hit_info = raycast(Vec3(x, y, z), direction=Vec3(0, 0, 0), distance=0) 
        if hit_info.hit:
            return False
        else:
            return True
        
    def input(self,key):
        if self.hovered: 
            if key == "left mouse down":
                axe.move()
                destroy(self)
                self.map.remove(self)
                

            elif key == "right mouse down":
                if self.check_object(*(self.position + mouse.normal)):
                    axe.move()
                    block = Block(self.position + mouse.normal)
                    Block.map.append(block)
            else:
                axe.stand()
        for i in range(10):
            if key == str(i):
                Block.number = i

axe = Pickaxe()