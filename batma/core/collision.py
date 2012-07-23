import batma

__all__ = ['Collider', 'CircleCollider', 'BoxCollider']

class Collider(object):
    def __init__(self):
        batma.engine.all_colliders.append(self)

    # def __del__(self):
    #     if batma.engine:
    #         batma.engine.all_colliders.remove(self)

    def contains(self, other): pass
    def intersects(self, other): pass
    def near_than(self, other, near_distance): pass
    def touches_point(self, x, y): pass
    def fits_in_box(self, packed_box): pass
    def minmax(self): pass
    def copy(self): pass
    def draw(self): pass

class BoxCollider(Collider):
    def __init__(self, center, half_width, half_height):
        super(BoxCollider, self).__init__()
        self.x, self.y = center
        self.__width = half_width*2
        self.__half_width = half_width
        self.__height = half_height*2
        self.__half_height = half_height

    def get_center(self):
        return batma.Vector2(self.x, self.y)
    def set_center(self, value):
        self.x, self.y = value
    center = property(get_center, set_center)

    def get_width(self):
        return self.__width
    def set_width(self, value):
        self.__width = value
        self.__half_width = value/2.0
    width = property(get_width, set_width)

    def get_height(self):
        return self.__height
    def set_height(self, value):
        self.__height = value
        self.__half_height = value/2.0
    height = property(get_height, set_height)

    def get_half_width(self):
        return self.__half_width
    def set_half_width(self, value):
        self.__half_width = value
        self.__width = value*2.0
    half_width = property(get_half_width, set_half_width)
        
    def get_half_height(self):
        return self.__half_height
    def set_half_height(self, value):
        self.__half_height = value
        self.__height = value*2.0
    half_height = property(get_half_height, set_half_height)

    def contains(self):
        a = self.minmax()
        b = other.minmax()

        if (b[0] > a[0] and b[1] < a[1] and b[2] > a[2] and b[3] < a[3]):
            return True

        return False

    def intersects(self, other):
        if isinstance(other, CircleCollider):
            return _intersects_circle_box(other, self)
        else:
            return _intersects_box_box(self, other)

    def distance(self, other):
        d = max((abs(self.center[0] - other.center[0])-self.half_width - other.half_width,
                abs(self.center[1] - other.center[1])-self.half_height - other.half_height ))
        if d<0.0:
            d = 0.0
        return d
    
    def near_than(self, other, near_distance):
        return ( abs(self.center[0] - other.center[0]) - self.half_width - other.half_width < near_distance and
                 abs(self.center[1] - other.center[1]) - self.half_height - other.half_height < near_distance)

    def touches_point(self, x, y):
        return ( abs(self.center[0] - x) < self.half_width and
                 abs(self.center[1] - y) < self.half_height )

    def fits_in_box(self, packed_box):
        return ( (packed_box[0] + self.half_width <= self.center[0] <= packed_box[1] - self.half_width) and
                 (packed_box[2] + self.half_height <= self.center[1] <= packed_box[3] - self.half_height) )

    def minmax(self):
        return (self.center[0] - self.half_width, self.center[0] + self.half_width,
                self.center[1] - self.half_height, self.center[1] + self.half_height)

    def copy(self):
        return BoxCollider(batma.Vector2(*self.center), self.half_width, self.half_height)

    def draw(self):
        batma.draw.rect(
            rect=(
                self.center[0] - self.half_width,
                self.center[1] - self.half_height,
                self.width,
                self.height
            ),
            color=batma.display.collider_color,
            width=1,
        )


class CircleCollider(Collider):
    def __init__(self, center, radius):
        super(CircleCollider, self).__init__()
        self.x, self.y = center
        self.__radius = radius
        self.__radius2 = radius**2

    def get_center(self):
        return batma.Vector2(self.x, self.y)
    def set_center(self, value):
        self.x, self.y = value
    center = property(get_center, set_center)

    def get_radius(self):
        return self.__radius
    def set_radius(self, value):
        self.__radius = value
        self.__radius2 = value**2
    radius = property(get_radius, set_radius)

    def get_radius2(self):
        return self.__radius2
    radius2 = property(get_radius2)

    def contains(self):
        a = self.minmax()
        b = other.minmax()

        if (b[0] > a[0] and b[1] < a[1] and b[2] > a[2] and b[3] < a[3]):
            return True

        return False

    def intersects(self, other):
        if isinstance(other, BoxCollider):
            return _intersects_circle_box(self, other)
        else:
            return _intersects_circle_circle(self, other)

    def distance(self, other):
        d = abs(self.center - other.center) - self.radius - other.radius
        if d<0.0:
            d = 0.0
        return d
    
    def near_than(self, other, near_distance):
        return abs(self.center - other.center) <= self.radius + other.radius + near_distance

    def touches_point(self, x, y):
        return abs(self.center - (x,y)) <= self.radius

    def fits_in_box(self, packed_box):
        r = self.radius
        return ( ((packed_box[0] + r) <= self.center[0] <= (packed_box[1] - r)) and
                 ((packed_box[2] + r) <= self.center[1] <= (packed_box[3] - r)) )

    def minmax(self):
        r = self.radius
        return (self.center[0]-r, self.center[0]+r,
                self.center[1]-r, self.center[1]+r)

    def copy(self):
        return CircleCollider(batma.Vector2(*self.center), self.radius)

    def draw(self):
        batma.draw.circle(
            center=self.center,
            radius=self.radius,
            color=batma.display.collider_color,
            width=1,
        )

def _intersects_box_box(box1, box2):
    return ( abs(box1.center[0] - box2.center[0]) < box1.half_width + box2.half_width and
             abs(box1.center[1] - box2.center[1]) < box1.half_height + box2.half_height )

def _intersects_circle_circle(circle1, circle2):
    return abs(circle1.center - circle2.center) < circle1.radius + circle2.radius

def _intersects_circle_box(circle, box):
    x_min, x_max, y_min, y_max = box.minmax()
    x, y = circle.center

    sq_dist = 0.0
    if x < x_min:
        sq_dist += (x_min - x)**2
    if x > x_max:
        sq_dist += (x - x_max)**2
    if y < y_min:
        sq_dist += (y_min - y)**2
    if y > y_max:
        sq_dist += (y - y_max)**2

    return sq_dist <= circle.radius2
