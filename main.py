from ursina import*
app = Ursina()#cтвореня гри

class Block(Entity):
    def __init__

block = Entity(model="assets\minecraft-grass-block\source\Minecraft_Grass_Block_OBJ\Grass_Block",
               texture="assets\minecraft-grass-block\source\Minecraft_Grass_Block_OBJ\Grass_Block_TEX.png",
               scale=2,
            position=(6,-5,100))
block.y = 10


app.run()