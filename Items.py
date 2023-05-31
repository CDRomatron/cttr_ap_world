from ...BaseClasses import Item
import typing

class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    progression: bool

class CTTRItem(Item):
    game: str = "CTTR"

item_table = {
    "Victory": ItemData(1, True),
    "Crystal": ItemData(2, False),
    "CrashCar": ItemData(3, False),
    "CortexCar": ItemData(4, False),
    "CocoCar": ItemData(5, False),
    "PasadenaCar": ItemData(6, False),
    "NinaCar": ItemData(7, False),
    "NGinCar": ItemData(8, False),
    "CrunchCar": ItemData(9, False),
    "VonClutchCar": ItemData(10, False),
    "AdventureKey": ItemData(11, True),
    "FairyKey": ItemData(12, True),
    "DinoKey": ItemData(13, True),
    "EgyptKey": ItemData(14, True),
    "SolarKey": ItemData(15, True),

}

# if not listed here, then 1
item_frequencies = {
}

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in item_table.items() if data.code}