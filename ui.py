from ursina import*

class Menu(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent= camera.ui,ignore_paused=True, **kwargs)
        self.background = Sprite("assets/backgraund.jpg",parent = self,z=1,color = color.white,scale = 0.1)   

if __name__ == '__main__':
    app = Ursina()
    menu = Menu()
    app.run()