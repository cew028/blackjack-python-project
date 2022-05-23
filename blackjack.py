import random

# Define a single deck:
deck = [ 
    {
        "name": "ace",
        "suit": "clubs",
        "points" : 11,
    }, 
    {
        "name": "two",
        "suit": "clubs",
        "points" : 2,
    }, 
    {
        "name": "three",
        "suit": "clubs",
        "points" : 3,
    }, 
    {
        "name": "four",
        "suit": "clubs",
        "points" : 4,
    }, 
    {
        "name": "five",
        "suit": "clubs",
        "points" : 5,
    }, 
    {
        "name": "six",
        "suit": "clubs",
        "points" : 6,
    }, 
    {
        "name": "seven",
        "suit": "clubs",
        "points" : 7,
    }, 
    {
        "name": "eight",
        "suit": "clubs",
        "points" : 8,
    }, 
    {
        "name": "nine",
        "suit": "clubs",
        "points" : 9,
    }, 
    {
        "name": "ten",
        "suit": "clubs",
        "points" : 10,
    }, 
    {
        "name": "jack",
        "suit": "clubs",
        "points" : 10,
    }, 
    {
        "name": "queen",
        "suit": "clubs",
        "points" : 10,
    }, 
    {
        "name": "king",
        "suit": "clubs",
        "points" : 10,
    },
    {
        "name": "ace",
        "suit": "diamonds",
        "points" : 11,
    }, 
    {
        "name": "two",
        "suit": "diamonds",
        "points" : 2,
    }, 
    {
        "name": "three",
        "suit": "diamonds",
        "points" : 3,
    }, 
    {
        "name": "four",
        "suit": "diamonds",
        "points" : 4,
    }, 
    {
        "name": "five",
        "suit": "diamonds",
        "points" : 5,
    }, 
    {
        "name": "six",
        "suit": "diamonds",
        "points" : 6,
    }, 
    {
        "name": "seven",
        "suit": "diamonds",
        "points" : 7,
    }, 
    {
        "name": "eight",
        "suit": "diamonds",
        "points" : 8,
    }, 
    {
        "name": "nine",
        "suit": "diamonds",
        "points" : 9,
    }, 
    {
        "name": "ten",
        "suit": "diamonds",
        "points" : 10,
    }, 
    {
        "name": "jack",
        "suit": "diamonds",
        "points" : 10,
    }, 
    {
        "name": "queen",
        "suit": "diamonds",
        "points" : 10,
    }, 
    {
        "name": "king",
        "suit": "diamonds",
        "points" : 10,
    },
    {
        "name": "ace",
        "suit": "hearts",
        "points" : 11,
    }, 
    {
        "name": "two",
        "suit": "hearts",
        "points" : 2,
    }, 
    {
        "name": "three",
        "suit": "hearts",
        "points" : 3,
    }, 
    {
        "name": "four",
        "suit": "hearts",
        "points" : 4,
    }, 
    {
        "name": "five",
        "suit": "hearts",
        "points" : 5,
    }, 
    {
        "name": "six",
        "suit": "hearts",
        "points" : 6,
    }, 
    {
        "name": "seven",
        "suit": "hearts",
        "points" : 7,
    }, 
    {
        "name": "eight",
        "suit": "hearts",
        "points" : 8,
    }, 
    {
        "name": "nine",
        "suit": "hearts",
        "points" : 9,
    }, 
    {
        "name": "ten",
        "suit": "hearts",
        "points" : 10,
    }, 
    {
        "name": "jack",
        "suit": "hearts",
        "points" : 10,
    }, 
    {
        "name": "queen",
        "suit": "hearts",
        "points" : 10,
    }, 
    {
        "name": "king",
        "suit": "hearts",
        "points" : 10,
    },
    {
        "name": "ace",
        "suit": "spades",
        "points" : 11,
    }, 
    {
        "name": "two",
        "suit": "spades",
        "points" : 2,
    }, 
    {
        "name": "three",
        "suit": "spades",
        "points" : 3,
    }, 
    {
        "name": "four",
        "suit": "spades",
        "points" : 4,
    }, 
    {
        "name": "five",
        "suit": "spades",
        "points" : 5,
    }, 
    {
        "name": "six",
        "suit": "spades",
        "points" : 6,
    }, 
    {
        "name": "seven",
        "suit": "spades",
        "points" : 7,
    }, 
    {
        "name": "eight",
        "suit": "spades",
        "points" : 8,
    }, 
    {
        "name": "nine",
        "suit": "spades",
        "points" : 9,
    }, 
    {
        "name": "ten",
        "suit": "spades",
        "points" : 10,
    }, 
    {
        "name": "jack",
        "suit": "spades",
        "points" : 10,
    }, 
    {
        "name": "queen",
        "suit": "spades",
        "points" : 10,
    }, 
    {
        "name": "king",
        "suit": "spades",
        "points" : 10,
    },
    
]

class Table(object):   
    def __init__(
        self, 
        top_card_index, 
        shoe, 
        your_main_hand, 
        split_hand_1, 
        split_hand_2, 
        split_hand_3, 
        dealer_hand, 
        dealer_secret,
        bankroll,
        min_bet,
        max_bet,
        cut_card,
        willing_to_split,
        has_doubled_down_0,
        has_doubled_down_1,
        has_doubled_down_2,
        has_doubled_down_3,
        insured,
        playable,
    ):
        self.top_card_index = top_card_index
        self.shoe = shoe
        self.your_main_hand = your_main_hand
        self.split_hand_1 = split_hand_1
        self.split_hand_2 = split_hand_2
        self.split_hand_3 = split_hand_3
        self.dealer_hand = dealer_hand
        self.dealer_secret = dealer_secret
        self.bankroll = bankroll
        self.min_bet = min_bet
        self.max_bet = max_bet
        self.cut_card = cut_card
        self.willing_to_split = willing_to_split
        self.has_doubled_down_0 = has_doubled_down_0
        self.has_doubled_down_1 = has_doubled_down_1
        self.has_doubled_down_2 = has_doubled_down_2
        self.has_doubled_down_3 = has_doubled_down_3
        self.insured = insured
        self.playable = playable

def a_or_an(card):
    """Determines whether an "a" or an "an" should preface an inputted card."""
    if card["name"] == "ace" or card["name"] == "eight":
        which_is_it = "an"
    else:
        which_is_it = "a"
    return which_is_it

def add_to_your_bet(amount):
    """Under certain circumstances the player may add more money than just their initial bet on a given hand."""
    print(f"You add another {'${:,.2f}'.format(amount)} to the table.")

def ask_to_play_again():
    """Prompt the player to play another hand."""
    print("Would you like to play another hand?")
    play_again = yes_or_no()
    if play_again == "Yes":
        # The player elected to play again.
        table.playable = True
        if table.bankroll < table.min_bet:
            print("But you don't have enough money!")
            quit()
    elif play_again == "No":
        # The player elected not to play again.
        print("You get up and leave the blackjack table.")
        print(f"You finish with {'${:,.2f}'.format(table.bankroll)}.")
        quit()

def buy_insurance():
    """If the dealer has a face-up ace, the player can buy insurance."""
    if table.dealer_hand[0]["name"] == "ace":
        print("Would you like to buy insurance?")
        insurance = yes_or_no()
        if insurance == "Yes":
            # The player elected to buy insurance.
            if table.bankroll - 0.5*bet < bet:
                print("You tried to buy insurance, but you do not have enough money to do so.")
                print(f"In order to buy insurance, you need to bet half of your initial bet of {'${:,.2f}'.format(bet)}, but you currently only have {'${:,.2f}'.format(table.bankroll - bet)} free.")
            else:
                add_to_your_bet(bet*0.5)
                table.insured = True
        elif insurance == "No":
            # The player elected not to buy insurance.
            print("You did not buy insurance.")

def calculate_winner(hand):
    """This function determines whether the dealer or the current player hand is the winner."""
    you_doubled_down = 0
    # First we check if the hand had been doubled down.
    if (
        (hand == table.your_main_hand and table.has_doubled_down_0)
        or (hand == table.split_hand_1 and table.has_doubled_down_1)
        or (hand == table.split_hand_2 and table.has_doubled_down_2)
        or (hand == table.split_hand_3 and table.has_doubled_down_3)
    ): 
        print("Your face down card is turned over.")
        print(f"It is {a_or_an(hand[-1])} {card_namer(hand[-1])}.")
        print(f"Your final score is {score(hand)}.")
        you_doubled_down = 1
    if score(hand) <= 21 and score(hand) == score(table.dealer_hand) + score(table.dealer_secret):
        print("You tied!")
        print("Your bet is returned to you.")
    elif score(hand) > 21 or score(hand) < score(table.dealer_hand) + score(table.dealer_secret) <= 21:
        print("You lost.")
        table.bankroll = table.bankroll - (bet * (you_doubled_down+1)) # This subtracts 'bet' if you didn't double down, and '2*bet' if you did.
    else:
        print("You won!")
        table.bankroll = table.bankroll + (bet * (you_doubled_down+1)) # This adds 'bet' if you didn't double down, and '2*bet' if you did.
    check_funds()

def card_namer(card):
    """Takes a given card dictionary and converts it to 'name' of 'suit'."""
    return f"{card['name']} of {card['suit']}"

def check_for_a_natural():
    if score(table.your_main_hand) == 21:
        # The player has a natural.
        print("You have a blackjack!")
        table.playable = False
        # But does the dealer also have a natural?
        if score(table.dealer_hand) + score(table.dealer_secret) == 21:
            # The dealer also has a natural.
            print(f"The dealer turns over their face down card, revealing {a_or_an(table.dealer_secret[0])} {card_namer(table.dealer_secret[0])}, which is a blackjack as well.")
        else:
            # The dealer does not have a natural.
            winnings = bet * 1.5
            table.bankroll = table.bankroll + winnings
            print(f"The dealer turns over their face down card, revealing {a_or_an(table.dealer_secret[0])} {card_namer(table.dealer_secret[0])}, which does not beat your hand.")
            print(f"You win at a rate of 3 to 2, meaning you gain {'${:,.2f}'.format(winnings)}.")
            check_funds()

def check_funds():
    """Print how much money the player has in their bankroll."""
    print(f"Your current bankroll is {'${:,.2f}'.format(table.bankroll)}.")

def cut_card_check():
    """Did the dealer reach the cut card?"""
    if table.top_card_index > len(table.shoe) - table.cut_card:
        print("The dealer shuffles the cards.")
        random.shuffle(table.shoe)
        table.top_card_index = 0

def double_down(hand):
    """Doubling down is the act of doubling your bet in exchange for only one more card."""
    if score(hand) in {9, 10, 11}:
        print("Would you like to double down?")
        double_down = yes_or_no()
        if double_down == "Yes":
            # The player elected to double down.
            if table.bankroll - bet < bet:
                print("You tried to double down, but you do not have enough money to do so.")
                print(f"In order to double down, you need to match your initial bet of {'${:,.2f}'.format(bet)}, but you currently only have {'${:,.2f}'.format(tablet.bankroll - bet)} free.")
            else:
                add_to_your_bet(bet)
                draw(hand)
                print("The dealer gives you a final card face down.")
                match hand:
                    case table.your_main_hand:
                        table.has_doubled_down_0 = True
                    case table.split_hand_1:
                        table.has_doubled_down_1 = True
                    case table.split_hand_2:
                        table.has_doubled_down_2 = True
                    case table.split_hand_3:
                        table.has_doubled_down_3 = True
                table.playable = False
        elif double_down == "No":
            # The player elected not to double down.
            print("You did not double down.")

def draw(hand):
    """Draw a card from the shoe and place it into the inputted hand. Also increment a counter keeping track of where you are in the shoe."""
    card = table.shoe[table.top_card_index]
    table.top_card_index += 1
    hand.append(card)
    return card

def make_a_bet():
    """Prompt the player to place a wager."""
    while True:
        try:
            bet = float(input("Place your bet: $"))
        except ValueError:
            print("That is not a valid bet.")
            continue
        
        if bet > table.max_bet or bet < table.min_bet:
            print("Your bet is not in the allowed range at this casino.")
            print(f"The minimum bet is {'${:,.2f}'.format(table.min_bet)} and the maximum bet is {'${:,.2f}'.format(table.max_bet)}.")
        elif bet > table.bankroll:
            print("You cannot bet more than you currently have.")
            print(f"You only have {'${:,.2f}'.format(table.bankroll)}.")
        else:
            # The player entered a valid bet.
            break
    return bet

def move_to_next_hand(hand):
    """The player may have split pairs previously. If so, they have additional hands to play."""
    if len(hand) != 0:
        if hand == table.split_hand_1 and len(table.split_hand_2) != 0:
            print("You move to your second hand.")
        elif hand == table.split_hand_2 and len(table.split_hand_3) != 0:
            print("You move to your third hand.")
        else:
            print("You move to your final hand.")
        print(f"Your current score is {score(hand)}.")
        print(f"The dealer has a {score(table.dealer_hand)} and a face down card.")
        table.playable = True
        table.has_doubled_down = False
        table.willing_to_split = True

def initial_deal():
    """The hands are reset. The dealer passes out the first set of cards to the player and themselves."""
    table.your_main_hand = []
    table.split_hand_1 = []
    table.split_hand_2 = []
    table.split_hand_3 = []
    table.dealer_hand = []
    table.dealer_secret = []
    table.willing_to_split = True
    table.has_doubled_down_0 = False
    table.has_doubled_down_1 = False
    table.has_doubled_down_2 = False
    table.has_doubled_down_3 = False
    table.insured = False
    draw(table.your_main_hand)
    draw(table.dealer_hand)
    draw(table.your_main_hand)
    draw(table.dealer_secret)
    print(f"The dealer hands you {a_or_an(table.your_main_hand[0])} {card_namer(table.your_main_hand[0])} and themselves {a_or_an(table.dealer_hand[0])} {card_namer(table.dealer_hand[0])}.")
    print(f"The dealer then hands you {a_or_an(table.your_main_hand[1])} {card_namer(table.your_main_hand[1])} and themselves a face down card.") 
    print(f"Your current score is {score(table.your_main_hand)}.")
    print(f"The dealer has a {score(table.dealer_hand)} and a face down card.")

def pay_out_insurance():
    """If the player purchased insurance, this function resolves that."""
    if table.insured:
        print(f"As for your insurance, the dealer's face down card was {a_or_an(table.dealer_hand[1])} {card_namer(table.dealer_hand[1])}.")
        if table.dealer_hand[1]["points"] == 10:
            print("Thus, you win your insurance bet.")
            table.bankroll = table.bankroll + bet # Your half bet is doubled.
        else:
            print("Thus, you lose your insurance bet.")
            table.bankroll = table.bankroll - 0.5*bet
        check_funds()

def play_dealer_hand():
    """The dealer stands at 17 and above."""
    # First we check that there wasn't a natural already.
    if score(table.your_main_hand) != 21 or len(table.your_main_hand) != 2 or len(table.split_hand_1) != 0:
        print("The dealer's face down card is turned over.")
        print(f"It is {a_or_an(table.dealer_secret[0])} {card_namer(table.dealer_secret[0])}.")
        table.dealer_hand.append(table.dealer_secret[0])
        table.dealer_secret.remove(table.dealer_secret[0])
        print(f"The dealer's total is {score(table.dealer_hand)}.")
        while score(table.dealer_hand) <= 16:
            print("The dealer hits.")
            draw(table.dealer_hand)
            print(f"The dealer draws {a_or_an(table.dealer_hand[-1])} {card_namer(table.dealer_hand[-1])}.")
            continue
        print(f"The dealer's final score is {score(table.dealer_hand)}.")
        if score(table.dealer_hand) > 21:
            print("The dealer busts.")

def play_your_hand(hand):
    """The player can choose to hit or stand."""
    while table.playable:
        action = str(input("Would you like to Hit (H) or Stand (S)? "))
        if action.casefold() != "H".casefold() and action.casefold() != "S".casefold():
            print("Please enter H or S.")
            continue
        elif action.casefold() == "H".casefold():
            print("You hit.")
            draw(hand)
            print(f"The dealer gives you {a_or_an(hand[-1])} {card_namer(hand[-1])}.")
            if score(hand) <= 21:
                print(f"Your current score is {score(hand)}.")
                continue
            else:
                print(f"Your final score is {score(hand)}.")
                print("You bust.")
                table.playable = False
                break
        else:
            print("You stand.")
            print(f"Your final score is {score(hand)}.")
            table.playable = False
            break

def score(hand):
    """Convert an inputted hand into "points". Aces are worth 11 unless they put you over 21, in which case they are worth 1."""
    score = 0
    there_is_an_ace = 0
    for card in hand:
        score += card["points"]
        if card["name"] == "ace":
            there_is_an_ace = 1
    if score > 21 and there_is_an_ace:
        score -= 10
    return score

def split_pairs(hand):
    """If a player draws a pair on their initial deal, they have the option to split that pair."""
    if len(hand) != 0:
        if hand[0]["points"] == hand[1]["points"]:
            # This is a pair.
            print("You have a pair of the same value.")
            print("Would you like to split?")
            split = yes_or_no()
            if split == "Yes":
                # The player elected to split.
                if table.bankroll - bet < bet:
                    print("You tried to split your hand, but you do not have enough money to do so.")
                    print(f"In order to split, you need to match your initial bet of {'${:,.2f}'.format(bet)}, but you currently only have {'${:,.2f}'.format(table.bankroll - bet)} free.")
                else:
                    if len(table.split_hand_1) == 0:
                        new_hand = table.split_hand_1
                    elif len(table.split_hand_2) == 0:
                        new_hand = table.split_hand_2
                    elif len(table.split_hand_3) == 0:
                        new_hand = table.split_hand_3
                    else:
                        print("You have already split three times.")
                        print("You cannot split a fourth time.")
                    if new_hand == table.split_hand_1 or new_hand == table.split_hand_2 or new_hand == table.split_hand_3:
                        add_to_your_bet(bet)
                        moving_card = hand[1]
                        hand.remove(hand[1])
                        new_hand.append(moving_card)
                    draw(hand)
                    draw(new_hand)
                    if hand[0]["name"] == "ace":
                        # Splitting aces can only get one additional card and no hits.
                        print("You split your aces.")
                        print(f"The dealer puts {a_or_an(hand[1])} {card_namer(hand[1])} on the {card_namer(hand[0])} and {a_or_an(new_hand[1])} {card_namer(new_hand[1])} on the {card_namer(new_hand[0])}.")
                        print(f"Your final score on the first hand is {score(hand)}.")
                        print(f"Your final score on the second hand is {score(new_hand)}.")
                        table.playable = False
                    else:
                        print("You split your hand.")
                        print(f"The dealer puts {a_or_an(hand[1])} {card_namer(hand[1])} on the {card_namer(hand[0])} and {a_or_an(new_hand[1])} {card_namer(new_hand[1])} on the {card_namer(new_hand[0])}.")
                        print("You focus on the first hand.")
                        print(f"Your current score is {score(hand)} and you have one hand yet to play.")
            elif split == "No":
                # The player elected not to split.
                table.willing_to_split = False
                print("You did not split.")

def yes_or_no():
    """This prompts the player to answer a yes or no question."""
    while True:
        answer = str(input("Yes (Y) or No (N)? "))
        if answer.casefold() != "N".casefold() and answer.casefold() != "Y".casefold():
            print("Please enter Y or N.")
            continue
        elif answer.casefold() == "Y".casefold():
            return "Yes"
        else:
            return "No"

# The number of decks used:
size = 6

# Initializing the game:
table = Table(
    top_card_index = 0, 
    shoe = list(deck * size),
    your_main_hand = [],
    split_hand_1 = [],
    split_hand_2 = [],
    split_hand_3 = [],
    dealer_hand = [],
    dealer_secret = [],
    bankroll = 200,
    min_bet = 2,
    max_bet = 500,
    cut_card = 52,
    willing_to_split = True,
    has_doubled_down_0 = False,
    has_doubled_down_1 = False,
    has_doubled_down_2 = False,
    has_doubled_down_3 = False,
    insured = False,
    playable = True,
)

# Before we begin, we shuffle the shoe:
random.shuffle(table.shoe)
table.playable = True

print("Welcome to the casino.")
check_funds()
print(f"The casino accepts bets between {'${:,.2f}'.format(table.min_bet)} and {'${:,.2f}'.format(table.max_bet)}, and pays out blackjacks at a rate of 3 to 2.")
print("You can split hands up to a maximum of three times.")
print("You sit at a table and begin to play blackjack.")
while True:
    bet = make_a_bet()
    initial_deal()
    check_for_a_natural()
    split_pairs(table.your_main_hand)
    # The player may have the ability to split again if they happened to draw another pair. 
    # The following if statements makes sure not to double-ask them if they've already said no. 
    # We ask twice more since players can split up to three times.
    if table.willing_to_split:
        split_pairs(table.your_main_hand)
    if table.willing_to_split:
        split_pairs(table.your_main_hand)
    double_down(table.your_main_hand)
    buy_insurance()
    play_your_hand(table.your_main_hand)
    move_to_next_hand(table.split_hand_1)
    # To get here, the player must have already split once.
    split_pairs(table.split_hand_1)
    # The following if statement prevents us from double-asking if they say no this time.
    if table.willing_to_split:
        split_pairs(table.split_hand_1)
    double_down(table.split_hand_1)
    play_your_hand(table.split_hand_1)
    move_to_next_hand(table.split_hand_2)
    split_pairs(table.split_hand_2)
    # No if statement is necessary here since, even if they wanted to split again, the player has already split the maximum number of times.
    double_down(table.split_hand_2)
    play_your_hand(table.split_hand_2)
    move_to_next_hand(table.split_hand_3)
    double_down(table.split_hand_3)
    play_your_hand(table.split_hand_3)
    play_dealer_hand()
    calculate_winner(table.your_main_hand)
    if len(table.split_hand_1) != 0: 
        if len(table.split_hand_2) != 0:
            print("The dealer then turns to your second hand.")
        else:
            print("The dealer then turns to your final hand.")
        calculate_winner(table.split_hand_1)
    if len(table.split_hand_2) != 0:
        if len(table.split_hand_3) != 0:
            print("The dealer then turns to your third hand.")
        else:
            print("The dealer then turns to your final hand.")
        calculate_winner(table.split_hand_2)
    if len(table.split_hand_3) != 0:
        print("The dealer then turns to your final hand.")
        calculate_winner(table.split_hand_3)
    pay_out_insurance()
    ask_to_play_again()
    cut_card_check()    # Note that placing this function here means that we only shuffle the shoe only at the ends of hands.
                        # This is okay though - if the cut card is deep enough one hand will not run out of cards.
                        # The variable amount of cards in the last hand also means that the deck penetration isn't quite hard-coded.