from dataclasses import dataclass

@dataclass
class PilotaGara:
    driverId: int
    forename: str
    surname: str
    position: int
    raceId: int


    def __eq__(self, other):
        if not isinstance(other, PilotaGara):
            return NotImplemented
        return self.driverId == other.driverId

    def __hash__(self):
        return hash(self.driverId)

    def __str__(self):
        return f"{self.forename} -- {self.surname}"