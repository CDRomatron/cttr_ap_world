from ..generic.Rules import add_rule
from .Regions import connect_regions, hubs

def set_rules(world, player: int, area_connections):
    connect_regions(world, player, hubs[0], hubs[0], lambda state: True)

    #midway checks behind MI access
    connect_regions(world, player, hubs[0], hubs[10], lambda state: state.can_reach("Adventure", "Region", player))

    #tier2 checks require all of tier 1 accessable plus HEF and TW
    connect_regions(world, player, hubs[0], hubs[6], lambda state: state.can_reach("Fairy", "Region", player)
                    and state.can_reach("Midway - Pasadena 1 (M5)", "Location", player)
                    and state.can_reach("Midway - N.Gin 1 (M6)", "Location", player)
                    and state.can_reach("Midway - Coco 1 (M7)", "Location", player)
                    and state.can_reach("Midway - Crunch 1 (M8)", "Location", player)
                    and state.can_reach("Midway - Nina 1 (M9)", "Location", player)
                    and state.can_reach("Midway - Von Clutch 1 (M10)", "Location", player)
                    and state.has("NGinSkin", player, 1)
                    and state.has("NinaSkin", player, 1))

    #tier3 checks require all of tier 2
    connect_regions(world, player, hubs[0], hubs[7], lambda state: state.can_reach("Dino", "Region", player)
                    and state.can_reach("Midway - Crash 2 (M15)","Location", player)
                    and state.can_reach("Midway - Coco 2 (M16)","Location", player)
                    and state.can_reach("Midway - Pasadena 2 (M17)","Location", player)
                    and state.can_reach("Midway - N. Gin 2 (M18)","Location", player)
                    and state.can_reach("Midway - Nina 2 (M26)","Location", player)
                    and state.can_reach("Midway - Crunch 2 (M27)","Location", player)
                    and state.can_reach("Midway - Von Clutch 2 (M28)","Location", player)
                    and state.can_reach("Midway - Cortex 2 (M29)","Location", player))
    #tier4 requires 3
    connect_regions(world, player, hubs[0], hubs[8], lambda state:
                    state.can_reach("Midway - Crash 3 (M33)", "Location", player)
                    and state.can_reach("Midway - Coco 3 (M34)", "Location", player)
                    and state.can_reach("Midway - Pasadena 3 (M36)", "Location", player)
                    and state.can_reach("Midway - N. Gin 3 (M48)", "Location", player)
                    and state.can_reach("Midway - Nina 3 (M46)", "Location", player)
                    and state.can_reach("Midway - Crunch 3 (M35)", "Location", player)
                    and state.can_reach("Midway - Von Clutch 3 (M45)", "Location", player)
                    and state.can_reach("Midway - Cortex 3 (M47)", "Location", player))

    #tier5 requires 4
    connect_regions(world, player, hubs[0], hubs[9], lambda state:
                    state.can_reach("Midway - Crash 4 (M59)", "Location", player)
                    and state.can_reach("Midway - Coco 4 (M61)", "Location", player)
                    and state.can_reach("Midway - Pasadena 4 (M64)", "Location", player)
                    and state.can_reach("Midway - N. Gin 4 (M65)", "Location", player)
                    and state.can_reach("Midway - Nina 4 (M66)", "Location", player)
                    and state.can_reach("Midway - Crunch 4 (M62)", "Location", player)
                    and state.can_reach("Midway - Von Clutch 4 (M67)", "Location", player)
                    and state.can_reach("Midway - Cortex 4 (M60)", "Location", player))

    connect_regions(world, player, hubs[0], hubs[1], lambda state: state.has("AdventureKey", player, 1))
    connect_regions(world, player, hubs[0], hubs[2], lambda state: state.has("FairyKey", player, 1))
    connect_regions(world, player, hubs[0], hubs[3], lambda state: state.has("DinoKey", player, 1))
    connect_regions(world, player, hubs[0], hubs[4], lambda state: state.has("EgyptKey", player, 1))
    connect_regions(world, player, hubs[0], hubs[5], lambda state: state.has("SolarKey", player, 1))

    world.completion_condition[player] = lambda state: state.can_reach("Solar", "Region", player)
