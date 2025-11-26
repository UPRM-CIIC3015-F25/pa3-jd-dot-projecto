class PlanetCard:
    def __init__(self, name, description, price=6, chips=0, mult=0, image=None, isActive=False):
        self.name = name
        self.description = description
        self.price = price
        self.chips = chips
        self.mult = mult
        self.image = image
        self.isActive = isActive

    def __str__(self):
        return f"{self.name}: {self.description}"

    def sellPrice(self):
        return int(self.price * 0.6)

# TODO (TASK 6.1): Implement the Planet Card system for Balatro.
#   Create a dictionary called PLANETS that stores all available PlanetCard objects.
#   Each entry should use the planet's name as the key and a PlanetCard instance as the value.
#   Each PlanetCard must include:
#       - name: the planet's name (e.g., "Mars")
#       - description: the hand it levels up or affects
#       - price: how much it costs to purchase
#       - chips: the chip bonus it provides
#       - mult: the multiplier it applies
#   Example structure:
#       "Gusty Garden": PlanetCard("Gusty Garden", "levels up galaxy", 6, 15, 7)
#   Include all planets up to "Sun" to complete the set.
#   These cards will be used in the shop and gameplay systems to upgrade specific poker hands.

PLANETS = {
    "Mercury": PlanetCard("Mercury", "boosts One Pair hands", price=5, chips=5, mult=1.2),
    "Venus": PlanetCard("Venus", "enhances Two Pair hands", price=6, chips=8, mult=1.3),
    "Earth": PlanetCard("Earth", "strengthens Three of a Kind hands", price=7, chips=10, mult=1.4),
    "Mars": PlanetCard("Mars", "improves Straight hands", price=8, chips=12, mult=1.5),
    "Jupiter": PlanetCard("Jupiter", "amplifies Flush hands", price=9, chips=15, mult=1.6),
    "Saturn": PlanetCard("Saturn", "boosts Full House hands", price=10, chips=18, mult=1.7),
    "Uranus": PlanetCard("Uranus", "enhances Four of a Kind hands", price=11, chips=20, mult=1.8),
    "Neptune": PlanetCard("Neptune", "strengthens Straight Flush hands", price=12, chips=25, mult=2.0),
    "Pluto": PlanetCard("Pluto", "mysterious power for any hand", price=13, chips=30, mult=2.2),
    "Sun": PlanetCard("Sun", "ultimate boost for the entire hand", price=15, chips=40, mult=2.5)
}
