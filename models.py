from ursina import*
from ursina.shaders import lit_with_shadows_shader, basic_lighting_shader
from settings import*
import os
from ursina.prefabs.first_person_controller import FirstPersonController
from direct.actor.Actor import Actor

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

class Player(FirstPersonController):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.step_sound = Audio("music/step.mp3",autoplay=False,loop = True,volume = 0.07)


    def update(self):
        super().update()
        if held_keys["w"] or held_keys["s"] or held_keys["a"] or held_keys["d"]:
            if not self.step_sound.playing and self.grounded:
                self.step_sound.play()
        else:   
            if self.step_sound.playing:
                self.step_sound.stop()

class Fox(Entity):
    def __init__(self,pos,**kwargs):
        super().__init__(parent=scene,
                         scale= 0.7,
                         position = pos,
                         origin_y = 0,
                         shader = basic_lighting_shader,
                         collider = "mesh",
                           **kwargs)
             
        self.actor = Actor("assets/models/minecraft_fox_walking_in_place/scene.gltf")
        self.actor.reparent_to(self)
        self.actor.loop("ArmatureAction") 
        self.dir = Vec3(1,0,1)#напрямок лисиці
        # self.rotation = self.dir
        self.rotation_y += 90
        self.step = 0.2

    def can_move(self,new_pos):
        # for block in Block.map:
            hit_info = raycast(new_pos, direction=self.rotation, distance=self.step) 
            if hit_info.hit:
                return False
            else:
                return True



    def update(self):
        new_position = self.position + self.dir * self.step
        if self.can_move(new_position):
            self.position = new_position






axe = Pickaxe()