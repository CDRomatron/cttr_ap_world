import typing
from ...Options import Choice, Option, Toggle, Range

cttr_options: typing.Dict[str, type(Option)] = {
    "total_crystals": Range
}