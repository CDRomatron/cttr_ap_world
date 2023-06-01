from BaseClasses import Item
import typing

class CTTRItem(Item):
    game: str = "CTTR"

item_table = {
    "Victory": 1,
    "Crystal": 2,
    "CrashCar": 3,
    "CortexCar": 4,
    "CocoCar": 5,
    "PasadenaCar": 6,
    "NinaCar": 7,
    "NGinCar": 8,
    "CrunchCar": 9,
    "VonClutchCar": 10,
    "AdventureKey": 11,
    "FairyKey": 12,
    "DinoKey": 13,
    "EgyptKey": 14,
    "SolarKey": 15

}

# if not listed here, then 1
item_frequencies = {
}

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in item_table.items() if data.code}