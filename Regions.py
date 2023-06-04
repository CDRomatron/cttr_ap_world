from BaseClasses import MultiWorld, Region, Entrance
from .Locations import CTTRLocation, midway_table, adventure_table, fairy_table, dino_table, egypt_table, solar_table, \
    midway_tier2_table, midway_tier3_table, midway_tier4_table, midway_tier5_table, midway_tier1_table, location_table

hubs = ["Menu","Adventure","Fairy","Dino","Egypt","Solar","Tier2","Tier3","Tier4","Tier5", "Tier1"]

def create_regions(world: MultiWorld, player: int):
    reg1 = Region("Menu", player, world)
    reg1.locations += [CTTRLocation(player, loc_name, location_table[loc_name], reg1) for loc_name in midway_table]

    regZ = Region("Tier1", player, world)
    regZ.locations += [CTTRLocation(player, loc_name, location_table[loc_name], regZ) for loc_name in midway_tier1_table]

    regA = Region("Tier2", player, world)
    regA.locations += [CTTRLocation(player, loc_name, location_table[loc_name], regA) for loc_name in midway_tier2_table]

    regB = Region("Tier3", player, world)
    regB.locations += [CTTRLocation(player, loc_name, location_table[loc_name], regB) for loc_name in midway_tier3_table]

    regC = Region("Tier4", player, world)
    regC.locations += [CTTRLocation(player, loc_name, location_table[loc_name], regC) for loc_name in midway_tier4_table]

    regD = Region("Tier5", player, world)
    regD.locations += [CTTRLocation(player, loc_name, location_table[loc_name], regD) for loc_name in midway_tier5_table]

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

    world.initialize_regions([reg1,reg2,reg3,reg4,reg5,reg6,regA,regB,regC,regD,regZ])
    world.regions = [reg1,reg2,reg3,reg4,reg5,reg6,regA,regB,regC,regD,regZ]

def connect_regions(world: MultiWorld, player: int, source: str, target: str, rule=None):
    sourceRegion = world.get_region(source, player)
    targetRegion = world.get_region(target, player)

    connection = Entrance(player, '', sourceRegion)
    if rule:
        connection.access_rule = rule

    sourceRegion.exits.append(connection)
    connection.connect(targetRegion)