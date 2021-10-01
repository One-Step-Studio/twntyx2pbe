# building_type: one of the known types in a dynamic list in a db, starts from 1
# level : 0 is not constructed
# current_production_type: also the current one, single unit, 0 means upgrading the building itself
# in_production_time: time spent on the current unit
# queue: list of 5 max
max_queue = 5


class Building:
    def __init__(self,
                 building_type: int, level: int, current_production_type: int, in_production_until: int, queue: [int]):
        self.building_type = building_type
        self.level = 0 + level
        self.current_production_type = current_production_type
        self.in_production_until = in_production_until
        self.queue = [int]
        self.queue.append(queue)

    def add_to_queue(self, production_type: int):
        if self.queue.__len__() <= max_queue:
            self.queue.append(production_type)


class City:
    def __init__(self, buildings):
        self.buildings: Building = buildings

    def upgrade(self, building_type):
        for building in self.buildings:
            if building.building_type == building_type:
                building.add_to_queue(0)
