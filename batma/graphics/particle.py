# -*- coding:utf-8 -*-
# Copyright (c) 2011 Renato de Pontes Pereira, renato.ppontes at gmail dot com
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.

import os
import random
import numpy as np
import ctypes
from OpenGL import GL as gl

import batma
from batma.maths import mathematic as math
from batma.core.gameobject import GameObject
from batma.maths.algebra import Vector2

__all__ = ['ParticleSystem']

# Constants ===================================================================
POSITION_FREE = 0
POSITION_GROUPED = 1

# Utility Functions ===========================================================
rand = lambda: random.random()*2 - 1

def pointer_to_numpy(a, ptype=ctypes.c_float):
    a = np.ascontiguousarray(a)           # Probably a NO-OP, but perhaps not
    return a.ctypes.data_as(ctypes.POINTER(ptype)) # Ugly and undocumented! 

# Main Class ==================================================================
class ParticleSystem(GameObject):
    def __init__(self, total_particles=0, texture=None, duration=0.0, 
                       gravity=None, pos_var=None, origin=None, angle=0.0, 
                       angle_var=0.0, speed=0.0, speed_var=0.0, 
                       tangential_accel=0.0,  tangential_accel_var=0.0, 
                       radial_accel=0.0, radial_accel_var=0.0, size=1.0, 
                       size_var=0.0, life=1.0, life_var=0.0, start_color=None, 
                       start_color_var=None, end_color=None, end_color_var=None, 
                       emission_rate=None, blend_additive=False, 
                       position_type=POSITION_GROUPED):
        super(ParticleSystem, self).__init__()

        if texture is None:
            texture = batma.resource.load_image_texture(
                os.path.join(os.path.dirname(__file__), 'assets', 'fire.png')
            )[0]
        elif isinstance(texture, basestring):
            texture = batma.resource.load_image_texture(texture)[0]

        if emission_rate is None:
            if life != 0 and total_particles != 0:
                emission_rate = self.total_particles/self.life
            else:
                emission_rate = 1.0

        self.total_particles = total_particles
        self.texture = texture
        self.duration = duration
        self.gravity = gravity or Vector2(0, 0)
        self.pos_var = pos_var or Vector2(0, 0)
        self.origin = origin or Vector2(0, 0)
        self.angle = angle
        self.angle_var = angle_var
        self.speed = speed
        self.speed_var = speed_var
        self.tangential_accel = tangential_accel
        self.tangential_accel_var = tangential_accel_var
        self.radial_accel = radial_accel
        self.radial_accel_var = radial_accel_var
        self.size = size
        self.size_var = size_var
        self.life = life
        self.life_var = life_var
        self.start_color = start_color or batma.Color(0, 0, 0, 0)
        self.start_color_var = start_color_var or batma.Color(0, 0, 0, 0)
        self.end_color = end_color or batma.Color(0, 0, 0, 0)
        self.end_color_var = end_color_var or batma.Color(0, 0, 0, 0)
        self.emission_rate = emission_rate
        self.blend_additive = blend_additive
        self.position_type = position_type

        self.particle_pos = np.zeros((self.total_particles, 2), np.float32)
        self.particle_dir = np.zeros((self.total_particles, 2), np.float32)
        self.particle_rad = np.zeros((self.total_particles, 1), np.float32)
        self.particle_tan = np.zeros((self.total_particles, 1), np.float32)
        self.particle_grav = np.zeros((self.total_particles, 2), np.float32)
        self.particle_color = np.zeros((self.total_particles, 4), np.float32)
        self.particle_delta_color = np.zeros((self.total_particles, 4), np.float32)
        self.particle_life = -np.ones((self.total_particles, 1), np.float32)
        self.particle_size = np.zeros((self.total_particles, 1), np.float32)
        self.particle_start_pos = np.zeros((self.total_particles, 2), np.float32)

        self.active = True
        self.elapsed = 0
        self.emit_counter = 0
        self.particle_count = 0
        self.auto_remove_on_finish = False

    def add_particle(self):
        a = self.particle_life < 0
        idxs = a.nonzero()
        idx = -1

        if len(idxs[0] > 0):
            idx = idxs[0][0]
        else:
            raise Exception('Non Empty Particle')

        self.particle_pos[idx][0] = self.origin[0] + self.pos_var[0]*rand()
        self.particle_pos[idx][1] = self.origin[1] + self.pos_var[1]*rand()

        self.particle_start_pos[idx][0] = self.origin[0]
        self.particle_start_pos[idx][1] = self.origin[1]

        a = math.radians(self.angle + self.angle_var*rand())
        v = Vector2(math.cos(a), math.sin(a))
        s = self.speed + self.speed_var*rand()

        dir = v*s

        self.particle_dir[idx][0] = dir[0]
        self.particle_dir[idx][1] = dir[1]

        self.particle_rad[idx] = self.radial_accel + self.radial_accel_var*rand()

        self.particle_tan[idx] = self.tangential_accel + self.tangential_accel_var*rand()
        
        life = self.particle_life[idx] = self.life + self.life_var * rand()

        sr = self.start_color[0] + self.start_color_var[0]*rand()
        sg = self.start_color[1] + self.start_color_var[1]*rand()
        sb = self.start_color[2] + self.start_color_var[2]*rand()
        sa = self.start_color[3] + self.start_color_var[3]*rand()

        self.particle_color[idx][0] = sr
        self.particle_color[idx][1] = sg
        self.particle_color[idx][2] = sb
        self.particle_color[idx][3] = sa

        er = self.end_color[0] + self.end_color_var[0]*rand()
        eg = self.end_color[1] + self.end_color_var[1]*rand()
        eb = self.end_color[2] + self.end_color_var[2]*rand()
        ea = self.end_color[3] + self.end_color_var[3]*rand()

        delta_color_r = (er-sr)/life
        delta_color_g = (eg-sg)/life
        delta_color_b = (eb-sb)/life
        delta_color_a = (ea-sa)/life

        self.particle_delta_color[idx][0] = delta_color_r
        self.particle_delta_color[idx][1] = delta_color_g
        self.particle_delta_color[idx][2] = delta_color_b
        self.particle_delta_color[idx][3] = delta_color_a

        self.particle_size[idx] = self.size + self.size_var*rand()

        self.particle_grav[idx][0] = self.gravity[0]
        self.particle_grav[idx][1] = self.gravity[1]

        self.particle_count += 1

    def update_particles(self, tick):
        mtick = tick/1000.0

        norm = np.sqrt(self.particle_pos[:,0]**2 + self.particle_pos[:,1]**2)
        norm = np.select([norm==0], [0.0000001], default=norm)
        posx = self.particle_pos[:,0]/norm
        posy = self.particle_pos[:,1]/norm

        radial = np.array([posx, posy])
        tangential = np.array([-posy, posx])

        radial = np.swapaxes(radial, 0, 1)
        radial *= self.particle_rad
        tangential = np.swapaxes(tangential, 0, 1)
        tangential *= self.particle_tan

        self.particle_dir +=  (tangential + radial + self.particle_grav)*mtick

        self.particle_pos += self.particle_dir*mtick

        self.particle_life -= mtick

        if self.position_type == POSITION_FREE:
            tuple = np.array(self.origin)
            tmp = tuple - self.particle_start_pos
            self.particle_pos -= tmp

        self.particle_color += self.particle_delta_color*mtick
        self.particle_color[:,3] = np.select([self.particle_life[:,0] < 0], [0], default=self.particle_color[:,3])

    def update(self, tick):
        if not self.enabled: return 

        mtick = tick/1000.0
        self.particle_count = np.sum(self.particle_life >= 0)

        if self.active:
            rate = 1.0/self.emission_rate
            self.emit_counter += mtick

            while self.particle_count < self.total_particles and self.emit_counter > rate:
                self.add_particle()
                self.emit_counter -= rate

            self.elapsed += mtick
            if self.duration != -1 and self.duration < self.elapsed:
                self.active = False
                self.elapsed = self.duration
                self.emit_counter = 0

        self.update_particles(tick)

    def draw(self):
        if not self.visible: return

        gl.glPushMatrix()
        self.transform()

        gl.glPointSize(self.size)
        gl.glBindTexture(gl.GL_TEXTURE_2D, self.texture)

        gl.glEnable(gl.GL_POINT_SPRITE)
        gl.glTexEnvi(gl.GL_POINT_SPRITE, gl.GL_COORD_REPLACE, gl.GL_TRUE)

        # gl.glDisable(gl.GL_CULL_FACE)
        # gl.glDisable(gl.GL_DEPTH_TEST)

        gl.glEnableClientState(gl.GL_VERTEX_ARRAY)
        vertex_ptr = pointer_to_numpy(self.particle_pos)
        gl.glVertexPointer(2, gl.GL_FLOAT, 0, vertex_ptr)

        gl.glEnableClientState(gl.GL_COLOR_ARRAY)
        color_ptr = pointer_to_numpy(self.particle_color)
        gl.glColorPointer(4, gl.GL_FLOAT, 0, color_ptr)

        gl.glPushAttrib(gl.GL_COLOR_BUFFER_BIT)

        gl.glEnable(gl.GL_BLEND)
        if self.blend_additive:
            gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)
            gl.glDrawArrays(gl.GL_POINTS, 0, self.total_particles)
            
            gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE)
        else:
            gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)

        gl.glDrawArrays(gl.GL_POINTS, 0, self.total_particles)
        gl.glPopAttrib()
        gl.glDisableClientState(gl.GL_COLOR_ARRAY)
        gl.glDisableClientState(gl.GL_VERTEX_ARRAY)
        gl.glDisable(gl.GL_POINT_SPRITE)

        gl.glPopMatrix()


# =============================================================================
# Particle Systems
# =============================================================================

class Firework(ParticleSystem):
    def __init__(self, total_particles=3000, texture=None, duration=-1.0, 
                       gravity=None, pos_var=None, origin=None, angle=90, 
                       angle_var=20, speed=180, speed_var=50, 
                       tangential_accel=0.0,  tangential_accel_var=0.0, 
                       radial_accel=0.0, radial_accel_var=0.0, size=8.0, 
                       size_var=2.0, life=3.5, life_var=1.0, start_color=None, 
                       start_color_var=None, end_color=None, end_color_var=None, 
                       emission_rate=None, blend_additive=False, 
                       position_type=POSITION_GROUPED):

        gravity = gravity or batma.Vector2(0, -90)
        pos_var = pos_var or batma.Vector2(0, 0)
        start_color = start_color or batma.Color(0.5, 0.5, 0.5, 1.0)
        start_color_var = start_color_var or batma.Color(0.5,  0.5,  0.5 , 1.0)
        end_color = end_color or batma.Color(0.1, 0.1, 0.1, 0.2)
        end_color_var = end_color_var or batma.Color(0.1, 0.1, 0.1, 0.2)
        emission_rate = emission_rate or total_particles/life

        super(Firework, self).__init__(
            total_particles, texture, duration, gravity, pos_var, origin, angle, 
            angle_var, speed, speed_var, tangential_accel, tangential_accel_var, 
            radial_accel, radial_accel_var, size, size_var, life, life_var, 
            start_color, start_color_var, end_color, end_color_var, 
            emission_rate, blend_additive, position_type
        )

class Explosion(ParticleSystem):
    def __init__(self, total_particles=7000, texture=None, duration=0.1, 
                       gravity=None, pos_var=None, origin=None, angle=90.0, 
                       angle_var=360.0, speed=70.0, speed_var=40.0, 
                       tangential_accel=0.0,  tangential_accel_var=0.0, 
                       radial_accel=0.0, radial_accel_var=0.0, size=15.0, 
                       size_var=10.0, life=5.0, life_var=2.0, start_color=None, 
                       start_color_var=None, end_color=None, end_color_var=None, 
                       emission_rate=None, blend_additive=False, 
                       position_type=POSITION_GROUPED):

        gravity = gravity or batma.Vector2(0, -90)
        pos_var = pos_var or batma.Vector2(0, 0)
        start_color = start_color or batma.Color(0.7, 0.2, 0.1, 1.0)
        start_color_var = start_color_var or batma.Color(0.5, 0.5, 0.5, 0.0)
        end_color = end_color or batma.Color(0.5, 0.5, 0.5, 0.0)
        end_color_var = end_color_var or batma.Color(0.5, 0.5, 0.5, 0.0)
        emission_rate = emission_rate or total_particles/life

        super(Explosion, self).__init__(
            total_particles, texture, duration, gravity, pos_var, origin, angle, 
            angle_var, speed, speed_var, tangential_accel, tangential_accel_var, 
            radial_accel, radial_accel_var, size, size_var, life, life_var, 
            start_color, start_color_var, end_color, end_color_var, 
            emission_rate, blend_additive, position_type
        )

class Fire(ParticleSystem):
    def __init__(self, total_particles=250, texture=None, duration=-1.0, 
                       gravity=None, pos_var=None, origin=None, angle=90.0, 
                       angle_var=10.0, speed=60.0, speed_var=20.0, 
                       tangential_accel=0.0,  tangential_accel_var=0.0, 
                       radial_accel=0.0, radial_accel_var=0.0, size=100.0, 
                       size_var=10.0, life=3.0, life_var=0.25, start_color=None, 
                       start_color_var=None, end_color=None, end_color_var=None, 
                       emission_rate=None, blend_additive=True, 
                       position_type=POSITION_GROUPED):

        gravity = gravity or batma.Vector2(0, 0)
        pos_var = pos_var or batma.Vector2(40, 20)
        # start_color = start_color or batma.Color(0.9, 0.1, 0.1, 1.0)
        start_color = start_color or batma.Color(0.76, 0.25, 0.12, 1.0)
        start_color_var = start_color_var or batma.Color(0.0, 0.0, 0.0, 0.0)
        end_color = end_color or batma.Color(0.0, 0.0, 0.0, 1.0)
        end_color_var = end_color_var or batma.Color(0.0, 0.0, 0.0, 0.0)
        emission_rate = emission_rate or total_particles/life

        super(Fire, self).__init__(
            total_particles, texture, duration, gravity, pos_var, origin, angle, 
            angle_var, speed, speed_var, tangential_accel, tangential_accel_var, 
            radial_accel, radial_accel_var, size, size_var, life, life_var, 
            start_color, start_color_var, end_color, end_color_var, 
            emission_rate, blend_additive, position_type
        )

class Flower(ParticleSystem):
    def __init__(self, total_particles=500, texture=None, duration=-1.0, 
                       gravity=None, pos_var=None, origin=None, angle=90.0, 
                       angle_var=360.0, speed=80.0, speed_var=10.0, 
                       tangential_accel=15.0,  tangential_accel_var=0.0, 
                       radial_accel=-60.0, radial_accel_var=0.0, size=30.0, 
                       size_var=0.0, life=4.0, life_var=1.0, start_color=None, 
                       start_color_var=None, end_color=None, end_color_var=None, 
                       emission_rate=None, blend_additive=True, 
                       position_type=POSITION_GROUPED):

        gravity = gravity or batma.Vector2(0, 0)
        pos_var = pos_var or batma.Vector2(0, 0)
        start_color = start_color or batma.Color(0.5, 0.5, 0.5, 1.0)
        start_color_var = start_color_var or batma.Color(0.5, 0.5, 0.5, 0.0)
        end_color = end_color or batma.Color(0.0, 0.0, 0.0, 1.0)
        end_color_var = end_color_var or batma.Color(0.0, 0.0, 0.0, 0.0)
        emission_rate = emission_rate or total_particles/life

        super(Flower, self).__init__(
            total_particles, texture, duration, gravity, pos_var, origin, angle, 
            angle_var, speed, speed_var, tangential_accel, tangential_accel_var, 
            radial_accel, radial_accel_var, size, size_var, life, life_var, 
            start_color, start_color_var, end_color, end_color_var, 
            emission_rate, blend_additive, position_type
        )

class Sun(ParticleSystem):
    def __init__(self, total_particles=350, texture=None, duration=-1.0, 
                       gravity=None, pos_var=None, origin=None, angle=90.0, 
                       angle_var=360.0, speed=20.0, speed_var=5.0, 
                       tangential_accel=0.0,  tangential_accel_var=0.0, 
                       radial_accel=0.0, radial_accel_var=0.0, size=40.0, 
                       size_var=0.0, life=1.0, life_var=0.5, start_color=None, 
                       start_color_var=None, end_color=None, end_color_var=None, 
                       emission_rate=None, blend_additive=True, 
                       position_type=POSITION_GROUPED):

        gravity = gravity or batma.Vector2(0, 0)
        pos_var = pos_var or batma.Vector2(0, 0)
        start_color = start_color or batma.Color(0.75, 0.25, 0.12, 1.0)
        start_color_var = start_color_var or batma.Color(0.0, 0.0, 0.0, 0.0)
        end_color = end_color or batma.Color(0.0, 0.0, 0.0, 0.0)
        end_color_var = end_color_var or batma.Color(0.0, 0.0, 0.0, 0.0)
        emission_rate = emission_rate or total_particles/life

        super(Sun, self).__init__(
            total_particles, texture, duration, gravity, pos_var, origin, angle, 
            angle_var, speed, speed_var, tangential_accel, tangential_accel_var, 
            radial_accel, radial_accel_var, size, size_var, life, life_var, 
            start_color, start_color_var, end_color, end_color_var, 
            emission_rate, blend_additive, position_type
        )

class Spiral(ParticleSystem):
    def __init__(self, total_particles=500, texture=None, duration=-1.0, 
                       gravity=None, pos_var=None, origin=None, angle=90.0, 
                       angle_var=0.0, speed=150.0, speed_var=0.0, 
                       tangential_accel=45.0,  tangential_accel_var=0.0, 
                       radial_accel=-380.0, radial_accel_var=0.0, size=20.0, 
                       size_var=10.0, life=12.0, life_var=0.0, start_color=None, 
                       start_color_var=None, end_color=None, end_color_var=None, 
                       emission_rate=None, blend_additive=True, 
                       position_type=POSITION_GROUPED):

        gravity = gravity or batma.Vector2(0, 0)
        pos_var = pos_var or batma.Vector2(0, 0)
        start_color = start_color or batma.Color(0.5, 0.5, 0.5, 1.0)
        start_color_var = start_color_var or batma.Color(0.5, 0.5, 0.5, 0.0)
        end_color = end_color or batma.Color(0.5, 0.5, 0.5, 1.0)
        end_color_var = end_color_var or batma.Color(0.5, 0.5, 0.5, 0.0)
        emission_rate = emission_rate or total_particles/life

        super(Spiral, self).__init__(
            total_particles, texture, duration, gravity, pos_var, origin, angle, 
            angle_var, speed, speed_var, tangential_accel, tangential_accel_var, 
            radial_accel, radial_accel_var, size, size_var, life, life_var, 
            start_color, start_color_var, end_color, end_color_var, 
            emission_rate, blend_additive, position_type
        )

class Meteor(ParticleSystem):
    def __init__(self, total_particles=150, texture=None, duration=-1.0, 
                       gravity=None, pos_var=None, origin=None, angle=90.0, 
                       angle_var=360.0, speed=15.0, speed_var=5.0, 
                       tangential_accel=0.0,  tangential_accel_var=0.0, 
                       radial_accel=-0.0, radial_accel_var=0.0, size=60.0, 
                       size_var=10.0, life=2.0, life_var=1.0, start_color=None, 
                       start_color_var=None, end_color=None, end_color_var=None, 
                       emission_rate=None, blend_additive=True, 
                       position_type=POSITION_GROUPED):

        gravity = gravity or batma.Vector2(-200, 100)
        pos_var = pos_var or batma.Vector2(0, 0)


        start_color = start_color or batma.Color(0.2, 0.7, 0.7, 1.0)
        start_color_var = start_color_var or batma.Color(0.0, 0.0, 0.0, 0.0)
        end_color = end_color or batma.Color(0.0, 0.0, 0.0, 1.0)
        end_color_var = end_color_var or batma.Color(0.0, 0.0, 0.0, 0.0)
        emission_rate = emission_rate or total_particles/life

        super(Meteor, self).__init__(
            total_particles, texture, duration, gravity, pos_var, origin, angle, 
            angle_var, speed, speed_var, tangential_accel, tangential_accel_var, 
            radial_accel, radial_accel_var, size, size_var, life, life_var, 
            start_color, start_color_var, end_color, end_color_var, 
            emission_rate, blend_additive, position_type
        )

class Galaxy(ParticleSystem):
    def __init__(self, total_particles=200, texture=None, duration=-1.0, 
                       gravity=None, pos_var=None, origin=None, angle=90.0, 
                       angle_var=360.0, speed=60.0, speed_var=10.0, 
                       tangential_accel=80.0,  tangential_accel_var=0.0, 
                       radial_accel=-80.0, radial_accel_var=0.0, size=37.0, 
                       size_var=10.0, life=4.0, life_var=1.0, start_color=None, 
                       start_color_var=None, end_color=None, end_color_var=None, 
                       emission_rate=None, blend_additive=True, 
                       position_type=POSITION_GROUPED):

        gravity = gravity or batma.Vector2(0, 0)
        pos_var = pos_var or batma.Vector2(0, 0)


        start_color = start_color or batma.Color(0.12, 0.25, 0.76, 1.0)
        start_color_var = start_color_var or batma.Color(0.0, 0.0, 0.0, 0.0)
        end_color = end_color or batma.Color(0.0, 0.0, 0.0, 0.0)
        end_color_var = end_color_var or batma.Color(0.0, 0.0, 0.0, 0.0)
        emission_rate = emission_rate or total_particles/life

        super(Galaxy, self).__init__(
            total_particles, texture, duration, gravity, pos_var, origin, angle, 
            angle_var, speed, speed_var, tangential_accel, tangential_accel_var, 
            radial_accel, radial_accel_var, size, size_var, life, life_var, 
            start_color, start_color_var, end_color, end_color_var, 
            emission_rate, blend_additive, position_type
        )

class Smoke(ParticleSystem):
    def __init__(self, total_particles=80, texture=None, duration=-1.0, 
                       gravity=None, pos_var=None, origin=None, angle=90.0, 
                       angle_var=10.0, speed=25.0, speed_var=10.0, 
                       tangential_accel=0.0,  tangential_accel_var=0.0, 
                       radial_accel=5.0, radial_accel_var=0.0, size=40.0, 
                       size_var=10.0, life=4.0, life_var=1.0, start_color=None, 
                       start_color_var=None, end_color=None, end_color_var=None, 
                       emission_rate=None, blend_additive=True, 
                       position_type=POSITION_GROUPED):

        gravity = gravity or batma.Vector2(0, 0)
        pos_var = pos_var or batma.Vector2(01, 0)


        start_color = start_color or batma.Color(0.5, 0.5, 0.5, 0.1)
        start_color_var = start_color_var or batma.Color(0.0, 0.0, 0.0, 0.1)
        end_color = end_color or batma.Color(0.5, 0.5, 0.5, 0.1)
        end_color_var = end_color_var or batma.Color(0.0, 0.0, 0.0, 0.1)
        emission_rate = emission_rate or total_particles/life

        super(Smoke, self).__init__(
            total_particles, texture, duration, gravity, pos_var, origin, angle, 
            angle_var, speed, speed_var, tangential_accel, tangential_accel_var, 
            radial_accel, radial_accel_var, size, size_var, life, life_var, 
            start_color, start_color_var, end_color, end_color_var, 
            emission_rate, blend_additive, position_type
        )
