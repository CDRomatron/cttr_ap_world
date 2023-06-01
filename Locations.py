import typing
from BaseClasses import Location

#this is the list of checks

class CTTRLocation(Location):
    game: str = "CTTR"

    def __init__(self, player: int, name: str, address: typing.Optional[int], parent):
        super().__init__(player, name, address, parent)
        self.event = not address


adventure_table = {
    #Mystery Island
    "Mission1":0,             #1000-crystal
    "Mission2":1,             #1000-crystal
    "Mission3":2,             #500-skin (cortex?)
    "Mission4":3,             #skin-cortex-crystal
    "Mission11":4,            #500-skin crashfedora
    "Mission12":5,            #2000-skin crashnega
    "FairyKeyCollection":6,
    "Adventure1":7,
    "Adventure2":8,
    "Adventure3":9,
    "AdventureArena":10,
    "AdventureSecret":11,
    "GagDroneCannon":12,
    "GagSharkZoo":13,
    "DOR4":14,
    "DOR10":15,
    "DOR12":16,
    "DOR14":17,
    "DOR19":18,
    "DOR24":19,
    "DOR32":20
}

midway_table = {
    #Midway
    "AdventureKeyCollection":21,
    "DOR5":22,
    "DOR26":23,
    "DOR30":24,
    "DOR31":25,
    "GagLoveTester":26,
    "GagPictureBooth":27,
    "Mission5":28,             #crystal-pasadena1
    "Mission6":29,             #mi item-ngin1
    "Mission7":30,             #mi item-coco1
    "Mission8":31,             #2500-crunch1
    "Mission9":32,             #mi item-nina1
    "Mission10":33,            #crystal-vonc1

    "Mission15":34,            #t1hef item-crash2
    "Mission16":35,            #t1hef item-coco2
    "Mission17":36,            #t1hef item-pasadena2
    "Mission18":37,            #t1skin-ngin2
    "Mission26":38,            #t1skin-nina2
    "Mission27":39,            #t13000-crunch2
    "Mission28":40,            #t13000-vonc2
    "Mission29":41,            #t1hef item-cortex2

    "Mission33":42,            #t2c3-crash3
    "Mission34":43,            #t2c3-coco3
    "Mission35":44,            #t23500-crunch3
    "Mission36":45,            #t23500-pasadena3
    "Mission45":46,            #t2c3-vonc3
    "Mission46":47,            #t23500-nina3
    "Mission47":48,            #t2c3-cortex3
    "Mission48":49,            #t2tw item-ngin3

    "Mission59":50,            #t3500-crashW2
    "Mission60":51,            #t3500-cortexW2
    "Mission61":52,            #t3500-cocoW2
    "Mission62":53,            #t3500-crunchW2
    "Mission64":54,            #t3500-pasadenaW2
    "Mission65":55,            #t3500-nginW2
    "Mission66":56,            #t3500-ninaW2
    "Mission67":57,            #t3500-voncW2

    "Mission68":58,            #t2wCrystal-crashW3
    "Mission69":59,            #t2wCrystal-cortexW3
    "Mission70":60,            #t2wCrystal-cocoW3
    "Mission71":61,            #t2wCrystal-crunchW3
    "Mission72":62,            #t2wCrystal-pasadenaW3
    "Mission73":63,            #t2wCrystal-nginW3
    "Mission74":64,            #t2wCrystal-ninaW3
    "Mission75":65             #t2wCrystal-voncW3
}

fairy_table = {
    #Happily Ever Faster
    "Mission13":66,            #1000-cocoskin
    "Mission14":67,            #1000-ngin skin?
    "Mission19":68,            #1000-crystal
    "Mission20":70,            #1000-crystal
    "Mission21":71,            #1000-crystal
    "Mission22":72,            #1500-crashskin-blacktie
    "DinoKeyCollection":73,
    "DOR6":74,
    "DOR11":75,
    "DOR13":76,
    "DOR29":77,
    "Fairy1":78,
    "Fairy2":79,
    "Fairy3":80,
    "FairySecret":81,
    "FairyArena":82,
    "GagDroneFairy":83,
    "GagPoisonApple":84
}

dino_table = {
    #Tyrannosaurus Wrecks

    "DinoSecret":85,
    "Mission23":86,            #1500-crashkin-cave
    "Mission24":87,            #1000-crystal
    "Mission25":88,            #1500-nina skin?
    "Mission30":89,            #1000-crystal
    "Mission31":90,            #1000-crystal
    "Mission32":91,            #bear-crystal
    "EgyptKey":92,
    "DOR2":93,
    "DOR15":94,
    "DOR18":95,
    "DOR20":96,
    "DOR22":97,
    "DOR25":98,
    "DOR27":99,
    "DOR28":100,
    "Dino1":101,
    "Dino2":102,
    "Dino3":103,
    "DinoArena":104,
    "GagDroneDart":105
}

egypt_table = {
    #Tomb Town

    "SolarKeyCollection":106,
    "Mission37":107,            #2000-skin pasadena
    "Mission38":108,            #2000-skin crunch
    "Mission39":109,            #1000-crystal
    "Mission40":110,            #1000-crystal
    "Mission41":111,            #1000-crystal
    "Mission42":112,            #2500-skincrash-mad
    "DOR3":113,
    "DOR7":114,
    "DOR8":115,
    "DOR9":116,
    "DOR23":117,
    "EgyptSecret":118,
    "Egypt1":119,
    "Egypt2":120,
    "Egypt3":121,
    "EgyptArena":122,
    "GagTenTonWeight":123
}

solar_table = {
    #Astro Land

    "Victory":124,              #SolarStoryComplete
    "Mission43":125,            #3500-skincrash-hiphop
    "Mission44":126,            #2000-voncskin
    "Mission49":127,            #1000-crystal
    "Mission50":128,            #1000-crystal
    "Mission51":129,            #1000-crystal
    "Mission52":130,            #4000-skincrash-skeleton
    "Mission53":131,            #8000-skincrash-star
    "SolarSecret":132,
    "Solar1":133,
    "Solar2":134,
    "Solar3":135,
    "SolarArena":136,
    "GagTwoDroneTele":137,
    "GagWalrusDrone":138,
    "GagRockethShip":139,
    "DOR1":140,
    "DOR16":141,
    "DOR17":142,
    "DOR21":143,
    "DOR33":144,
    "DOR34":145,

    #All DOR

    "Naked":146                 #All DOR


}

location_table = {**midway_table,**adventure_table,**fairy_table,**dino_table,**egypt_table,**solar_table}