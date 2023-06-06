from BaseClasses import MultiWorld, Region, Entrance
from .Locations import CTTRLocation, midway_table, adventure_table, fairy_table, dino_table, egypt_table, solar_table, \
    midway_tier2_table, midway_tier3_table, midway_tier4_table, midway_tier5_table, midway_tier1_table, adv1_table,\
    adv2_table, adv3_table, fai1_table, fai2_table, fai3_table, din1_table, din2_table, din3_table, egy1_table,\
    egy2_table, egy3_table, sol1_table, sol2_table, sol3_table, gem_table, location_table

hubs = ["Menu","Adventure","Fairy","Dino","Egypt","Solar","Tier2","Tier3","Tier4","Tier5", "Tier1"]

def create_regions(world: MultiWorld, player: int):
    menu = Region("Menu", player, world)
    menu.locations += [CTTRLocation(player, loc_name, location_table[loc_name], menu) for loc_name in midway_table]

    tier1 = Region("Tier1", player, world)
    tier1.locations += [CTTRLocation(player, loc_name, location_table[loc_name], tier1) for loc_name in midway_tier1_table]

    tier2 = Region("Tier2", player, world)
    tier2.locations += [CTTRLocation(player, loc_name, location_table[loc_name], tier2) for loc_name in midway_tier2_table]

    tier3 = Region("Tier3", player, world)
    tier3.locations += [CTTRLocation(player, loc_name, location_table[loc_name], tier3) for loc_name in midway_tier3_table]

    tier4 = Region("Tier4", player, world)
    tier4.locations += [CTTRLocation(player, loc_name, location_table[loc_name], tier4) for loc_name in midway_tier4_table]

    tier5 = Region("Tier5", player, world)
    tier5.locations += [CTTRLocation(player, loc_name, location_table[loc_name], tier5) for loc_name in midway_tier5_table]

    adventure = Region("Adventure", player, world)
    adventure.locations += [CTTRLocation(player, loc_name, location_table[loc_name], adventure) for loc_name in adventure_table]

    fairy = Region("Fairy", player, world)
    fairy.locations += [CTTRLocation(player, loc_name, location_table[loc_name], fairy) for loc_name in fairy_table]

    dino = Region("Dino", player, world)
    dino.locations += [CTTRLocation(player, loc_name, location_table[loc_name], dino) for loc_name in dino_table]

    egypt = Region("Egypt", player, world)
    egypt.locations += [CTTRLocation(player, loc_name, location_table[loc_name], egypt) for loc_name in egypt_table]

    solar = Region("Solar", player, world)
    solar.locations += [CTTRLocation(player, loc_name, location_table[loc_name], solar) for loc_name in solar_table]

    adv1 = Region("Adv1", player, world)
    adv1.locations += [CTTRLocation(player, loc_name, location_table[loc_name], adv1) for loc_name in adv1_table]

    adv2 = Region("Adv2", player, world)
    adv2.locations += [CTTRLocation(player, loc_name, location_table[loc_name], adv2) for loc_name in adv2_table]

    adv3 = Region("Adv3", player, world)
    adv3.locations += [CTTRLocation(player, loc_name, location_table[loc_name], adv3) for loc_name in adv3_table]

    fai1 = Region("Fai1", player, world)
    fai1.locations += [CTTRLocation(player, loc_name, location_table[loc_name], fai1) for loc_name in fai1_table]

    fai2 = Region("Fai2", player, world)
    fai2.locations += [CTTRLocation(player, loc_name, location_table[loc_name], fai2) for loc_name in fai2_table]

    fai3 = Region("Fai3", player, world)
    fai3.locations += [CTTRLocation(player, loc_name, location_table[loc_name], fai3) for loc_name in fai3_table]

    din1 = Region("Din1", player, world)
    din1.locations += [CTTRLocation(player, loc_name, location_table[loc_name], din1) for loc_name in din1_table]

    din2 = Region("Din2", player, world)
    din2.locations += [CTTRLocation(player, loc_name, location_table[loc_name], din2) for loc_name in din2_table]

    din3 = Region("Din3", player, world)
    din3.locations += [CTTRLocation(player, loc_name, location_table[loc_name], din3) for loc_name in din3_table]

    egy1 = Region("Egy1", player, world)
    egy1.locations += [CTTRLocation(player, loc_name, location_table[loc_name], egy1) for loc_name in egy1_table]

    egy2 = Region("Egy2", player, world)
    egy2.locations += [CTTRLocation(player, loc_name, location_table[loc_name], egy2) for loc_name in egy2_table]

    egy3 = Region("Egy3", player, world)
    egy3.locations += [CTTRLocation(player, loc_name, location_table[loc_name], egy3) for loc_name in egy3_table]

    sol1 = Region("Sol1", player, world)
    sol1.locations += [CTTRLocation(player, loc_name, location_table[loc_name], sol1) for loc_name in sol1_table]

    sol2 = Region("Sol2", player, world)
    sol2.locations += [CTTRLocation(player, loc_name, location_table[loc_name], sol2) for loc_name in sol2_table]

    sol3 = Region("Sol3", player, world)
    sol3.locations += [CTTRLocation(player, loc_name, location_table[loc_name], sol3) for loc_name in sol3_table]

    adva = Region("AdvA", player, world)
    adva.locations += [CTTRLocation(player, "Arena - Jungle Rumble (A)", location_table["Arena - Jungle Rumble (A)"], adva)]
    adva.locations += [CTTRLocation(player, "Arena - Jungle Rumble (B)", location_table["Arena - Jungle Rumble (B)"], adva)]

    dina = Region("DinA", player, world)
    dina.locations += [
        CTTRLocation(player, "Arena - Extinction Party (A)", location_table["Arena - Extinction Party (A)"], dina)]
    dina.locations += [
        CTTRLocation(player, "Arena - Extinction Party (B)", location_table["Arena - Extinction Party (B)"], dina)]

    faia = Region("FaiA", player, world)
    faia.locations += [
        CTTRLocation(player, "Arena - Hardly Ever Land", location_table["Arena - Hardly Ever Land"], faia)]

    sola = Region("SolA", player, world)
    sola.locations += [
        CTTRLocation(player, "Arena - Space Stunts", location_table["Arena - Space Stunts"], sola)]

    adventureKey = Region("AdventurePad", player, world)
    adventureKey.locations += [CTTRLocation(player, "MI - Gem Collection", location_table["MI - Gem Collection"], adventureKey)]

    fairyKey = Region("FairyPad", player, world)
    fairyKey.locations += [
        CTTRLocation(player, "HEF - Gem Collection", location_table["HEF - Gem Collection"], fairyKey)]

    dinoKey = Region("DinoPad", player, world)
    dinoKey.locations += [
        CTTRLocation(player, "TW - Gem Collection", location_table["TW - Gem Collection"], dinoKey)]

    egyptKey = Region("EgyptPad", player, world)
    egyptKey.locations += [
        CTTRLocation(player, "TT - Gem Collection", location_table["TT - Gem Collection"], egyptKey)]

    solarKey = Region("SolarPad", player, world)
    solarKey.locations += [
        CTTRLocation(player, "AL - Ending", location_table["AL - Ending"], solarKey)]

    world.initialize_regions([menu,adventure,fairy,dino,egypt,solar,tier2,tier3,tier4,tier5,tier1,adv1,adv2,adv3,
                              fai1,fai2,fai3,din1,din2,din3,egy1,egy2,egy3,sol1,sol2,sol3,adva,dina,faia,sola,
                              adventureKey, fairyKey, dinoKey, egyptKey, solarKey])
    world.regions = [menu,adventure,fairy,dino,egypt,solar,tier2,tier3,tier4,tier5,tier1,adv1,adv2,adv3,
                              fai1,fai2,fai3,din1,din2,din3,egy1,egy2,egy3,sol1,sol2,sol3,adva,dina,faia,sola,
                              adventureKey, fairyKey, dinoKey, egyptKey, solarKey]

def connect_regions(world: MultiWorld, player: int, source: str, target: str, rule=None):
    sourceRegion = world.get_region(source, player)
    targetRegion = world.get_region(target, player)

    connection = Entrance(player, '', sourceRegion)
    if rule:
        connection.access_rule = rule

    sourceRegion.exits.append(connection)
    connection.connect(targetRegion)