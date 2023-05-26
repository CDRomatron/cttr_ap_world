from BaseClasses import Item
import typing

class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    progression: bool

class CTTRItem(Item):
    game: str = "CTTR"

item_table = {
    "Crystal": ItemData(00000, False),
    "Victory": ItemData(None, True)
}

# if not listed here, then 1
item_frequencies = {
    "Crystal": 80
}

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in item_table.items() if data.code}