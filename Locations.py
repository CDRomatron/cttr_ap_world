import typing
from BaseClasses import Location

#this is the list of checks

class CTTRLocation(Location):
    game: str = "CTTR"

    def __init__(self, player: int, name: str, address: typing.Optional[int], parent):
        super().__init__(player, name, address, parent)
        self.event = not address


gem_table = {
    "MI - Gem Collection": 1234543216,
    "HEF - Gem Collection": 12345432173,
    "TW - Gem Collection": 12345432192,
    "TT - Gem Collection": 123454321106
}

adventure_table = {
    #Mystery Island
    "MI - Worker Crystal (M1)": 1234543210,             #1000-crystal
    "MI - Worker Crystal (M2)": 1234543211,             #1000-crystal
    "MI - Cortex Skin (M3)": 1234543212,             #500-skin (cortex?)
    "MI - Cortex Crystal (M4)": 1234543213,             #skin-cortex-crystal
    "MI - Crash Skin Classic (M11)": 1234543214,            #500-skin crashfedora
    "MI - Crash Skin Nega (M12)": 1234543215,            #2000-skin crashnega
    "MI - Tiki Turbo": 1234543217,
    "MI - Pirates of the Carburetor": 1234543218,
    "MI - Deep Sea Driving": 1234543219,
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
    "Midway - N. Gin 1 (M6)":12345432129,             #mi item-ngin1
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

adv1_table = {
    "Race - Tiki Turbo (A)":123454321147,
    "Race - Tiki Turbo (B)":123454321148,
    "Crashinator - Tiki Turbo":123454321177,
    "Fast Lap - Tiki Turbo":123454321192,
    "Run and Gun - Tiki Turbo": 123454321207,
    "Rolling Thunder - Tiki Turbo": 123454321222,
}

adv2_table = {
    "Race - Pirates of the Carburetor (A)":123454321149,
    "Race - Pirates of the Carburetor (B)":123454321150,
    "Crashinator - Pirates of the Carburetor": 123454321178,
    "Fast Lap - Pirates of the Carburetor": 123454321193,
    "Run and Gun - Pirates of the Carburetor": 123454321208,
    "Rolling Thunder - Pirates of the Carburetor": 123454321223,
}

adv3_table = {
    "Race - Deep Sea Driving (A)": 123454321151,
    "Race - Deep Sea Driving (B)": 123454321152,
    "Crashinator - Deep Sea Driving": 123454321179,
    "Fast Lap - Deep Sea Driving": 123454321194,
    "Run and Gun - Deep Sea Driving": 123454321209,
    "Rolling Thunder - Deep Sea Driving": 123454321224,
}

fai1_table = {
    "Race - Once Upon a Tire (A)": 123454321153,
    "Race - Once Upon a Tire (B)": 123454321154,
    "Crashinator - Once Upon a Tire": 123454321180,
    "Fast Lap - Once Upon a Tire": 123454321195,
    "Run and Gun - Once Upon a Tire": 123454321210,
    "Rolling Thunder - Once Upon a Tire": 123454321225,
}

fai2_table = {
    "Race - Track and the Beanstalk (A)": 123454321155,
    "Race - Track and the Beanstalk (B)": 123454321156,
    "Crashinator - Track and the Beanstalk": 123454321181,
    "Fast Lap - Track and the Beanstalk": 123454321196,
    "Run and Gun - Track and the Beanstalk": 123454321211,
    "Rolling Thunder - Track and the Beanstalk": 123454321226,
}

fai3_table = {
    "Race - Evilocity (A)": 123454321157,
    "Race - Evilocity (B)": 123454321158,
    "Crashinator - Evilocity": 123454321182,
    "Fast Lap - Evilocity": 123454321197,
    "Run and Gun - Evilocity": 123454321212,
    "Rolling Thunder - Evilocity": 123454321227,
}

din1_table = {
    "Race - Fossil Fuel Injection (A)": 123454321159,
    "Race - Fossil Fuel Injection (B)": 123454321160,
    "Crashinator - Fossil Fuel Injection": 123454321183,
    "Fast Lap - Fossil Fuel Injection": 123454321198,
    "Run and Gun - Fossil Fuel Injection": 123454321213,
    "Rolling Thunder - Fossil Fuel Injection": 123454321228,
}

din2_table = {
    "Race - Labrea Car Pits (A)": 123454321161,
    "Race - Labrea Car Pits (B)": 123454321162,
    "Crashinator - Labrea Car Pits": 123454321184,
    "Fast Lap - Labrea Car Pits": 123454321199,
    "Run and Gun - Labrea Car Pits": 123454321214,
    "Rolling Thunder - Labrea Car Pits": 123454321229,
}

din3_table = {
    "Race - Tire and Ice (A)": 123454321163,
    "Race - Tire and Ice (B)": 123454321164,
    "Crashinator - Tire and Ice": 123454321185,
    "Fast Lap - Tire and Ice": 123454321200,
    "Run and Gun - Tire and Ice": 123454321215,
    "Rolling Thunder - Tire and Ice": 123454321230,
}

egy1_table = {
    "Race - Dead Heat (A)": 123454321165,
    "Race - Dead Heat (B)": 123454321166,
    "Crashinator - Dead Heat": 123454321186,
    "Fast Lap - Dead Heat": 123454321201,
    "Run and Gun - Dead Heat": 123454321216,
    "Rolling Thunder - Dead Heat": 123454321231,
}

egy2_table = {
    "Race - Crash Test Mummies (A)": 123454321167,
    "Race - Crash Test Mummies (B)": 123454321168,
    "Crashinator - Crash Test Mummies": 123454321187,
    "Fast Lap - Crash Test Mummies": 123454321202,
    "Run and Gun - Crash Test Mummies": 123454321217,
    "Rolling Thunder - Crash Test Mummies": 123454321232,
}

egy3_table = {
    "Race - Pyramid Pass (A)": 123454321169,
    "Race - Pyramid Pass (B)": 123454321170,
    "Crashinator - Pyramid Pass": 123454321188,
    "Fast Lap - Pyramid Pass": 123454321203,
    "Run and Gun - Pyramid Pass": 123454321218,
    "Rolling Thunder - Pyramid Pass": 123454321233,
}
sol1_table = {
    "Race - Rings of Uranus (A)": 123454321171,
    "Race - Rings of Uranus (B)": 123454321172,
    "Crashinator - Rings of Uranus": 123454321189,
    "Fast Lap - Rings of Uranus": 123454321204,
    "Run and Gun - Rings of Uranus": 123454321219,
    "Rolling Thunder - Rings of Uranus": 123454321234,
}
sol2_table = {
    "Race - Uranus Mine (A)": 123454321173,
    "Race - Uranus Mine (B)": 123454321174,
    "Crashinator - Uranus Mine": 123454321190,
    "Fast Lap - Uranus Mine": 123454321205,
    "Run and Gun - Uranus Mine": 123454321220,
    "Rolling Thunder - Uranus Mine": 123454321235,
}
sol3_table = {
    "Race - Craters on Uranus (A)": 123454321175,
    "Race - Craters on Uranus (B)": 123454321176,
    "Crashinator - Craters on Uranus": 123454321191,
    "Fast Lap - Craters on Uranus": 123454321206,
    "Run and Gun - Craters on Uranus": 123454321221,
    "Rolling Thunder - Craters on Uranus": 123454321236
}

arena_table = {
    "Arena - Jungle Rumble (A)": 123454321237,
    "Arena - Jungle Rumble (B)": 123454321238,
    "Arena - Extinction Party (A)": 123454321239,
    "Arena - Extinction Party (B)": 123454321240,
    "Arena - Hardly Ever Land": 123454321241,
    "Arena - Space Stunts": 123454321242
}

location_table = {**midway_table,**adventure_table,**fairy_table,**dino_table,**egypt_table,**solar_table,
                  **midway_tier2_table,**midway_tier3_table,**midway_tier4_table,**midway_tier5_table,
                  **midway_tier1_table, **adv1_table, **adv2_table, **adv3_table, **fai1_table, **fai2_table,
                  **fai3_table, **din1_table, **din2_table, **din3_table, **egy1_table, **egy2_table, **egy3_table,
                  **sol1_table, **sol2_table, **sol3_table, **arena_table, **gem_table}