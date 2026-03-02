CARDS = ["King", "Queen", "Jack"]
ACTIONS = ["c", "b", "f"] #Check or bet

class KuhnState:

    def __init__(self, history, cards):

        """Track what each players card's and action histories are"""
        self.history = history
        self.cards = cards


    def current_player(self):

        return len(self.history) % 2


def is_terminal(history):

    """This will determine how the game ends"""

    return history in ["cc", "bc", "bf", "cbc", "cbf"]


def get_utility(history, cards):

    card_ranks = {"King": 2, "Queen": 1, "Jack": 0}

    player_zero_hand = cards[0]
    player_one_hand = cards[1]

    if history.endswith("f"):

        return 1 if history == "bf" else -1

    p0_rank = card_ranks[player_zero_hand]
    p1_rank = card_ranks[player_one_hand]

    if history == "cc":

        pot = 1

    else:

        pot = 2


    if p0_rank > p1_rank:

        return pot

    else:

        return -pot



def get_available_actions(history):


    """Available Actions given the history"""


    if history in ["", "c"]:

        return ["c", "b"]

    elif history in ["b", "cb"]:

        return ["f", "c"]


    return []






