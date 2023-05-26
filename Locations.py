import typing
from BaseClasses import Location

class CTTRLocation(Location):
    game: str = "CTTR"

    def __init__(self, player: int, name: str, address: typing.Optional[int], parent):
        super().__init__(player, name, address, parent)
        self.event = not address


location_table = {
    #Midway
    #Mystery Island
    "HUB2ParkWorker": 0
    #Happily Ever Faster
    #Tyrannosaurus Wrecks
    #Tomb Town
    #Astro Land
    
}

exclusion_table = {

}

events_table = {

}

lookup_id_to_name: typing.Dict[int, str] = {id: name for name, id in location_table.items()}