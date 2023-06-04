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
    "MI - Worker Crystal (M1)": 1234543210,             #1000-crystal
    "MI - Worker Crystal (M2)": 1234543211,             #1000-crystal
    "MI - Cortex Skin (M3)": 1234543212,             #500-skin (cortex?)
    "MI - Cortex Crystal (M4)": 1234543213,             #skin-cortex-crystal
    "MI - Crash Skin Classic (M11)": 1234543214,            #500-skin crashfedora
    "MI - Crash Skin Nega (M12)": 1234543215,            #2000-skin crashnega
    "MI - Gem Collection": 1234543216,
    "MI - Tiki Turbo": 1234543217,
    "MI - Pirates of the Carburetor": 1234543218,
    "MI - Deep See Driving": 1234543219,
    "MI - Jungle Rumble": 12345432110,
    "MI - Secret": 12345432111,
    "MI - Gag Drone Cannon": 12345432112,
    "MI - Gag Shark Zoo": 12345432113,
    "MI - DOR4": 12345432114,
    "MI - DOR10": 12345432115,
    "MI - DOR12": 12345432116,
    "MI - DOR14": 12345432117,
    "MI - DOR19": 12345432118,
    "MI - DOR24": 12345432119,
    "MI - DOR32": 12345432120
}

midway_table = {
    #Midway
    "Midway - Gem Collection":12345432121,
    "Midway - DOR5":12345432122,
    "Midway - DOR26":12345432123,
    "Midway - DOR30":12345432124,
    "Midway - DOR31":12345432125,
    "Midway - Gag Love Tester":12345432126,
    "Midway - Gag Picture Booth":12345432127,
    "Midway - Pasadena 1 (M5)":12345432128,             #crystal-pasadena1
    "Midway - Crunch 1 (M8)":12345432131,             #2500-crunch1
    "Midway - Von Clutch 1 (M10)":12345432133,            #crystal-vonc1
}

midway_tier1_table = {
    "Midway - Nina 1 (M9)":12345432132,             #mi item-nina1
    "Midway - N.Gin 1 (M6)":12345432129,             #mi item-ngin1
    "Midway - Coco 1 (M7)":12345432130,             #mi item-coco1
}

midway_tier2_table = {
    "Midway - Crash 2 (M15)":12345432134,            #t1hef item-crash2
    "Midway - Coco 2 (M16)":12345432135,            #t1hef item-coco2
    "Midway - Pasadena 2 (M17)":12345432136,            #t1hef item-pasadena2
    "Midway - N. Gin 2 (M18)":12345432137,            #t1skin-ngin2
    "Midway - Nina 2 (M26)":12345432138,            #t1skin-nina2
    "Midway - Crunch 2 (M27)":12345432139,            #t13000-crunch2
    "Midway - Von Clutch 2 (M28)":12345432140,            #t13000-vonc2
    "Midway - Cortex 2 (M29)":12345432141,            #t1hef item-cortex2
}

midway_tier3_table = {
    "Midway - Crash 3 (M33)":12345432142,            #t2c3-crash3
    "Midway - Coco 3 (M34)":12345432143,            #t2c3-coco3
    "Midway - Crunch 3 (M35)":12345432144,            #t23500-crunch3
    "Midway - Pasadena 3 (M36)":12345432145,            #t23500-pasadena3
    "Midway - Von Clutch 3 (M45)":12345432146,            #t2c3-vonc3
    "Midway - Nina 3 (M46)":12345432147,            #t23500-nina3
    "Midway - Cortex 3 (M47)":12345432148,            #t2c3-cortex3
    "Midway - N. Gin 3 (M48)":12345432149,            #t2tw item-ngin3
}
midway_tier4_table = {
    "Midway - Crash 4 (M59)":12345432150,            #t3500-crashW2
    "Midway - Cortex 4 (M60)":12345432151,            #t3500-cortexW2
    "Midway - Coco 4 (M61)":12345432152,            #t3500-cocoW2
    "Midway - Crunch 4 (M62)":12345432153,            #t3500-crunchW2
    "Midway - Pasadena 4 (M64)":12345432154,            #t3500-pasadenaW2
    "Midway - N. Gin 4 (M65)":12345432155,            #t3500-nginW2
    "Midway - Nina 4 (M66)":12345432156,            #t3500-ninaW2
    "Midway - Von Clutch 4 (M67)":12345432157,            #t3500-voncW2
}

midway_tier5_table = {
    "Midway - Crash 5 (M68)":12345432158,            #t2wCrystal-crashW3
    "Midway - Cortex 5 (M69)":12345432159,            #t2wCrystal-cortexW3
    "Midway - Coco 5 (M70)":12345432160,            #t2wCrystal-cocoW3
    "Midway - Crunch 5 (M71)":12345432161,            #t2wCrystal-crunchW3
    "Midway - Pasadena 5 (M72)":12345432162,            #t2wCrystal-pasadenaW3
    "Midway - N. Gin 5 (M73)":12345432163,            #t2wCrystal-nginW3
    "Midway - Nina 5 (M74)":12345432164,            #t2wCrystal-ninaW3
    "Midway - Von Clutch 5 (M75)":12345432165             #t2wCrystal-voncW3
}

fairy_table = {
    #Happily Ever Faster
    "HEF - Coco Skin (M13)":12345432166,            #1000-cocoskin
    "HEF - N. Gin Skin (M14)":12345432167,            #1000-ngin skin?
    "HEF - Worker Crystal (M19)":12345432168,            #1000-crystal
    "HEF - Worker Crystal (M20)":12345432170,            #1000-crystal
    "HEF - Worker Crystal (M21)":12345432171,            #1000-crystal
    "HEF - Crash Skin Agent (M22)":12345432172,            #1500-crashskin-blacktie
    "HEF - Gem Collection":12345432173,
    "HEF - DOR6":12345432174,
    "HEF - DOR11":12345432175,
    "HEF - DOR13":12345432176,
    "HEF - DOR29":12345432177,
    "HEF - Once Upon a Tire":12345432178,
    "HEF - Track and the Beanstalk":12345432179,
    "HEF - Evilocity":12345432180,
    "HEF - Secret":12345432181,
    "HEF - Hardly Ever Land":12345432182,
    "HEF - Gag Drone Fairy":12345432183,
    "HEF - Gag Poison Apple":12345432184
}

dino_table = {
    #Tyrannosaurus Wrecks

    "TW - Secret":12345432185,
    "TW - Crash Skin Cave (M23)":12345432186,            #1500-crashkin-cave
    "TW - Worker Crystal (M24)":12345432187,            #1000-crystal
    "TW - Nina Skin (M25)":12345432188,            #1500-nina skin?
    "TW - Worker Crystal (M30)":12345432189,            #1000-crystal
    "TW - Worker Crystal (M31)":12345432190,            #1000-crystal
    "TW - Crunch Crystal (M32)":12345432191,            #bear-crystal
    "TW - Gem Collection":12345432192,
    "TW - DOR2":12345432193,
    "TW - DOR15":12345432194,
    "TW - DOR18":12345432195,
    "TW - DOR20":12345432196,
    "TW - DOR22":12345432197,
    "TW - DOR25":12345432198,
    "TW - DOR27":12345432199,
    "TW - DOR28":123454321100,
    "TW - Fossil Fuel Injection":123454321101,
    "TW - Labrea Car Pits":123454321102,
    "TW - Tire & Ice":123454321103,
    "TW - Extinction Party":123454321104,
    "TW - Gag Drone Dart":123454321105
}

egypt_table = {
    #Tomb Town

    "TT - Gem Collection":123454321106,
    "TT - Pasadena Skin (M37)":123454321107,            #2000-skin pasadena
    "TT - Crunch Skin (M38)":123454321108,            #2000-skin crunch
    "TT - Worker Crystal (M39)":123454321109,            #1000-crystal
    "TT - Worker Crystal (M40)":123454321110,            #1000-crystal
    "TT - Worker Crystal (M41)":123454321111,            #1000-crystal
    "TT - Crash Skin Mad (M42)":123454321112,            #2500-skincrash-mad
    "TT - DOR3":123454321113,
    "TT - DOR7":123454321114,
    "TT - DOR8":123454321115,
    "TT - DOR9":123454321116,
    "TT - DOR23":123454321117,
    "TT - Secret":123454321118,
    "TT - Dead Heat":123454321119,
    "TT - Crash Test Mummies":123454321120,
    "TT - Pyramid Pass":123454321121,
    #"EgyptArena":123454321122,
    "TT - Gag Ten Ton Weight":123454321123
}

solar_table = {
    #Astro Land

    "AL - Ending":123454321124,              #SolarStoryComplete
    "Al - Crash Skin Hiphop (M43)":123454321125,            #3500-skincrash-hiphop
    "AL - Von Clutch Skin (M44)":123454321126,            #2000-voncskin
    "AL - Worker Crystal (M49)":123454321127,            #1000-crystal
    "AL - Worker Crystal (M50)":123454321128,            #1000-crystal
    "AL - Worker Crystal (M51)":123454321129,            #1000-crystal
    "AL - Crash Skin Skeleton (M52)":123454321130,            #4000-skincrash-skeleton
    "AL - Crash Skin Star (M53)":123454321131,            #8000-skincrash-star
    "AL - Secret":123454321132,
    "AL - Rings of Uranus":123454321133,
    "AL - Uranus' Mine":123454321134,
    "AL - Craters on Uranus":123454321135,
    "AL - Space Stunts":123454321136,
    "AL - Gag Two Drone Tele":123454321137,
    "AL - Gag Walrus Drone":123454321138,
    "AL - Gag Rocket Ship":123454321139,
    "AL - DOR1":123454321140,
    "AL - DOR16":123454321141,
    "AL - DOR17":123454321142,
    "AL - DOR21":123454321143,
    "AL - DOR33":123454321144,
    "AL - DOR34":123454321145,

    #All DOR

    "All DOR - Crash Skin Baby":123454321146                 #All DOR


}

location_table = {**midway_table,**adventure_table,**fairy_table,**dino_table,**egypt_table,**solar_table,
                  **midway_tier2_table,**midway_tier3_table,**midway_tier4_table,**midway_tier5_table,
                  **midway_tier1_table}