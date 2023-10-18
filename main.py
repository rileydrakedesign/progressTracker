import pandas as pd 
import numpy as np
import kivy
from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.lang import Builder 

Builder.load_file('gui.kv')

class MyLayout(Widget):
    def checkbox_click(slef, instance, value):
        if value == True:
            pass
        else:
            pass
    

class progressApp(App):
    def build(self):
        return MyLayout()
    
if __name__ == '__main__':
    progressApp().run()