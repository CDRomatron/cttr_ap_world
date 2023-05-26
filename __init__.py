import os

from .Items import CTTRItem, item_table, item_frequencies
from .Locations import CTTRLocation, location_table, exclusion_table, events_table
from .Regions import cttr_regions, default_connections
from .Rules import set_rules
from worlds.generic.Rules import exclusion_rules

from BaseClasses import Region, Entrance, Item
from .Options import cttr_options
from ..AutoWorld import World

client_version = 5

class CTTRWorld(World):
    game: str = "CTTR"
    options = cttr_options
    topology_present = True

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.id for name, data in location_table.items()}

    data_version = 2

    