
from ursina import *
from direct.actor.Actor import Actor

app = Ursina()

entity = Entity(parent = scene)
#animations are stored within the file
actor = Actor("assets/models/minecraft_fox_walking_in_place/scene.gltf")
actor.reparent_to(entity)

actor.loop("ArmatureAction")  # use .play() instead of loop() to play it once.

app.run()