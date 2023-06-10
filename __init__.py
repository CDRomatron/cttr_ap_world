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

    keys = [0, 1, 2, 3]

    area_connections: typing.Dict[int, int]

    option_definitions = cttr_options

    def __init__(self, world: MultiWorld, player: int):
        super().__init__(world,player)

    def create_regions(self):
        create_regions(self.multiworld, self.player)
        #self.multiworld.clear_location_cache()

    def set_rules(self):
        self.area_connections = {}
        set_rules(self.multiworld, self.player, self.area_connections, self.keys)

    def create_item(self, name: str) -> Item:
        item_id = item_table[name]
        if False:
            classification = ItemClassification.filler
        else:
            classification = ItemClassification.progression

        item = CTTRItem(name, classification, item_id, self.player)
        return item

    def create_items(self):
        #keys
        adventurekey = self.create_item("Adventure Key")
        fairykey = self.create_item("Fairy Key")
        dinokey = self.create_item("Dino Key")
        egyptkey = self.create_item("Egypt Key")
        solarkey = self.create_item("Solar Key")
        victory = self.create_item("Victory")


        keyitems = [adventurekey, fairykey, dinokey, egyptkey]
        locations = ["MI - Gem Collection", "HEF - Gem Collection", "TW - Gem Collection", "TT - Gem Collection"]
        shuffle(self.keys)

        #self.multiworld.itempool += [adventurekey, fairykey, dinokey, egyptkey, solarkey]
        self.multiworld.get_location("Midway - Gem Collection", self.player).place_locked_item(keyitems[self.keys[0]])
        self.multiworld.get_location(locations[self.keys[0]], self.player).place_locked_item(keyitems[self.keys[1]])
        self.multiworld.get_location(locations[self.keys[1]], self.player).place_locked_item(keyitems[self.keys[2]])
        self.multiworld.get_location(locations[self.keys[2]], self.player).place_locked_item(keyitems[self.keys[3]])
        self.multiworld.get_location(locations[self.keys[3]], self.player).place_locked_item(solarkey)
        self.multiworld.get_location("AL - Ending", self.player).place_locked_item(victory)


        #skins
        cortexskin = self.create_item("Cortex Skin")
        cocoskin = self.create_item("Coco Skin")
        pasadenaskin = self.create_item("Pasadena Skin")
        crunchskin = self.create_item("Crunch Skin")
        nginskin = self.create_item("N.Gin Skin")
        ninaskin = self.create_item("Nina Skin")
        vonclutchskin = self.create_item("Von Clutch Skin")
        caveskin = self.create_item("Crash Skin (Cave)")
        classicskin = self.create_item("Crash Skin (Classic)")
        agentskin = self.create_item("Crash Skin (Agent)")
        madskin = self.create_item("Crash Skin (Mad)")
        hiphopskin = self.create_item("Crash Skin (Hiphop)")
        starskin = self.create_item("Crash Skin (Star)")
        skeletonskin = self.create_item("Crash Skin (Skeleton)")
        negaskin = self.create_item("Crash Skin (Nega)")
        nakedskin = self.create_item("Crash Skin (Naked)")

        self.multiworld.itempool += [cortexskin, cocoskin, pasadenaskin, crunchskin, nginskin, ninaskin, vonclutchskin]
        self.multiworld.itempool += [caveskin, classicskin, agentskin, madskin, hiphopskin, starskin, skeletonskin, negaskin, nakedskin]

        #tracks
        adv1 = self.create_item("Track - Tiki Turbo")
        adv2 = self.create_item("Track - Pirates of the Carburetor")
        adv3 = self.create_item("Track - Deep Sea Driving")
        fai1 = self.create_item("Track - Once Upon a Tire")
        fai2 = self.create_item("Track - Track and the Beanstalk")
        fai3 = self.create_item("Track - Evilocity")
        din1 = self.create_item("Track - Fossil Fuel Injection")
        din2 = self.create_item("Track - Labrea Car Pits")
        din3 = self.create_item("Track - Tire and Ice")
        egy1 = self.create_item("Track - Dead Heat")
        egy2 = self.create_item("Track - Crash Test Mummies")
        egy3 = self.create_item("Track - Pyramid Pass")
        sol1 = self.create_item("Track - Rings of Uranus")
        sol2 = self.create_item("Track - Uranus Mine")
        sol3 = self.create_item("Track - Craters on Uranus")

        self.multiworld.itempool += [adv1, adv2, adv3]
        self.multiworld.itempool += [fai1, fai2, fai3]
        self.multiworld.itempool += [din1, din2, din3]
        self.multiworld.itempool += [egy1, egy2, egy3]
        self.multiworld.itempool += [sol1, sol2, sol3]

        #arenas
        adva = self.create_item("Arena - Jungle Rumble")
        dina = self.create_item("Arena - Extinction Party")
        faia = self.create_item("Arena - Hardly Ever Land")
        sola = self.create_item("Arena - Space Stunts")

        self.multiworld.itempool += [adva, dina, faia, sola]

        self.multiworld.itempool += [self.create_item("Crash Car") for i in range(0, 5)]
        self.multiworld.itempool += [self.create_item("Cortex Car") for i in range(0, 6)]
        self.multiworld.itempool += [self.create_item("Coco Car") for i in range(0, 6)]
        self.multiworld.itempool += [self.create_item("Crunch Car") for i in range(0, 6)]
        self.multiworld.itempool += [self.create_item("Pasadena Car") for i in range(0, 6)]
        self.multiworld.itempool += [self.create_item("Nina Car") for i in range(0, 6)]
        self.multiworld.itempool += [self.create_item("N.Gin Car") for i in range(0, 6)]
        self.multiworld.itempool += [self.create_item("Von Clutch Car") for i in range(0, 6)]

        self.multiworld.itempool += [self.create_item("Crystal") for i in range(0, 60)]

        #dors
        self.multiworld.itempool += [self.create_item("DOR " + str(i)) for i in range(1, 35)]

        #gags
        gag1 = self.create_item("Gag Drone Cannon")
        gag2 = self.create_item("Gag Shark Zoo")
        gag3 = self.create_item("Gag Love Tester")
        gag4 = self.create_item("Gag Picture Booth")
        gag5 = self.create_item("Gag Drone Fairy")
        gag6 = self.create_item("Gag Poison Apple")
        gag7 = self.create_item("Gag Drone Dart")
        gag8 = self.create_item("Gag Ten Ton Weight")
        gag9 = self.create_item("Gag Two Drone Tele")
        gag10 = self.create_item("Gag Walrus Drone")
        gag11 = self.create_item("Gag Rocket Ship")

        self.multiworld.itempool += [gag1, gag2, gag3, gag4, gag5, gag6, gag7, gag8, gag9, gag10, gag11]

        remaining = (len(location_table) - len(self.multiworld.itempool))-5
        self.multiworld.itempool += [self.create_item("50 Coins") for i in range(0, remaining)]

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
