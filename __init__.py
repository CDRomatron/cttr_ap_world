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
from random import shuffle


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
        #keys
        adventurekey = self.create_item("AdventureKey")
        fairykey = self.create_item("FairyKey")
        dinokey = self.create_item("DinoKey")
        egyptkey = self.create_item("EgyptKey")
        solarkey = self.create_item("SolarKey")

        keys = [0, 1, 2, 3]
        keyitems = [adventurekey, fairykey, dinokey, egyptkey]
        locations = ["MI - Gem Collection", "HEF - Gem Collection", "TW - Gem Collection", "TT - Gem Collection"]
        shuffle(keys)

        #self.multiworld.itempool += [adventurekey, fairykey, dinokey, egyptkey, solarkey]
        self.multiworld.get_location("Midway - Gem Collection", self.player).place_locked_item(keyitems[keys[0]])
        self.multiworld.get_location(locations[keys[0]], self.player).place_locked_item(keyitems[keys[1]])
        self.multiworld.get_location(locations[keys[1]], self.player).place_locked_item(keyitems[keys[2]])
        self.multiworld.get_location(locations[keys[2]], self.player).place_locked_item(keyitems[keys[3]])
        self.multiworld.get_location(locations[keys[3]], self.player).place_locked_item(solarkey)


        #skins
        cortexskin = self.create_item("CortexSkin")
        cocoskin = self.create_item("CocoSkin")
        pasadenaskin = self.create_item("PasadenaSkin")
        crunchskin = self.create_item("CrunchSkin")
        nginskin = self.create_item("NGinSkin")
        ninaskin = self.create_item("NinaSkin")
        vonclutchskin = self.create_item("VonClutchSkin")

        self.multiworld.itempool += [cortexskin, cocoskin, pasadenaskin, crunchskin, nginskin, ninaskin, vonclutchskin]

        self.multiworld.itempool += [self.create_item("CrashCar") for i in range(0, 5)]
        self.multiworld.itempool += [self.create_item("CortexCar") for i in range(0, 6)]
        self.multiworld.itempool += [self.create_item("CocoCar") for i in range(0, 6)]
        self.multiworld.itempool += [self.create_item("CrunchCar") for i in range(0, 6)]
        self.multiworld.itempool += [self.create_item("PasadenaCar") for i in range(0, 6)]
        self.multiworld.itempool += [self.create_item("NinaCar") for i in range(0, 6)]
        self.multiworld.itempool += [self.create_item("NGinCar") for i in range(0, 6)]
        self.multiworld.itempool += [self.create_item("VonClutchCar") for i in range(0, 6)]
        remaining = len(self.multiworld.itempool)
        self.multiworld.itempool += [self.create_item("Crystal") for i in range(0, 87)]

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
