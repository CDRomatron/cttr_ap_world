import typing
from BaseClasses import Location

#this is the list of checks

class CTTRLocation(Location):
    game: str = "CTTR"

    def __init__(self, player: int, name: str, address: typing.Optional[int], parent):
        super().__init__(player, name, address, parent)
        self.event = not address


gem_table = {
    "MI - Gem Collection":  123454321006,
    "HEF - Gem Collection": 123454321073,
    "TW - Gem Collection":  123454321092,
    "TT - Gem Collection":  123454321106
}

adventure_table = {
    #Mystery Island
    "MI - Worker Crystal (M1)":         123454321243,             #1000-crystal
    "MI - Worker Crystal (M2)":         123454321001,             #1000-crystal
    "MI - Cortex Skin (M3)":            123454321002,             #500-skin (cortex?)
    "MI - Crash Skin Classic (M11)":    123454321004,            #500-skin crashfedora
    "MI - Crash Skin Nega (M12)":       123454321005,            #2000-skin crashnega
    "MI - Tiki Turbo":                  123454321007,
    "MI - Pirates of the Carburetor":   123454321008,
    "MI - Deep Sea Driving":            123454321009,
    "MI - Jungle Rumble":               123454321010,
    "MI - Secret":                      123454321011,
    "MI - Gag Drone Cannon":            123454321012,
    "MI - Gag Shark Zoo":               123454321013,
    "MI - DOR4":                        123454321014,
    "MI - DOR10":                       123454321015,
    "MI - DOR12":                       123454321016,
    "MI - DOR14":                       123454321017,
    "MI - DOR19":                       123454321018,
    "MI - DOR24":                       123454321019,
    "MI - DOR32":                       123454321020
}

adventure_cortex_table = {
    #That one cortex crystal locked behind the skin
    "MI - Cortex Crystal (M4)": 123454321003  # skin-cortex-crystal
}

midway_table = {
    #Midway
    "Midway - Gem Collection":      123454321021,
    "Midway - DOR5":                123454321022,
    "Midway - DOR26":               123454321023,
"Midway - DOR30":                   123454321024,
    "Midway - DOR31":               123454321025,
    "Midway - Gag Love Tester":     123454321026,
    "Midway - Gag Picture Booth":   123454321027,
    "Midway - Pasadena 1 (M5)":     123454321028,             #crystal-pasadena1
    "Midway - Crunch 1 (M8)":       123454321031,             #2500-crunch1
    "Midway - Von Clutch 1 (M10)":  123454321033,            #crystal-vonc1
}

midway_tier1_table = {
    "Midway - Nina 1 (M9)":     123454321032,             #mi item-nina1
    "Midway - N. Gin 1 (M6)":   123454321029,             #mi item-ngin1
    "Midway - Coco 1 (M7)":     123454321030,             #mi item-coco1
}

midway_tier2_table = {
    "Midway - Crash 2 (M15)":       123454321034,            #t1hef item-crash2
    "Midway - Coco 2 (M16)":        123454321035,            #t1hef item-coco2
    "Midway - Pasadena 2 (M17)":    123454321036,            #t1hef item-pasadena2
    "Midway - N. Gin 2 (M18)":      123454321037,            #t1skin-ngin2
    "Midway - Nina 2 (M26)":        123454321038,            #t1skin-nina2
    "Midway - Crunch 2 (M27)":      123454321039,            #t13000-crunch2
    "Midway - Von Clutch 2 (M28)":  123454321040,            #t13000-vonc2
    "Midway - Cortex 2 (M29)":      123454321041,            #t1hef item-cortex2
}

midway_tier3_table = {
    "Midway - Crash 3 (M33)":       123454321042,            #t2c3-crash3
    "Midway - Coco 3 (M34)":        123454321043,            #t2c3-coco3
    "Midway - Crunch 3 (M35)":      123454321044,            #t23500-crunch3
    "Midway - Pasadena 3 (M36)":    123454321045,            #t23500-pasadena3
    "Midway - Von Clutch 3 (M45)":  123454321046,            #t2c3-vonc3
    "Midway - Nina 3 (M46)":        123454321047,            #t23500-nina3
    "Midway - Cortex 3 (M47)":      123454321048,            #t2c3-cortex3
    "Midway - N. Gin 3 (M48)":      123454321049,            #t2tw item-ngin3
}
midway_tier4_table = {
    "Midway - Crash 4 (M59)":       123454321050,            #t3500-crashW2
    "Midway - Cortex 4 (M60)":      123454321051,            #t3500-cortexW2
    "Midway - Coco 4 (M61)":        123454321052,            #t3500-cocoW2
    "Midway - Crunch 4 (M62)":      123454321053,            #t3500-crunchW2
    "Midway - Pasadena 4 (M64)":    123454321054,            #t3500-pasadenaW2
    "Midway - N. Gin 4 (M65)":      123454321055,            #t3500-nginW2
    "Midway - Nina 4 (M66)":        123454321056,            #t3500-ninaW2
    "Midway - Von Clutch 4 (M67)":  123454321057,            #t3500-voncW2
}

midway_tier5_table = {
    "Midway - Crash 5 (M68)":       123454321058,            #t2wCrystal-crashW3
    "Midway - Cortex 5 (M69)":      123454321059,            #t2wCrystal-cortexW3
    "Midway - Coco 5 (M70)":        123454321060,            #t2wCrystal-cocoW3
    "Midway - Crunch 5 (M71)":      123454321061,            #t2wCrystal-crunchW3
    "Midway - Pasadena 5 (M72)":    123454321062,            #t2wCrystal-pasadenaW3
    "Midway - N. Gin 5 (M73)":      123454321063,            #t2wCrystal-nginW3
    "Midway - Nina 5 (M74)":        123454321064,            #t2wCrystal-ninaW3
    "Midway - Von Clutch 5 (M75)":  123454321065             #t2wCrystal-voncW3
}

fairy_table = {
    #Happily Ever Faster
    "HEF - Coco Skin (M13)":            123454321066,            #1000-cocoskin
    "HEF - N. Gin Skin (M14)":          123454321067,            #1000-ngin skin?
    "HEF - Worker Crystal (M19)":       123454321068,            #1000-crystal
    "HEF - Worker Crystal (M20)":       123454321070,            #1000-crystal
    "HEF - Worker Crystal (M21)":       123454321071,            #1000-crystal
    "HEF - Crash Skin Agent (M22)":     123454321072,            #1500-crashskin-blacktie
    "HEF - DOR6":                       123454321074,
    "HEF - DOR11":                      123454321075,
    "HEF - DOR13":                      123454321076,
    "HEF - DOR29":                      123454321077,
    "HEF - Once Upon a Tire":           123454321078,
    "HEF - Track and the Beanstalk":    123454321079,
    "HEF - Evilocity":                  123454321080,
    "HEF - Secret":                     123454321081,
    "HEF - Hardly Ever Land":           123454321082,
    "HEF - Gag Drone Fairy":            123454321083,
    "HEF - Gag Poison Apple":           123454321084
}

dino_table = {
    #Tyrannosaurus Wrecks

    "TW - Secret":                  123454321085,
    "TW - Crash Skin Cave (M23)":   123454321086,            #1500-crashkin-cave
    "TW - Worker Crystal (M24)":    123454321087,            #1000-crystal
    "TW - Nina Skin (M25)":         123454321088,            #1500-nina skin?
    "TW - Worker Crystal (M30)":    123454321089,            #1000-crystal
    "TW - Worker Crystal (M31)":    123454321090,            #1000-crystal
    "TW - Crunch Crystal (M32)":    123454321091,            #bear-crystal
    "TW - DOR2":                    123454321093,
    "TW - DOR15":                   123454321094,
    "TW - DOR18":                   123454321095,
    "TW - DOR20":                   123454321096,
    "TW - DOR22":                   123454321097,
    "TW - DOR25":                   123454321098,
    "TW - DOR27":                   123454321099,
    "TW - DOR28":                   123454321100,
    "TW - Fossil Fuel Injection":   123454321101,
    "TW - Labrea Car Pits":         123454321102,
    "TW - Tire & Ice":              123454321103,
    "TW - Extinction Party":        123454321104,
    "TW - Gag Drone Dart":          123454321105
}

egypt_table = {
    #Tomb Town
    "TT - Pasadena Skin (M37)":     123454321107,            #2000-skin pasadena
    "TT - Crunch Skin (M38)":       123454321108,            #2000-skin crunch
    "TT - Worker Crystal (M39)":    123454321109,            #1000-crystal
    "TT - Worker Crystal (M40)":    123454321110,            #1000-crystal
    "TT - Worker Crystal (M41)":    123454321111,            #1000-crystal
    "TT - Crash Skin Mad (M42)":    123454321112,            #2500-skincrash-mad
    "TT - DOR3":                    123454321113,
    "TT - DOR7":                    123454321114,
    "TT - DOR8":                    123454321115,
    "TT - DOR9":                    123454321116,
    "TT - DOR23":                   123454321117,
    "TT - Secret":                  123454321118,
    "TT - Dead Heat":               123454321119,
    "TT - Crash Test Mummies":      123454321120,
    "TT - Pyramid Pass":            123454321121,
    #"EgyptArena":123454321122,
    "TT - Gag Ten Ton Weight":      123454321123
}

solar_table = {
    #Astro Land

    "AL - Ending":                      123454321124,              #SolarStoryComplete
    "Al - Crash Skin Hiphop (M43)":     123454321125,            #3500-skincrash-hiphop
    "AL - Von Clutch Skin (M44)":       123454321126,            #2000-voncskin
    "AL - Worker Crystal (M49)":        123454321127,            #1000-crystal
    "AL - Worker Crystal (M50)":        123454321128,            #1000-crystal
    "AL - Worker Crystal (M51)":        123454321129,            #1000-crystal
    "AL - Crash Skin Skeleton (M52)":   123454321130,            #4000-skincrash-skeleton
    "AL - Crash Skin Star (M53)":       123454321131,            #8000-skincrash-star
    "AL - Secret":                      123454321132,
    "AL - Rings of Uranus":             123454321133,
    "AL - Uranus' Mine":                123454321134,
    "AL - Craters on Uranus":           123454321135,
    "AL - Space Stunts":                123454321136,
    "AL - Gag Two Drone Tele":          123454321137,
    "AL - Gag Walrus Drone":            123454321138,
    "AL - Gag Rocket Ship":             123454321139,
    "AL - DOR1":                        123454321140,
    "AL - DOR16":                       123454321141,
    "AL - DOR17":                       123454321142,
    "AL - DOR21":                       123454321143,
    "AL - DOR33":                       123454321144,
    "AL - DOR34":                       123454321145
}

dor_table = {
    #All DOR

    "All DOR - Crash Skin Baby":    123454321146
}

adv1_table = {
    "Race - Tiki Turbo (A)":        123454321147,
    "Race - Tiki Turbo (B)":        123454321148,
    "Crashinator - Tiki Turbo":     123454321177,
    "Fast Lap - Tiki Turbo":        123454321192,
    "Run and Gun - Tiki Turbo":     123454321207,
    "Rolling Thunder - Tiki Turbo": 123454321222,
}

adv2_table = {
    "Race - Pirates of the Carburetor (A)":         123454321149,
    "Race - Pirates of the Carburetor (B)":         123454321150,
    "Crashinator - Pirates of the Carburetor":      123454321178,
    "Fast Lap - Pirates of the Carburetor":         123454321193,
    "Run and Gun - Pirates of the Carburetor":      123454321208,
    "Rolling Thunder - Pirates of the Carburetor":  123454321223,
}

adv3_table = {
    "Race - Deep Sea Driving (A)":          123454321151,
    "Race - Deep Sea Driving (B)":          123454321152,
    "Crashinator - Deep Sea Driving":       123454321179,
    "Fast Lap - Deep Sea Driving":          123454321194,
    "Run and Gun - Deep Sea Driving":       123454321209,
    "Rolling Thunder - Deep Sea Driving":   123454321224,
}

fai1_table = {
    "Race - Once Upon a Tire (A)":          123454321153,
    "Race - Once Upon a Tire (B)":          123454321154,
    "Crashinator - Once Upon a Tire":       123454321180,
    "Fast Lap - Once Upon a Tire":          123454321195,
    "Run and Gun - Once Upon a Tire":       123454321210,
    "Rolling Thunder - Once Upon a Tire":   123454321225,
}

fai2_table = {
    "Race - Track and the Beanstalk (A)":           123454321155,
    "Race - Track and the Beanstalk (B)":           123454321156,
    "Crashinator - Track and the Beanstalk":        123454321181,
    "Fast Lap - Track and the Beanstalk":           123454321196,
    "Run and Gun - Track and the Beanstalk":        123454321211,
    "Rolling Thunder - Track and the Beanstalk":    123454321226,
}

fai3_table = {
    "Race - Evilocity (A)":         123454321157,
    "Race - Evilocity (B)":         123454321158,
    "Crashinator - Evilocity":      123454321182,
    "Fast Lap - Evilocity":         123454321197,
    "Run and Gun - Evilocity":      123454321212,
    "Rolling Thunder - Evilocity":  123454321227,
}

din1_table = {
    "Race - Fossil Fuel Injection (A)":         123454321159,
    "Race - Fossil Fuel Injection (B)":         123454321160,
    "Crashinator - Fossil Fuel Injection":      123454321183,
    "Fast Lap - Fossil Fuel Injection":         123454321198,
    "Run and Gun - Fossil Fuel Injection":      123454321213,
    "Rolling Thunder - Fossil Fuel Injection":  123454321228,
}

din2_table = {
    "Race - Labrea Car Pits (A)":           123454321161,
    "Race - Labrea Car Pits (B)":           123454321162,
    "Crashinator - Labrea Car Pits":        123454321184,
    "Fast Lap - Labrea Car Pits":           123454321199,
    "Run and Gun - Labrea Car Pits":        123454321214,
    "Rolling Thunder - Labrea Car Pits":    123454321229,
}

din3_table = {
    "Race - Tire and Ice (A)":          123454321163,
    "Race - Tire and Ice (B)":          123454321164,
    "Crashinator - Tire and Ice":       123454321185,
    "Fast Lap - Tire and Ice":          123454321200,
    "Run and Gun - Tire and Ice":       123454321215,
    "Rolling Thunder - Tire and Ice":   123454321230,
}

egy1_table = {
    "Race - Dead Heat (A)":         123454321165,
    "Race - Dead Heat (B)":         123454321166,
    "Crashinator - Dead Heat":      123454321186,
    "Fast Lap - Dead Heat":         123454321201,
    "Run and Gun - Dead Heat":      123454321216,
    "Rolling Thunder - Dead Heat":  123454321231,
}

egy2_table = {
    "Race - Crash Test Mummies (A)":            123454321167,
    "Race - Crash Test Mummies (B)":            123454321168,
    "Crashinator - Crash Test Mummies":         123454321187,
    "Fast Lap - Crash Test Mummies":            123454321202,
    "Run and Gun - Crash Test Mummies":         123454321217,
    "Rolling Thunder - Crash Test Mummies":     123454321232,
}

egy3_table = {
    "Race - Pyramid Pass (A)":          123454321169,
    "Race - Pyramid Pass (B)":          123454321170,
    "Crashinator - Pyramid Pass":       123454321188,
    "Fast Lap - Pyramid Pass":          123454321203,
    "Run and Gun - Pyramid Pass":       123454321218,
    "Rolling Thunder - Pyramid Pass":   123454321233,
}
sol1_table = {
    "Race - Rings of Uranus (A)":           123454321171,
    "Race - Rings of Uranus (B)":           123454321172,
    "Crashinator - Rings of Uranus":        123454321189,
    "Fast Lap - Rings of Uranus":           123454321204,
    "Run and Gun - Rings of Uranus":        123454321219,
    "Rolling Thunder - Rings of Uranus":    123454321234,
}
sol2_table = {
    "Race - Uranus Mine (A)":           123454321173,
    "Race - Uranus Mine (B)":           123454321174,
    "Crashinator - Uranus Mine":        123454321190,
    "Fast Lap - Uranus Mine":           123454321205,
    "Run and Gun - Uranus Mine":        123454321220,
    "Rolling Thunder - Uranus Mine":    123454321235,
}
sol3_table = {
    "Race - Craters on Uranus (A)":         123454321175,
    "Race - Craters on Uranus (B)":         123454321176,
    "Crashinator - Craters on Uranus":      123454321191,
    "Fast Lap - Craters on Uranus":         123454321206,
    "Run and Gun - Craters on Uranus":      123454321221,
    "Rolling Thunder - Craters on Uranus":  123454321236
}

arena_table = {
    "Arena - Jungle Rumble (A)":        123454321237,
    "Arena - Jungle Rumble (B)":        123454321238,
    "Arena - Extinction Party (A)":     123454321239,
    "Arena - Extinction Party (B)":     123454321240,
    "Arena - Hardly Ever Land":         123454321241,
    "Arena - Space Stunts":             123454321242
}

location_table = {**midway_table,**adventure_table,**fairy_table,**dino_table,**egypt_table,**solar_table,
                  **midway_tier2_table,**midway_tier3_table,**midway_tier4_table,**midway_tier5_table,
                  **midway_tier1_table, **adv1_table, **adv2_table, **adv3_table, **fai1_table, **fai2_table,
                  **fai3_table, **din1_table, **din2_table, **din3_table, **egy1_table, **egy2_table, **egy3_table,
                  **sol1_table, **sol2_table, **sol3_table, **arena_table, **gem_table, **adventure_cortex_table,
                **dor_table}