"""

Implementation of a Counterfactual Rergret Minimization to generate Nash Equilbrim for Kuhn Poker

"""


class Node:

    """Node class that represents an Information Set in a Tree"""

    def __init__(self, card, betting_history):
        

        self.cards = card
        self.betting_history = betting_history

        self.info_history = f"{card}, {betting_history}" #Generate a unique i.d for each hand


        #This will track the regre and stratgey sum for eahc hand
        self.regret_sum = []
        self.stratgey_sum = []