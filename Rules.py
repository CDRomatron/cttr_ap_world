from ..generic.Rules import add_rule
from .Regions import connect_regions, hubs

def set_rules(world, player: int, area_connections):
    connect_regions(world, player, "Menu", hubs[0], lambda state: True)
    connect_regions(world, player, "Menu", hubs[1], lambda state: state.has("AdventureKey", player, 1))
    connect_regions(world, player, "Menu", hubs[2], lambda state: state.has("FairyKey", player, 1))
    connect_regions(world, player, "Menu", hubs[3], lambda state: state.has("DinoKey", player, 1))
    connect_regions(world, player, "Menu", hubs[4], lambda state: state.has("EgyptKey", player, 1))
    connect_regions(world, player, "Menu", hubs[5], lambda state: state.has("SolarKey", player, 1))

    world.completion_condition[player] = lambda state: state.can_reach("Solar", "Region", player)
