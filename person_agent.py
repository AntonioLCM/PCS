"""
    Team: Eight minus one
    Description: A class for 'person agents' to be used in an abm within
                 Mesa.
"""

import mesa
from generate_arrow_list import generate_arrow_list
from Blueprints.arrow_priority import arrow_priority


EXIT1 = [(70, 18), (71, 18), (72, 18), (73, 18)]
EXIT2 = [(61, 33), (62, 33)]
EXIT3 = [(79, 158), (80, 158), (81, 158), (82, 158), (83, 158)]
EXIT4 = [(76, 181), (77, 181), (78, 181), (79, 181)]
ALL_EXITS = EXIT1 + EXIT2 + EXIT3 + EXIT4

ARROWS = generate_arrow_list(ALL_EXITS)


class PersonAgent(mesa.Agent):
    def __init__(self, unique_id, model):
        # Initialize as Agent from mesa
        super().__init__(unique_id, model)

        # Define state etc. below
        self.dir = None
        self.arrows = ARROWS
        self.best_ar = None

    def _sees_exit(self):
        # Check if there is an exit in neighborhood with range max_vis (visible
        # distance in smoke). There's probably an efficient way to check this
        # instead of just checking all possible neighborhood cells
        pass

    def move(self):
        # If no arrows in visibility range randomwalk, if arrow(s) then find
        # best exit according to distance between arrow and exit and move
        # towards this exit. After passing the arrow keep moving in direction
        # of arrow.
        neighbor_cells = self.model.grid.get_neighborhood(self.pos, moore=True)

        if vis_ars := self.visible_arrows():
            self.best_ar = self.find_best_exit(vis_ars)
            if self.pos == self.best_ar.pos:
                self.dir = self.best_ar.dir
                self.arrows.remove(self.best_ar)
                self.best_ar = None

            if self.best_ar and (new_pos := self.calc_move(self.best_ar.pos)):
                self.model.grid.move_agent(self, new_pos)
        elif self.dir and (new_pos := self.pos_by_dir(self.dir)):
            self.model.grid.move_agent(self, new_pos)
        else:
            # This could probably be more efficient using numpy somehow..
            # TODO: ^
            possible_empty = [cell for cell in neighbor_cells
                              if self.model.grid.is_cell_empty(cell)]
            if len(possible_empty) != 0:
                self.model.grid.move_agent(self,
                                           self.random.choice(possible_empty))

    def pos_by_dir(self, direction):
        neighbor_cells = self.model.grid.get_neighborhood(self.pos, moore=True)
        possible_empty = [cell for cell in neighbor_cells
                          if self.model.grid.is_cell_empty(cell)]
        x, y = self.pos
        if direction == 0 and (x, y + 1) in possible_empty:
            return (x, y + 1)
        elif direction == 1 and (x + 1, y) in possible_empty:
            return (x + 1, y)
        elif direction == 2 and (x, y - 1) in possible_empty:
            return (x, y - 1)
        elif direction == 3 and (x - 1, y) in possible_empty:
            return (x - 1, y)
        return False

    def get_empty_neighborhood(self):
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        pass

    def calc_move(self, loc):
        possible_moves = []
        neighbor_cells = self.model.grid.get_neighborhood(self.pos, moore=True)
        possible_empty = [cell for cell in neighbor_cells
                          if self.model.grid.is_cell_empty(cell)]
        x, y = self.pos
        i, j = loc[0] - x, loc[1] - y
        print(i, j)
        if i >= 0 and j >= 0:
            possible_moves = [(x + 1, y + 1), (x + 1, y), (x, y + 1)]
        elif i >= 0 and j <= 0:
            possible_moves = [(x + 1, y - 1), (x + 1, y), (x, y - 1)]
        elif i <= 0 and j <= 0:
            possible_moves = [(x - 1, y - 1), (x - 1, y), (x, y - 1)]
        elif i <= 0 and j >= 0:
            possible_moves = [(x - 1, y + 1), (x - 1, y), (x, y + 1)]
        if possible_moves:
            legal_moves = [dest for dest in possible_moves
                           if dest in possible_empty]
            if legal_moves:
                return self.random.choice(legal_moves)
        return False

    def find_best_exit(self, arrows):
        nearest_exit = None
        exit_dist = 9999
        for ar in arrows:
            ar_exit, dist = arrow_priority(ar.exit_priority)
            if dist < exit_dist:
                nearest_exit = ar
                exit_dist = dist
        return nearest_exit

    def visible_arrows(self):
        # Collect all arrows visible within range (max_vis)
        vis_arrows = []
        for arrow in self.arrows:
            if arrow.is_in_range(self.pos, self.model.max_vis):
                vis_arrows.append(arrow)
        return vis_arrows

    def step(self):
        if self.pos in EXIT1:
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)
            self.model.person_agents -= 1
            self.model.counter_EXIT1 += 1
        elif self.pos in EXIT2:
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)
            self.model.person_agents -= 1
            self.model.counter_EXIT2 += 1
        elif self.pos in EXIT3:
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)
            self.model.person_agents -= 1
            self.model.counter_EXIT3 += 1
        elif self.pos in EXIT4:
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)
            self.model.person_agents -= 1
            self.model.counter_EXIT4 += 1
        else:
            self.move()
