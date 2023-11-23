from pico2d import *
import game_world
import game_framework
import random
import server

class Ball:
    image = None

    def __init__(self, x = None, y = None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(100, 1180)
        self.y = y if y else random.randint(100, 924)
        self.sx, self.sy = self.x, self.y

    def draw(self):
        self.image.draw(self.sx, self.sy)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.sx += math.cos(server.boy.dir) * -1 * server.boy.speed * game_framework.frame_time
        self.sy += math.sin(server.boy.dir) * -1 * server.boy.speed * game_framework.frame_time
        pass

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
	    pass

