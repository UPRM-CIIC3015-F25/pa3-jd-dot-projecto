from Cards.Card import Card, Rank

# TODO (TASK 3): Implement a function that evaluates a player's poker hand.
#   Loop through all cards in the given 'hand' list and collect their ranks and suits.
#   Use a dictionary to count how many times each rank appears to detect pairs, three of a kind, or four of a kind.
#   Sort these counts from largest to smallest. Use another dictionary to count how many times each suit appears to check
#   for a flush (5 or more cards of the same suit). Remove duplicate ranks and sort them to detect a
#   straight (5 cards in a row). Remember that the Ace (rank 14) can also count as 1 when checking for a straight.
#   If both a straight and a flush occur in the same suit, return "Straight Flush". Otherwise, use the rank counts
#   and flags to determine if the hand is: "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind",
#   "Two Pair", "One Pair", or "High Card". Return a string with the correct hand type at the end.
def evaluate_hand(hand: list[Card]):

    ranks = [card.rank.value for card in hand]
    suits = [card.suit for card in hand]

    rankCount = {}
    for r in ranks:
        rankCount[r] = rankCount.get(r, 0) + 1

    countList = sorted(rankCount.values(), reverse=True)

    suitCount = {}
    for s in suits:
        suitCount[s] = suitCount.get(s, 0) + 1

    flushSuit = None
    for s, c in suitCount.items():
        if c >= 5:
            flushSuit = s
            break

    uniqueRanks = sorted(set(ranks))

    if 14 in uniqueRanks:
        uniqueRanks.append(1)
        uniqueRanks = sorted(set(uniqueRanks))

    straight = False
    straightHigh = 0

    for i in range(len(uniqueRanks) - 4):
        if (uniqueRanks[i] + 1 == uniqueRanks[i+1] and
            uniqueRanks[i] + 2 == uniqueRanks[i+2] and
            uniqueRanks[i] + 3 == uniqueRanks[i+3] and
            uniqueRanks[i] + 4 == uniqueRanks[i+4]):
            straight = True
            straightHigh = uniqueRanks[i+4]
            break

    if straight and flushSuit is not None:

        flushCards = [c.rank.value for c in hand if c.suit == flushSuit]
        flushUnique = sorted(set(flushCards))

        if 14 in flushUnique:
            flushUnique.append(1)
            flushUnique = sorted(set(flushUnique))

        for i in range(len(flushUnique) - 4):
            if (flushUnique[i] + 1 == flushUnique[i+1] and
                flushUnique[i] + 2 == flushUnique[i+2] and
                flushUnique[i] + 3 == flushUnique[i+3] and
                flushUnique[i] + 4 == flushUnique[i+4]):
                return "Straight Flush"

    if countList[0] == 4:
        return "Four of a Kind"
    if countList[0] == 3 and countList[1] == 2:
        return "Full House"
    if flushSuit is not None:
        return "Flush"
    if straight:
        return "Straight"
    if countList[0] == 3:
        return "Three of a Kind"
    if countList[0] == 2 and countList[1] == 2:
        return "Two Pair"
    if countList[0] == 2:
        return "One Pair"

    return "High Card"

