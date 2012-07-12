# -*- coding:utf-8 -*-

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from OpenGL import GL as gl

import batma

class Image(object):
    def __init__(self, filename):
        surface = pygame.image.load(filename)
        self.width = surface.get_width()
        self.height = surface.get_height()
        data = pygame.image.tostring(surface, 'RGBA', 1)
        self.surface = gl.glGenTextures(1)
        gl.glBindTexture(gl.GL_TEXTURE_2D, self.surface)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
        gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGBA, self.width, self.height, 0, gl.GL_RGBA, gl.GL_UNSIGNED_BYTE, data)

    def __del__(self):
        if self.surface is not None:
            if gl.glDeleteTextures is not None:
                gl.glDeleteTextures(self.surface)
                self.surface = None


    def draw(self, position=(0, 0), rotation=0.0, scale=1, origin=(0, 0)):
        texwidth = self.width# * scale
        texheight = self.height# * scale

        if origin is None:
            originx = texwidth / 2
            originy = texheight / 2
        else:
            originx = origin[0]# * scale
            originy = origin[1]# * scale

        gl.glPushMatrix()
        #gl.glTranslatef(position[0], position[1], 0)

        #if rotation is not 0.0:
        #    gl.glRotatef(rotation, 0, 0, 1)

        gl.glColor4f(1, 1, 1, 1)
        gl.glBindTexture(gl.GL_TEXTURE_2D, self.surface)

        gl.glBegin(gl.GL_TRIANGLE_STRIP)
        gl.glTexCoord2f(0, 1)#self.height_ratio); 
        gl.glVertex2f(-originx, texheight - originy)
        gl.glTexCoord2f(1, 1)#self.width_ratio, self.height_ratio); 
        gl.glVertex2f(texwidth - originx, texheight - originy)
        gl.glTexCoord2f(0, 1); 
        gl.glVertex2f(-originx, -originy)
        gl.glTexCoord2f(1, 1)#self.width_ratio, 1); 
        gl.glVertex2f(texwidth - originx, -originy)
        gl.glEnd()
        
        gl.glPopMatrix()

        # gl.glPushMatrix();
        # gl.glTranslatef(320, 240, 0);


        # gl.glColor4f(0, 0, 0, 1)
        # gl.glDisable(gl.GL_TEXTURE_2D)

        # gl.glBegin(gl.GL_QUADS);
        # gl.glColor3f(1, 0, 0);
        # gl.glVertex2f(100, 100);
        # gl.glVertex2f(100, 200);
        # gl.glVertex2f(200, 200);
        # gl.glVertex2f(200, 0);       
        # gl.glEnd();

        # gl.glEnable(gl.GL_TEXTURE_2D)
        # gl.glPopMatrix();


class Game(batma.Scene):
    def initialize(self):
        pass
    
    def load_content(self):
        pass

    def unload_content(self):
        pass

    def update(self, tick):
        if batma.keyboard.is_clicked('quit'): #ESC or ALT+F4
            batma.engine.stop()
    
    def draw(self):
        batma.draw.circle(batma.mouse.position, radius=35, width=1)

game = Game()
batma.run(game)