import sys
from collections import Counter
from functools import total_ordering

CARDS = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 1,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}

FIVE_OF_A_KIND = 6
FOUR_OF_A_KIND = 5
FULL_HOUSE = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0


@total_ordering
class Card:
    def __init__(self, value):
        self.value = value
        self.weight = CARDS[self.value]

    def __eq__(self, other):
        return self.weight == other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __hash__(self):
        return hash(self.value)

    def __str__(self):
        return self.value


@total_ordering
class Hand:
    def __init__(self, cards: list[Card], bid: int, weight: int):
        self.cards = cards
        self.bid = bid
        self.weight = weight

    def __eq__(self, other):
        return self.cards == other.cards

    def __gt__(self, other):
        if self.weight == other.weight:
            for i in range(len(self.cards)):
                if self.cards[i] == other.cards[i]:
                    continue
                return self.cards[i] > other.cards[i]
        return self.weight > other.weight

    def __str__(self):
        return "".join(str(c) for c in self.cards)

    @classmethod
    def parse(cls, s: str, bid: int = 0):
        counter = Counter()
        cards = []
        for ch in s:
            card = Card(ch)
            counter[ch] += 1
            cards.append(card)

        weight = cls.parse_weight(counter)

        cards = [Card(c) for c in s]
        return cls(cards=cards, bid=bid, weight=weight)

    @staticmethod
    def parse_weight(counter):
        weight = HIGH_CARD
        jokers = counter.get("J")
        if jokers:
            for v in sorted(counter):
                if v == "J":
                    continue
                else:
                    counter[v] += jokers
                    del counter["J"]

        l = len(counter)
        if l == 1:
            weight = FIVE_OF_A_KIND
        elif l == 2:
            if any(v == 4 for v in counter.values()):
                weight = FOUR_OF_A_KIND
            else:
                weight = FULL_HOUSE
        elif l == 3:
            if any(v == 3 for v in counter.values()):
                weight = THREE_OF_A_KIND
            else:
                weight = TWO_PAIR
        elif l == 4:
            weight = ONE_PAIR

        return weight


def parse_lines(lines):
    hands = []
    for line in lines:
        h, bid = line.split()
        hands.append(Hand.parse(h, bid=int(bid)))
    return hands


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.readlines()

    hands = parse_lines(lines)
    hands.sort()

    winnings = 0
    for i, hand in enumerate(hands):
        winnings += (i + 1) * hand.bid

    print(winnings)
