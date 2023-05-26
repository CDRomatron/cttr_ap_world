from ..generic.Rules import set_rule
from ..AutoWorld import LogicMixin
from BaseClasses import MultiWorld
from .Locations import Location, location_table, events_table


class CTTRLogic(LogicMixin):
    # Defs here

    def rule(self, player: int):
        return True

def set_rules(world: MultiWorld, player: int):
    def reachable_locations(state):
        return [location for location in world.get_locations() if
                location.player == player and
                location.can_reach(state)]
    
    goal = 20
    can_complete = lambda state: len(reachable_locations(state)) >= goal and state.can_reach('Astro Land', 'Region', player)

    if world.logic[player] != 'nologic':
        world.completion_condition[player] = lambda state: state.has('Victory', player)
    
    set_rule(world.get_entrance('Go to Mystery Island', player), lambda state: True)
    set_rule(world.get_entrance('Go to Happily Ever Faster', player), lambda state: True)
    set_rule(world.get_entrance('Go to Tyrannosaurus Wrecks', player), lambda state: True)
    set_rule(world.get_entrance('Go to Tomb Town', player), lambda state: True)
    set_rule(world.get_entrance('Go to Astro Land', player), lambda state: True)