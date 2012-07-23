import operator as op

__all__ = ['Group']

class Group(list):
    # META ====================================================================
    def __init__(self, *game_objects):
        super(Group, self).__init__(game_objects)

    def add(self, *game_objects):
        for game_object in game_objects:
            self.append(game_object)

    def remove(self, *game_objects):
        for game_object in game_objects:
            super(Group, self).remove(game_object)

    def clear(self):
        super(Group, self).__init__([])
    # =========================================================================

    # COLLISION ===============================================================
    def they_collide(self, obj1, obj2):
        return obj1.collider.intersects(obj2.collider)


    def objs_colliding(self, obj):
        intersects = obj.collider.intersects
        return [other for other in self if
                (other is not obj) and intersects(other.collider)]

    def iter_colliding(self, obj):
        intersects = obj.collider.intersects
        for other in self:
            if other is not obj and intersects(other.collider):
                yield other

    def any_colliding(self, obj):
        for other in self:
            if self.they_collide(obj, other):
                return True

        return False

    def any_near(self, obj, near_distance): 
        near_than = obj.collider.near_than
        for other in self:
            if other is not obj and near_than(other.collider, near_distance):
                return other

        return None

    def objs_near(self, obj, near_distance): 
        near_than = obj.collider.near_than
        return [other for other in self if
                (other is not obj) and near_than(other.collider, near_distance)]

    def objs_near_wdistance(self, obj, near_distance):
        distance = obj.collider.distance
        res = []
        for other in self:
            if other is obj:
                continue

            d = distance(other.collider)
            if d <= near_distance:
                res.append((other, d))

        return res

    def ranked_objs_near(self, obj, near_distance):
        tmp = objs_near_wdistance(obj, near_distance)
        tmp.sort(key=op.itemgetter(1))

        return tmp

    def iter_all_collisions(self): 
        # O(n**2)
        for i, obj in enumerate(self):
            intersects = obj.collider.intersects
            for j, other in enumerate(self):
                if j >= i:
                    break
                if intersects(other.collider):
                    yield (obj, other)

    def objs_touching_point(self, x, y): 
        touching = set()
        for obj in self:
            if obj.collider.touches_point(x, y):
                touching.add(obj)
        
        return touching

    def objs_into_box(self, minx, maxx, miny, maxy): 
        into = set()
        packed_box = minx, maxx, miny, maxy
        for obj in self:
            if obj.collider.fits_in_box(packed_box):
                into.add(obj)

        return into
    # =========================================================================

    def update(self, tick):
        for game_object in self:
            game_object.update(tick)

    def draw(self):
        for game_object in self:
            game_object.draw()
