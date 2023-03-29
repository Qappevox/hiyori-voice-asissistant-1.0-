#using python 3.6.8
"""
req:
kivy
kivymd
playsound
gTTS
speech_recognition
"""
try:
    #kivy imports
    from kivy.uix.screenmanager import ScreenManager, Screen
    from kivy.core.window import Window
    from kivy.config import Config
    import kivy
    from kivymd.app import MDApp
    #modules
    from optimizeSystem import optimizer
    from hiyori import App
    import time
except ModuleNotFoundError:
    print("Modules are not installed")
    exit()

kivy.require('1.9.0')
Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '200')
Window.size = (200, 240)

class HiyoriVoiceAssistant(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def build(self):
        global screen, screens
        Window.borderless = False
        self.theme_cls.theme_style = "Light"  
        self.theme_cls.primary_palette = "BlueGray"
        return App()

app = HiyoriVoiceAssistant()
optimizer.optimizeSys()

if __name__ == "__main__":
    app.run()