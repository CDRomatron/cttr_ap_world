import typing
from ...BaseClasses import Location

#this is the list of checks

class CTTRLocation(Location):
    game: str = "CTTR"

    def __init__(self, player: int, name: str, address: typing.Optional[int], parent):
        super().__init__(player, name, address, parent)
        self.event = not address


adventure_table = {
    #Mystery Island
    "Mission1",             #1000-crystal
    "Mission2",             #1000-crystal
    "Mission3",             #500-skin (cortex?)
    "Mission4",             #skin-cortex-crystal
    "Mission11",            #500-skin crashfedora
    "Mission12",            #2000-skin crashnega
    "FairyKeyCollection",
    "Adventure1",
    "Adventure2",
    "Adventure3",
    "AdventureArena",
    "AdventureSecret",
    "GagDroneCannon",
    "GagSharkZoo",
    "DOR4",
    "DOR10",
    "DOR12",
    "DOR14",
    "DOR19",
    "DOR24",
    "DOR32"
}

midway_table = {
    #Midway
    "AdventureKeyCollection",
    "DOR5",
    "DOR26",
    "DOR30",
    "DOR31",
    "GagLoveTester",
    "GagPictureBooth",
    "Mission5",             #crystal-pasadena1
    "Mission6",             #mi item-ngin1
    "Mission7",             #mi item-coco1
    "Mission8",             #2500-crunch1
    "Mission9",             #mi item-nina1
    "Mission10",            #crystal-vonc1

    "Mission15",            #t1hef item-crash2
    "Mission16",            #t1hef item-coco2
    "Mission17",            #t1hef item-pasadena2
    "Mission18",            #t1skin-ngin2
    "Mission26",            #t1skin-nina2
    "Mission27",            #t13000-crunch2
    "Mission28",            #t13000-vonc2
    "Mission29",            #t1hef item-cortex2

    "Mission33",            #t2c3-crash3
    "Mission34",            #t2c3-coco3
    "Mission35",            #t23500-crunch3
    "Mission36",            #t23500-pasadena3
    "Mission45",            #t2c3-vonc3
    "Mission46",            #t23500-nina3
    "Mission47",            #t2c3-cortex3
    "Mission48",            #t2tw item-ngin3

    "Mission59",            #t3500-crashW2
    "Mission60",            #t3500-cortexW2
    "Mission61",            #t3500-cocoW2
    "Mission62",            #t3500-crunchW2
    "Mission64",            #t3500-pasadenaW2
    "Mission65",            #t3500-nginW2
    "Mission66",            #t3500-ninaW2
    "Mission67",            #t3500-voncW2

    "Mission68",            #t2wCrystal-crashW3
    "Mission69",            #t2wCrystal-cortexW3
    "Mission70",            #t2wCrystal-cocoW3
    "Mission71",            #t2wCrystal-crunchW3
    "Mission72",            #t2wCrystal-pasadenaW3
    "Mission73",            #t2wCrystal-nginW3
    "Mission74",            #t2wCrystal-ninaW3
    "Mission75"             #t2wCrystal-voncW3
}

fairy_table = {
    #Happily Ever Faster
    "Mission13",            #1000-cocoskin
    "Mission14",            #1000-ngin skin?
    "Mission19",            #1000-crystal
    "Mission20",            #1000-crystal
    "Mission21",            #1000-crystal
    "Mission22",            #1500-crashskin-blacktie
    "DinoKeyCollection",
    "DOR6",
    "DOR11",
    "DOR13",
    "DOR29",
    "Fairy1",
    "Fairy2",
    "Fairy3",
    "FairySecret",
    "FairyArena",
    "GagDroneFairy",
    "GagPoisonApple"
}

dino_table = {
    #Tyrannosaurus Wrecks

    "DinoSecret",
    "Mission23",            #1500-crashkin-cave
    "Mission24",            #1000-crystal
    "Mission25",            #1500-nina skin?
    "Mission30",            #1000-crystal
    "Mission31",            #1000-crystal
    "Mission32",            #bear-crystal
    "EgyptKey",
    "DOR2",
    "DOR15",
    "DOR18",
    "DOR20",
    "DOR22",
    "DOR25",
    "DOR27",
    "DOR28",
    "Dino1",
    "Dino2",
    "Dino3",
    "DinoArena",
    "GagDroneDart"
}

egypt_table = {
    #Tomb Town

    "SolarKeyCollection",
    "Mission37",            #2000-skin pasadena
    "Mission38",            #2000-skin crunch
    "Mission39",            #1000-crystal
    "Mission40",            #1000-crystal
    "Mission41",            #1000-crystal
    "Mission42",            #2500-skincrash-mad
    "DOR3",
    "DOR7",
    "DOR8",
    "DOR9",
    "DOR23",
    "EgyptSecret",
    "Egypt1",
    "Egypt2",
    "Egypt3",
    "EgyptArena",
    "GagTenTonWeight"
}

solar_table = {
    #Astro Land

    "Victory",              #SolarStoryComplete
    "Mission43",            #3500-skincrash-hiphop
    "Mission44",            #2000-voncskin
    "Mission49",            #1000-crystal
    "Mission50",            #1000-crystal
    "Mission51",            #1000-crystal
    "Mission52",            #4000-skincrash-skeleton
    "Mission53",            #8000-skincrash-star
    "SolarSecret",
    "Solar1",
    "Solar2",
    "Solar3",
    "SolarArena",
    "GagTwoDroneTele",
    "GagWalrusDrone",
    "GagRockethShip",
    "DOR1",
    "DOR16",
    "DOR17",
    "DOR21",
    "DOR33",
    "DOR34",

    #All DOR

    "Naked"                 #All DOR


}

location_table = {**midway_table,**adventure_table,**fairy_table,**dino_table,**egypt_table,**solar_table}

exclusion_table = {

}

events_table = {

}

lookup_id_to_name: typing.Dict[int, str] = {id: name for name, id in location_table.items()}