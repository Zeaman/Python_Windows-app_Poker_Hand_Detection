import tkinter as tk


def FindPokerHand(hands):
    # Define variable lists:
    possible_ranks = []  # for the possible ranks got
    ranks = []  # Empty list for the ranks
    suits = []  # Empty list for the suits

    for cards in hands:
        # Use if condition to access card number 10:
        if len(cards) == 2:
            rank = cards[0]
            suit = cards[1]
        else:
            rank = cards[0:2]
            suit = cards[2]
        if rank == "A":
            rank = 14
        elif rank == "K":
            rank = 13
        elif rank == "Q":
            rank = 12
        elif rank == "J":
            rank = 11

        # Add the rank and suit found to the empty lists above:
        ranks.append(int(rank))
        suits.append(suit)
    # Print the ranks and suits appended:
    # print(ranks)

    # Sort the extracted ranks:
    sorted_ranks = sorted(ranks)
    # print(sorted_ranks)

    # Check the Cases:
    # Check: Royal Flush, Straight Flush, & Flush:
    if suits.count(suits[0]) == 5:
        if 10 in sorted_ranks and 11 in sorted_ranks and 12 in sorted_ranks and \
                13 in sorted_ranks and 14 in sorted_ranks:
            possible_ranks.append(1)  # (1) Royal Flush

        elif all(sorted_ranks[i] == sorted_ranks[i - 1] + 1 for i in range(1, len(sorted_ranks))):
            possible_ranks.append(2)  # (2) Straight Flush

        else:
            possible_ranks.append(5)  # (5) Flush

    # Straight:
    if all(sorted_ranks[i] == sorted_ranks[i - 1] + 1 for i in range(1, len(sorted_ranks))):
        possible_ranks.append(6)    # Straight

    hand_unique_vals = list(set(sorted_ranks))
    # print(hand_unique_vals)

    # Four of the kind and Full House:
    if len(hand_unique_vals) == 2:
        for val in hand_unique_vals:
            if sorted_ranks.count(val) == 4:
                possible_ranks.append(3)  # (3) Four of the kind
            if sorted_ranks.count(val) == 3:
                possible_ranks.append(4)  # (4) Full House

    # Three of the kind and Two Pair:
    if len(hand_unique_vals) == 3:
        for val in hand_unique_vals:
            if sorted_ranks.count(val) == 3:
                possible_ranks.append(7)  # (7) Three of the kind
            if sorted_ranks.count(val) == 2:
                possible_ranks.append(8)  # (8) Two Pair

    # Pair:
    if len(hand_unique_vals) == 4:
        possible_ranks.append(9)  # (9) Pair

    if not possible_ranks:
        possible_ranks.append(10)  # (10) High Card

    # Print the possible ranks:
    # print(possible_ranks)

    # Create a dictionary for the pokers:
    pokerHandRanks_dec = {1: "Royal Flush", 2: "Straight Flush", 3: "Four of a Kind", 4: "Full House", 5: "Flush",
                          6: "Straight", 7: "Three of Kind", 8: "Two Pair", 9: "Pair", 10: "High Card"}

    output_poker = pokerHandRanks_dec[max(possible_ranks)]
    print(hands, output_poker)
    return output_poker


def check_poker_hand():
    input_cards = [entry.get().upper() for entry in entry_widgets]
    result = FindPokerHand(input_cards)
    result_label.config(text=f"Poker Hand: {result}")


# Create the main window
root = tk.Tk()
root.title("Poker Hand Detection GUI")

# Create entry widgets for card input
entry_widgets = [tk.Entry(root, width=3) for _ in range(5)]
for entry in entry_widgets:
    entry.pack(side=tk.LEFT, padx=5)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=check_poker_hand)
submit_button.pack(side=tk.LEFT, padx=5)

# Create a label to display the result
result_label = tk.Label(root, text="Poker Hand: ")
result_label.pack(pady=10)

# Make the window non-resizable
root.resizable(False, False)
# root.geometry("300x50")  # Set the size of the GUI window Size: width and height

# Run the Tkinter event loop
root.mainloop()
