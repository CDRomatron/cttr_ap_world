from worlds.AutoWorld import World, WebWorld
from BaseClasses import Item, Tutorial, ItemClassification, MultiWorld
from .Items import item_table, CTTRItem
from .Locations import location_table, CTTRLocation
from .Options import cttr_options
from .Regions import create_regions, hubs
from .Rules import set_rules
import typing
import os
import json


class CTTRWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up CTTR for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["testname"]
    )]

class CTTRWorld(World):
    """
    An open world Crash Bandicoot adventure game. Oh yeah, and there's racing or something.
    """

    game: str = "CTTR"
    topology_present = False

    web = CTTRWeb()

    item_name_to_id = item_table
    location_name_to_id = location_table

    data_version = 1

    area_connections: typing.Dict[int, int]

    option_definitions = cttr_options

    def __init__(self, world: MultiWorld, player: int):
        super().__init__(world,player)

    def create_regions(self):
        create_regions(self.multiworld, self.player)
        self.multiworld.clear_location_cache()

    def set_rules(self):
        self.area_connections = {}
        set_rules(self.multiworld, self.player, self.area_connections)

    def create_item(self, name: str) -> Item:
        item_id = item_table[name]
        if name == "Crystal":
            classification = ItemClassification.filler
        else:
            classification = ItemClassification.progression

        item = CTTRItem(name, classification, item_id, self.player)
        return item

    def create_items(self):
        adventurekey = self.create_item("AdventureKey")
        fairykey = self.create_item("FairyKey")
        dinokey = self.create_item("DinoKey")
        egyptkey = self.create_item("EgyptKey")
        solarkey = self.create_item("SolarKey")
        self.multiworld.itempool += [adventurekey, fairykey, dinokey, egyptkey, solarkey]
        self.multiworld.itempool += [self.create_item("CrashCar") for i in range(0, 5)]
        self.multiworld.itempool += [self.create_item("CortexCar") for i in range(0, 6)]
        self.multiworld.itempool += [self.create_item("CocoCar") for i in range(0, 6)]
        self.multiworld.itempool += [self.create_item("CrunchCar") for i in range(0, 6)]
        self.multiworld.itempool += [self.create_item("PasadenaCar") for i in range(0, 6)]
        self.multiworld.itempool += [self.create_item("NinaCar") for i in range(0, 6)]
        self.multiworld.itempool += [self.create_item("NGinCar") for i in range(0, 6)]
        self.multiworld.itempool += [self.create_item("VonClutchCar") for i in range(0, 6)]
        remaining = len(self.multiworld.itempool)
        self.multiworld.itempool += [self.create_item("Crystal") for i in range(0, 94)]

    def fill_slot_data(self):
        return {
            #"total_crystals": self.multiworld.total_crystals.value
        }
    def generate_output(self, output_directory: str):
        if self.multiworld.players != 1:
            return
        data = {
            "slot_data": self.fill_slot_data(),
            "location_to_item": {self.location_name_to_id[i.name]: item_table[i.item.name] for i in
                                 self.multiworld.get_locations()},
            "data_package": {
                "data": {
                    "games": {
                        self.game: {
                            "item_name_to_id": self.item_name_to_id,
                            "location_name_to_id": self.location_name_to_id
                        }
                    }
                }
            }
        }
        filename = f"{self.multiworld.get_out_file_name_base(self.player)}.apcttr"
        with open(os.path.join(output_directory, filename), 'w') as f:
            json.dump(data, f)
