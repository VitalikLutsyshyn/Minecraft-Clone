from ursina import*
from ursina import Default

class MenuButton(Button):
    def __init__(self, text, action,x,y,parent):
        super().__init__(text=text,
                        on_click = action,
                        parent=parent,
                        text_size = 3,
                        color= color.white,
                        texture = "assets/button.png",
                        scale = (0.7,0.1),
                        x=x,
                        y=y,
                        origin = (0,0),#середина
                        ignore_paused=True,
                        highlight_scale=1.025,
                        highlight_color = color.rgb(150,150,150),
                        pressed_scale= 1.1)

class Menu(Entity):
    def __init__(self,game, **kwargs):
        super().__init__(parent= camera.ui,ignore_paused=True, **kwargs)
        self.background = Sprite("assets/backgraund.jpg",parent = self,z=1,color = color.white,scale = 0.1)   
        Text.default_font = "assets/MinecraftRegular-Bmg3.otf"
        # Text.sixe = 10
        # Text.default_resolution = 1080 *Text.size
        self.title = Text("Minecraft 2.0",scale = 5,parent=self,origin=(0,0),x=0,y=0.40)
        self.btns = [MenuButton("Save Game",game.save_game,0,0.15,self),
                     MenuButton("Continue",game.load_game,0,0,self),
                     MenuButton("New Game",game.new_game,0,-0.15,self),
                     MenuButton("Exit",application.quit,0,-0.3,self)]
        self.save_btn = self.btns[0]
        self.save_btn.enabled = False


if __name__ == '__main__':
    app = Ursina()
    menu = Menu()
    window.fullscreen = True
    app.run()