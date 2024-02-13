from ursina import*
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.sky import Sky
app = Ursina()#cтвореня гри

class Block(Button):
    def __init__(self,pos,**kwargs):
        super().__init__(parent=scene,
            model="assets\minecraft-grass-block\source\Minecraft_Grass_Block_OBJ\Grass_Block",
               texture="assets\minecraft-grass-block\source\Minecraft_Grass_Block_OBJ\Grass_Block_TEX.png",
               collider = "box",
               scale=0.5,
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
                Block(self.position + mouse.normal)




for x in range(-10,10):
    for z in range(-10,10):
        block = Block((x,0,z))
    
player = FirstPersonController()
sky = Sky()
player.y = 30
window.fullscreen = True


app.run()