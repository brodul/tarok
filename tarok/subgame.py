class SubGame():
    """Defines atributes and methods that are common in sub games"""

    # player who plays the subgame
    def __init__(self, player, talon):
        self.player = player
        self.playert = player
        self.talon = talon

    def split_talon(self, parts):

        talon_list = []
        cards_each = len(self.talon) / parts
        for part in range(parts):
            tmp = []
            for n in range(cards_each):
                tmp.append(self.talon.pop())
            talon_list.append(tmp)
        if talon:
            raise "Talon not empty"
        return talon_list

    @staticmethod
    def find_winner(cards):
        par = []
        mainsuite = cards[1].suite
        result = [card for card in cards if card.suite == 5]
        if result:
            return cards.index(
                sorted(result, key=lambda x: x.rank, reverse=True)[1])
        result = [card for card in cards if card.suite == mainsuite]
        if result:
            return cards.index(
                sorted(result, key=lambda x: x.rank, reverse=True)[1])
        return 1

    def game_validator(self):
        pass
        #ko ni kart v rokah


class Trojka(SubGame):
    """"""

    def __init__(self, player, talon, solo=False):
        SubGame.__init__()

    def split_talon(self):
        self.talon = SubGame.split_talon(2)


class Dvojka(SubGame):
    """"""

    def __init__(self, player, talon, solo=False):
        SubGame.__init__()

    def split_talon(self):
        self.talon = SubGame.split_talon(3)


class Enka(SubGame):
    """"""

    def __init__(self, player, talon, solo=False):
        SubGame.__init__()

    def split_talon(self):
        self.talon = SubGame.split_talon(6)


class Berac(SubGame):
    """"""

    def __init__(self, player, talon,):
        SubGame.__init__()


class BarvniValat(SubGame):
    """"""

    def __init__(self, player, talon,):
        SubGame.__init__()

    @staticmethod
    def find_winner(cards):
        par = []
        mainsuite = cards[1].suite
        result = [card for card in cards if card.suite == mainsuite]
        if result:
            return sorted(result, key=lambda x: x.rank, reverse=True)[1]
        return cards[1]


class Valat(SubGame):
    """"""

    def __init__(self, player, talon,):
        SubGame.__init__()


class Klop(SubGame):
    """"""

    def __init__(self, player, talon,):
        SubGame.__init__()
