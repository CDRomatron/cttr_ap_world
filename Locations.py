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
    "Mission1":1234543210,             #1000-crystal
    "Mission2":1234543211,             #1000-crystal
    "Mission3":1234543212,             #500-skin (cortex?)
    "Mission4":1234543213,             #skin-cortex-crystal
    "Mission11":1234543214,            #500-skin crashfedora
    "Mission12":1234543215,            #2000-skin crashnega
    "FairyKeyCollection":1234543216,
    "Adventure1":1234543217,
    "Adventure2":1234543218,
    "Adventure3":1234543219,
    "AdventureArena":12345432110,
    "AdventureSecret":12345432111,
    "GagDroneCannon":12345432112,
    "GagSharkZoo":12345432113,
    "DOR4":12345432114,
    "DOR10":12345432115,
    "DOR12":12345432116,
    "DOR14":12345432117,
    "DOR19":12345432118,
    "DOR24":12345432119,
    "DOR32":12345432120
}

midway_table = {
    #Midway
    "AdventureKeyCollection":12345432121,
    "DOR5":12345432122,
    "DOR26":12345432123,
    "DOR30":12345432124,
    "DOR31":12345432125,
    "GagLoveTester":12345432126,
    "GagPictureBooth":12345432127,
    "Mission5":12345432128,             #crystal-pasadena1
    "Mission6":12345432129,             #mi item-ngin1
    "Mission7":12345432130,             #mi item-coco1
    "Mission8":12345432131,             #2500-crunch1
    "Mission9":12345432132,             #mi item-nina1
    "Mission10":12345432133,            #crystal-vonc1

    "Mission15":12345432134,            #t1hef item-crash2
    "Mission16":12345432135,            #t1hef item-coco2
    "Mission17":12345432136,            #t1hef item-pasadena2
    "Mission18":12345432137,            #t1skin-ngin2
    "Mission26":12345432138,            #t1skin-nina2
    "Mission27":12345432139,            #t13000-crunch2
    "Mission28":12345432140,            #t13000-vonc2
    "Mission29":12345432141,            #t1hef item-cortex2

    "Mission33":12345432142,            #t2c3-crash3
    "Mission34":12345432143,            #t2c3-coco3
    "Mission35":12345432144,            #t23500-crunch3
    "Mission36":12345432145,            #t23500-pasadena3
    "Mission45":12345432146,            #t2c3-vonc3
    "Mission46":12345432147,            #t23500-nina3
    "Mission47":12345432148,            #t2c3-cortex3
    "Mission48":12345432149,            #t2tw item-ngin3

    "Mission59":12345432150,            #t3500-crashW2
    "Mission60":12345432151,            #t3500-cortexW2
    "Mission61":12345432152,            #t3500-cocoW2
    "Mission62":12345432153,            #t3500-crunchW2
    "Mission64":12345432154,            #t3500-pasadenaW2
    "Mission65":12345432155,            #t3500-nginW2
    "Mission66":12345432156,            #t3500-ninaW2
    "Mission67":12345432157,            #t3500-voncW2

    "Mission68":12345432158,            #t2wCrystal-crashW3
    "Mission69":12345432159,            #t2wCrystal-cortexW3
    "Mission70":12345432160,            #t2wCrystal-cocoW3
    "Mission71":12345432161,            #t2wCrystal-crunchW3
    "Mission72":12345432162,            #t2wCrystal-pasadenaW3
    "Mission73":12345432163,            #t2wCrystal-nginW3
    "Mission74":12345432164,            #t2wCrystal-ninaW3
    "Mission75":12345432165             #t2wCrystal-voncW3
}

fairy_table = {
    #Happily Ever Faster
    "Mission13":12345432166,            #1000-cocoskin
    "Mission14":12345432167,            #1000-ngin skin?
    "Mission19":12345432168,            #1000-crystal
    "Mission20":12345432170,            #1000-crystal
    "Mission21":12345432171,            #1000-crystal
    "Mission22":12345432172,            #1500-crashskin-blacktie
    "DinoKeyCollection":12345432173,
    "DOR6":12345432174,
    "DOR11":12345432175,
    "DOR13":12345432176,
    "DOR29":12345432177,
    "Fairy1":12345432178,
    "Fairy2":12345432179,
    "Fairy3":12345432180,
    "FairySecret":12345432181,
    "FairyArena":12345432182,
    "GagDroneFairy":12345432183,
    "GagPoisonApple":12345432184
}

dino_table = {
    #Tyrannosaurus Wrecks

    "DinoSecret":12345432185,
    "Mission23":12345432186,            #1500-crashkin-cave
    "Mission24":12345432187,            #1000-crystal
    "Mission25":12345432188,            #1500-nina skin?
    "Mission30":12345432189,            #1000-crystal
    "Mission31":12345432190,            #1000-crystal
    "Mission32":12345432191,            #bear-crystal
    "EgyptKey":12345432192,
    "DOR2":12345432193,
    "DOR15":12345432194,
    "DOR18":12345432195,
    "DOR20":12345432196,
    "DOR22":12345432197,
    "DOR25":12345432198,
    "DOR27":12345432199,
    "DOR28":123454321100,
    "Dino1":123454321101,
    "Dino2":123454321102,
    "Dino3":123454321103,
    "DinoArena":123454321104,
    "GagDroneDart":123454321105
}

egypt_table = {
    #Tomb Town

    "SolarKeyCollection":123454321106,
    "Mission37":123454321107,            #2000-skin pasadena
    "Mission38":123454321108,            #2000-skin crunch
    "Mission39":123454321109,            #1000-crystal
    "Mission40":123454321110,            #1000-crystal
    "Mission41":123454321111,            #1000-crystal
    "Mission42":123454321112,            #2500-skincrash-mad
    "DOR3":123454321113,
    "DOR7":123454321114,
    "DOR8":123454321115,
    "DOR9":123454321116,
    "DOR23":123454321117,
    "EgyptSecret":123454321118,
    "Egypt1":123454321119,
    "Egypt2":123454321120,
    "Egypt3":123454321121,
    "EgyptArena":123454321122,
    "GagTenTonWeight":123454321123
}

solar_table = {
    #Astro Land

    "Victory":123454321124,              #SolarStoryComplete
    "Mission43":123454321125,            #3500-skincrash-hiphop
    "Mission44":123454321126,            #2000-voncskin
    "Mission49":123454321127,            #1000-crystal
    "Mission50":123454321128,            #1000-crystal
    "Mission51":123454321129,            #1000-crystal
    "Mission52":123454321130,            #4000-skincrash-skeleton
    "Mission53":123454321131,            #8000-skincrash-star
    "SolarSecret":123454321132,
    "Solar1":123454321133,
    "Solar2":123454321134,
    "Solar3":123454321135,
    "SolarArena":123454321136,
    "GagTwoDroneTele":123454321137,
    "GagWalrusDrone":123454321138,
    "GagRockethShip":123454321139,
    "DOR1":123454321140,
    "DOR16":123454321141,
    "DOR17":123454321142,
    "DOR21":123454321143,
    "DOR33":123454321144,
    "DOR34":123454321145,

    #All DOR

    "Naked":123454321146                 #All DOR


}

location_table = {**midway_table,**adventure_table,**fairy_table,**dino_table,**egypt_table,**solar_table}