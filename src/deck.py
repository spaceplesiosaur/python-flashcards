class Deck:
    def __init__(self, card_stack):
        self.cards = card_stack
    def count_cards(self):
        return len(self.cards)
