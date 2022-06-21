from tkinter import *
import json
import pathlib
import math

PATH = str(pathlib.Path(__file__).parent.resolve())+'/'

RED = '#fd564d'
GREY = '#1A2223'

class Game:
    def __init__(self, root):
        self.root = root
        self.producers = []
        self.upgrades = []
        
        with open(PATH+'producers.json') as json_file:
            self.json_data = json.load(json_file)
    
        self.mill = [' ', ' ', ' Mil', ' Bil', ' Tril', ' Quad', ' Quin', 'Sext']

    def millify(self, x):
        x = float(x)
        if x >= 1000000:
            index = max(0,min(len(self.mill)-1, int(math.floor(0 if x == 0 else math.log10(abs(x))/3))))
            return '{:.2f}{}'.format(x / 10**(3 * index), self.mill[index])
        else:
            return "{:,}".format(round(x))
    
    def widget_manager(self):
        pass
    
    def da_stats(self, master):
        pass
    
    def da_markget(self, master):
        pass
    
    def upgrades(self, master):
        pass
    
    def p_producer(self, item):
        pass
    
    def p_upgrade(self, item):
        pass
    
    def tick(self):
        self.root.after(50, self.tick)

if __name__ == '__main__':
    root = Tk()
    root.title('Bamboo farming simulator')
    app = Game(root)
    app.tick()
    root.minsize(1024, 576)
    root.maxsize(1024, 576)
    root.mainloop()