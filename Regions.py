from ...BaseClasses import MultiWorld, Region, Entrance
from Locations import CTTRLocation, midway_table, adventure_table, fairy_table, dino_table, egypt_table, solar_table, \
    location_table

hubs = ["Midway","Adventure","Fairy","Dino","Egypt","Solar"]

def create_regions(world: MultiWorld, player: int):
    reg1 = Region("Midway", player, world)
    reg1.locations += [CTTRLocation(player, loc_name, location_table[loc_name], reg1) for loc_name in midway_table]

    reg2 = Region("Adventure", player, world)
    reg2.locations += [CTTRLocation(player, loc_name, location_table[loc_name], reg2) for loc_name in adventure_table]

    reg3 = Region("Fairy", player, world)
    reg3.locations += [CTTRLocation(player, loc_name, location_table[loc_name], reg3) for loc_name in fairy_table]

    reg4 = Region("Dino", player, world)
    reg4.locations += [CTTRLocation(player, loc_name, location_table[loc_name], reg4) for loc_name in dino_table]

    reg5 = Region("Egypt", player, world)
    reg5.locations += [CTTRLocation(player, loc_name, location_table[loc_name], reg5) for loc_name in egypt_table]

    reg6 = Region("Solar", player, world)
    reg6.locations += [CTTRLocation(player, loc_name, location_table[loc_name], reg6) for loc_name in solar_table]

def connect_regions(world: MultiWorld, player: int, source: str, target: str, rule=None):
    sourceRegion = world.get_region(source, player)
    targetRegion = world.get_region(target, player)

    connection = Entrance(player, '', sourceRegion)
    if rule:
        connection.access_rule = rule

    sourceRegion.exits.append(connection)
    connection.connect(targetRegion)