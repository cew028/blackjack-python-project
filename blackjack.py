import random

#Define a single deck:
deck = [ "ace of clubs", "two of clubs", "three of clubs", "four of clubs", "five of clubs", "six of clubs", "seven of clubs", "eight of clubs", "nine of clubs", "ten of clubs", "jack of clubs", "queen of clubs", "king of clubs",
"ace of diamonds", "two of diamonds", "three of diamonds", "four of diamonds", "five of diamonds", "six of diamonds", "seven of diamonds", "eight of diamonds", "nine of diamonds", "ten of diamonds", "jack of diamonds", "queen of diamonds", "king of diamonds",
"ace of hearts", "two of hearts", "three of hearts", "four of hearts", "five of hearts", "six of hearts", "seven of hearts", "eight of hearts", "nine of hearts", "ten of hearts", "jack of hearts", "queen of hearts", "king of hearts",
"ace of spades", "two of spades", "three of spades", "four of spades", "five of spades", "six of spades", "seven of spades", "eight of spades", "nine of spades", "ten of spades", "jack of spades", "queen of spades", "king of spades" ]

#"a" or "an" calculator:
def aoran(card):
    if "ace" in card or "eight" in card:
        whichisit = "an"
    else:
        whichisit = "a"
    return whichisit
 
#The number of decks used:
size = 6

#Initializing the shoe.
shoe = list(deck * size)

#The number of cards that are not dealt before shuffling:
cutcard = 52 

#Minimum bet size:
minbet = 2

#Maximum bet size:
maxbet = 500

#Amount of money you have:
bankroll = 200

#Drawing a card and placing it into a hand:
def draw(hand):
    global topcardindex
    card = shoe[topcardindex]
    topcardindex += 1
    hand.append(card)
    return card
    
#Converting a card to points:
def convertpt(card):
    if "ace" in card:
        points = 11
    elif "two" in card:
        points = 2
    elif "three" in card:
        points = 3
    elif "four" in card:
        points = 4
    elif "five" in card:
        points = 5
    elif "six" in card:
        points = 6
    elif "seven" in card:
        points = 7
    elif "eight" in card:
        points = 8
    elif "nine" in card:
        points = 9
    elif "ten" in card:
        points = 10
    elif "jack" in card:
        points = 10
    elif "queen" in card:
        points = 10
    elif "king" in card:
        points = 10
    else:
        print("There was an unexpected error. Perhaps you are trying to evaluate the score of something that is not a playing card?")
        points = 0
    return points
    
#Converting a card to its name:
def convertnm(card):
    if "ace" in card:
        name = "ace"
    elif "two" in card:
        name = "two"
    elif "three" in card:
        name = "three"
    elif "four" in card:
        name = "four"
    elif "five" in card:
        name = "five"
    elif "six" in card:
        name = "six"
    elif "seven" in card:
        name = "seven"
    elif "eight" in card:
        name = "eight"
    elif "nine" in card:
        name = "nine"
    elif "ten" in card:
        name = "ten"
    elif "jack" in card:
        name = "jack"
    elif "queen" in card:
        name = "queen"
    elif "king" in card:
        name = "king"
    else:
        print("There was an unexpected error. Perhaps you are trying to evaluate the name of something that is not a playing card?")
        name = "ERROR"
    return name
    
#Scoring a hand:
def score(hand):
    value = 0
    isthereanace = 0
    for i in range(len(hand)):
        value += convertpt(hand[i])
        if convertpt(hand[i]) == 11:
            isthereanace = 1
    if value > 21 and isthereanace == 1:
        value -= 10
    return value
    
#Splitting a hand:
def computesplit(hand):
    if convertnm(hand[0]) == convertnm(hand[1]):
        #They do have a pair.
        print("You have a pair of the same denomination.")
        print("Would you like to split?")
        while True:
            split = str(input("Yes (Y) or No (N)? "))
            if split.casefold() != "N".casefold() and split.casefold() != "Y".casefold():
                print("Please enter Y or N.")
                continue
            elif split.casefold() == "Y".casefold():
                #They chose to split.
                if bankroll-bet < bet:
                    print("You tried to split your hand, but you do not have enough money to do so.")
                    print(f"In order to split, you need to match your initial bet of {'${:,.2f}'.format(bet)}, but you currently only have {'${:,.2f}'.format(bankroll-bet)} free.")
                    break
                else:
                    if len(splithand1) == 0:
                        newhand = splithand1
                    elif len(splithand2) == 0:
                        newhand = splithand2
                    elif len(splithand3) == 0:
                        newhand = splithand3
                    else:
                        print("You have already split three times.")
                        print("You cannot split a fourth time.")
                    if newhand == splithand1 or newhand == splithand2 or newhand == splithand3:
                        print(f"You add another {'${:,.2f}'.format(bet)} to the table.")
                        movingcard = hand[1]
                        hand.remove(hand[1])
                        newhand.append(movingcard)
                    if convertnm(hand[0]) == "ace":
                        #Splitting aces can only get one additional card and no hits.
                        draw(hand) #The card on your first hand.
                        draw(newhand) #The card on your second hand.
                        print("You split your aces.")
                        print(f"The dealer puts {aoran(hand[1])} {hand[1]} on the {hand[0]} and {aoran(newhand[1])} {newhand[1]} on the {newhand[0]}.")
                        print(f"Your final score on the first hand is {score(hand)}.")
                        print(f"Your final score on the second hand is {score(newhand)}.")
                        playable = 0
                        break
                        
                    else:
                        draw(hand) #The card on your first hand.
                        draw(newhand) #The card on your second hand.
                        print("You split your hand.")
                        print(f"The dealer puts {aoran(hand[1])} {hand[1]} on the {hand[0]} and {aoran(newhand[1])} {newhand[1]} on the {newhand[0]}.")
                        print("You focus the first hand.")
                        print(f"Your current score is {score(hand)} and you have one hand yet to play.")
                        break
            else:
                #They chose not to split.
                print("You did not split.")
                break
  
#Computing double down:
def computedd(hand):
    global dd_ed
    if score(hand) in [9,10,11]:
        print("Would you like to double down?")
        while True:
            doubledown = str(input("Yes (Y) or No (N)? "))
            if doubledown.casefold() != "N".casefold() and doubledown.casefold() != "Y".casefold():
                print("Please enter Y or N.")
                continue
            elif doubledown.casefold() == "Y".casefold():
                #They chose to double down.
                if bankroll-bet < bet:
                    print("You tried to double down, but you do not have enough money to do so.")
                    print(f"In order to double down, you need to match your initial bet of {'${:,.2f}'.format(bet)}, but you currently only have {'${:,.2f}'.format(bankroll-bet)} free.")
                    break
                else:
                    print(f"You add another {'${:,.2f}'.format(bet)} to the table.")
                    draw(hand)
                    print("The dealer gives you a final card face down.")
                    dd_ed = 1
                    playable = 0
                    break
            else:
                #They chose not to double down.
                print("You did not double down.")
                break
    return dd_ed

#Calculating who won:
def calculatewin(hand):
    global bankroll
    if dd_ed == 1:
        print("Your face down card is turned over.")
        print(f"It is {aoran(hand[-1])} {hand[-1]}.")
        print(f"Your final score is {score(hand)}.")
    if score(hand) <= 21 and score(hand) == score(dealerhand) + score(dealersecret):
        print("You tied!")
        print("Your bet is returned to you.")
        print(f"Your current bankroll is {'${:,.2f}'.format(bankroll)}.")
    elif score(hand) > 21 or score(hand) < score(dealerhand) + score(dealersecret) <= 21:
        print("You lost.")
        bankroll = bankroll - (bet * (dd_ed+1)) #This is bet*1 if you didn't double down and bet*2 if you did.
        print(f"Your current bankroll is {'${:,.2f}'.format(bankroll)}.")
    else:
        print("You won!")
        bankroll = bankroll + (bet * (dd_ed+1)) #This is bet*1 if you didn't double down and bet*2 if you did.
        print(f"Your current bankroll is {'${:,.2f}'.format(bankroll)}.")
    

#Before we begin, we shuffle the shoe:
random.shuffle(shoe)
topcardindex = 0

print("Welcome to the casino.")
print(f"You currently have {'${:,.2f}'.format(bankroll)}.")
print(f"The casino accepts bets between {'${:,.2f}'.format(minbet)} and {'${:,.2f}'.format(maxbet)}, and pays out blackjacks at a rate of 3 to 2.")
print("You can split hands up to a maximum of three times.")
print("You sit at a table and begin to play blackjack.")

#Playing blackjack:

playable = 1 #When this changes to 0, you cannot make any more moves.

while True:
    dd_ed = 0 #At the start of a round, reset the check if the player has doubled down.
    insured = 0 #At the start of a round, reset the check if the player has bought insurance.
    #Begin by placing a bet:
    while True:
        try:
            bet = float(input("Place your bet: $"))
        except ValueError:
            print("That is not a valid bet.")
            continue
            
        if bet > maxbet or bet < minbet:
            print("Your bet is not in the allowed range at this casino.")
            print(f"The minimum bet is {'${:,.2f}'.format(minbet)} and the maximum bet is {'${:,.2f}'.format(maxbet)}.")
        elif bet > bankroll:
            print("You cannot bet more than you currently have.")
            print(f"You only have {'${:,.2f}'.format(bankroll)}.")
        else:
            #The player entered a valid bet.
            break
    #The bet has been placed.

    #Next deal the cards:
    yourhand = []
    splithand1 = []
    splithand2 = []
    splithand3 = []
    dealerhand = []
    dealersecret = []
    draw(yourhand) #Your first card.
    draw(dealerhand) #The dealer's card.
    draw(yourhand) #Your second card.
    draw(dealersecret) #The dealer's face down card.
    print(f"The dealer hands you {aoran(yourhand[0])} {yourhand[0]} and themselves {aoran(dealerhand[0])} {dealerhand[0]}.")
    print(f"The dealer then hands you {aoran(yourhand[1])} {yourhand[1]} and themselves a face down card.") 
    print(f"Your current score is {score(yourhand)}.")
    print(f"The dealer has a {score(dealerhand)} and a face down card.")
    #The first four cards have been dealt.

    #Does the player have a natural?
    if score(yourhand) == 21:
        #Yes! But does the dealer also?
        if score(dealerhand) + score(dealersecret) == 21:
            #They do too!
            print("You have a blackjack!")
            print(f"The dealer turns over their face down card, revealing {aoran(dealersecret[0])} {dealersecret[0]}, which is a blackjack as well.")
            playable = 0
        else:
            #They don't!
            winnings = bet*1.5
            bankroll = bankroll + winnings
            print("You have a blackjack!")
            print(f"The dealer turns over their face down card, revealing {aoran(dealersecret[0])} {dealersecret[0]}, which does not beat your hand.")
            print(f"You win at a rate of 3 to 2, meaning you gain {'${:,.2f}'.format(winnings)}.")
            print(f"Your total bankroll is {'${:,.2f}'.format(bankroll)}.")
            playable = 0
    #Otherwise, the player does not have a natural. Play the hand.
        
    #Does the player have a pair and want to split them?
    computesplit(yourhand)
    computesplit(yourhand)
    computesplit(yourhand) #You can split up to three times.
    #Otherwise, they do not have a pair.
        
    #Can the player double down?
    computedd(yourhand)
    #Otherwise, they cannot double down.

    #Can the player buy insurance?
    if convertnm(dealerhand[0]) == "ace":
        #The player can buy insurance if they want.
        print("Would you like to buy insurance?")
        while True:
            insurance = str(input("Yes (Y) or No (N)? "))
            if insurance.casefold() != "N".casefold() and insurance.casefold() != "Y".casefold():
                print("Please enter Y or N.")
                continue
            elif insurance.casefold() == "Y".casefold():
                #They chose to buy insurance.
                if bankroll - 0.5*bet < bet:
                    print("You tried to buy insurance, but you do not have enough money to do so.")
                    print(f"In order to buy insurance, you need to bet half of your initial bet of {'${:,.2f}'.format(bet)}, but you currently only have {'${:,.2f}'.format(bankroll-bet)} free.")
                    break
                else:
                    print(f"You add another {'${:,.2f}'.format(bet*0.5)} to the table.")
                    insured = 1
                    break
            else:
                #They chose not to buy insurance.
                print("You did not buy insurance.")
                break
    #Otherwise, they cannot buy insurance.

    #Now we play!
    while playable == 1 and dd_ed == 0: #Here begins the gameplay of yourhand.
        action = str(input("Would you like to Hit (H) or Stand (S)? "))
        if action.casefold() != "H".casefold() and action.casefold() != "S".casefold():
            print("Please enter H or S.")
            continue
        elif action.casefold() == "H".casefold():
            print("You hit.")
            draw(yourhand)
            print(f"The dealer gives you {aoran(yourhand[-1])} {yourhand[-1]}.")
            if score(yourhand) <= 21:
                print(f"Your current score is {score(yourhand)}.")
                continue
            else:
                print(f"Your final score is {score(yourhand)}.")
                print("You bust.")
                playable = 0
                break
        else:
            print("You stand.")
            print(f"Your final score is {score(yourhand)}.")
            playable = 0
            break
    #The player finishes their game.
    
    #Did the player split? If so, they have another hand to play.
    if len(splithand1) != 0:
        print("You move to your next hand.")
        print(f"Your current score is {score(splithand1)}.")
        print(f"The dealer has a {score(dealerhand)} and a face down card.")
        playable = 1
        dd_ed = 0
        computesplit(splithand1)
        computesplit(splithand1)
        computedd(splithand1)
        while playable == 1 and dd_ed == 0: #Here begins the gameplay of splithand1.
            action = str(input("Would you like to Hit (H) or Stand (S)? "))
            if action.casefold() != "H".casefold() and action.casefold() != "S".casefold():
                print("Please enter H or S.")
                continue
            elif action.casefold() == "H".casefold():
                print("You hit.")
                draw(splithand1)
                print(f"The dealer gives you {aoran(splithand1[-1])} {splithand1[-1]}.")
                if score(splithand1) <= 21:
                    print(f"Your current score is {score(splithand1)}.")
                    continue
                else:
                    print(f"Your final score is {score(splithand1)}.")
                    print("You bust.")
                    playable = 0
                    break
            else:
                print("You stand.")
                print(f"Your final score is {score(splithand1)}.")
                playable = 0
                break
    if len(splithand2) != 0:
        print("You move to your next hand.")
        print(f"Your current score is {score(splithand2)}.")
        print(f"The dealer has a {score(dealerhand)} and a face down card.")
        playable = 1
        dd_ed = 0
        computesplit(splithand2)
        computedd(splithand2)
        while playable == 1 and dd_ed == 0: #Here begins the gameplay of this splithand2.
            action = str(input("Would you like to Hit (H) or Stand (S)? "))
            if action.casefold() != "H".casefold() and action.casefold() != "S".casefold():
                print("Please enter H or S.")
                continue
            elif action.casefold() == "H".casefold():
                print("You hit.")
                draw(splithand2)
                print(f"The dealer gives you {aoran(splithand2[-1])} {splithand2[-1]}.")
                if score(splithand2) <= 21:
                    print(f"Your current score is {score(splithand2)}.")
                    continue
                else:
                    print(f"Your final score is {score(splithand2)}.")
                    print("You bust.")
                    playable = 0
                    break
            else:
                print("You stand.")
                print(f"Your final score is {score(splithand2)}.")
                playable = 0
                break
    if len(splithand3) != 0:
        print("You move to your final hand.")
        print(f"Your current score is {score(splithand3)}.")
        print(f"The dealer has a {score(dealerhand)} and a face down card.")
        playable = 1
        dd_ed = 0
        computedd(splithand3)
        while playable == 1 and dd_ed == 0: #Here begins the gameplay of this splithand3.
            action = str(input("Would you like to Hit (H) or Stand (S)? "))
            if action.casefold() != "H".casefold() and action.casefold() != "S".casefold():
                print("Please enter H or S.")
                continue
            elif action.casefold() == "H".casefold():
                print("You hit.")
                draw(splithand3)
                print(f"The dealer gives you {aoran(splithand3[-1])} {splithand3[-1]}.")
                if score(splithand3) <= 21:
                    print(f"Your current score is {score(splithand3)}.")
                    continue
                else:
                    print(f"Your final score is {score(splithand3)}.")
                    print("You bust.")
                    playable = 0
                    break
            else:
                print("You stand.")
                print(f"Your final score is {score(splithand3)}.")
                playable = 0
                break
    #Now the player has finished playing all splits.

    #The dealer now plays.
    #First we should check that there wasn't a natural.
    if score(yourhand) != 21 or len(yourhand) != 2 or len(splithand1) != 0: #If there wasn't a natural, the dealer now plays normally.
        print("The dealer's face down card is turned over.")
        print(f"It is {aoran(dealersecret[0])} {dealersecret[0]}.")
        dealerhand.append(dealersecret[0])
        dealersecret.remove(dealersecret[0])
        print(f"The dealer's total is {score(dealerhand)}.")
        while score(dealerhand) <= 16:
            print("The dealer hits.")
            draw(dealerhand)
            print(f"The dealer draws {aoran(dealerhand[-1])} {dealerhand[-1]}.")
            continue
        print(f"The dealer's final score is {score(dealerhand)}.")
        if score(dealerhand) > 21:
            print("The dealer busts.")
    #The dealer ends.

    #Who won?
    calculatewin(yourhand)
    if len(splithand1) != 0:
        print("The dealer then turns to your second hand.")
        calculatewin(splithand1)
    if len(splithand2) != 0:
        print("The dealer then turns to your third hand.")
        calculatewin(splithand2)
    if len(splithand3) != 0:
        print("The dealer then turns to your final hand.")
        calculatewin(splithand3)
    if insured == 1:
        print(f"As for your insurance, the dealer's face down card was {aoran(dealerhand[1])} {dealerhand[1]}.")
        if convertpt(dealerhand[1]) == 10:
            print("Thus, you win your insurance bet.")
            bankroll = bankroll + bet #Your half bet is doubled.
            print(f"Your current bankroll is {'${:,.2f}'.format(bankroll)}.")
        else:
            print("Thus, you lose your insurance bet.")
            bankroll = bankroll - 0.5*bet
            print(f"Your current bankroll is {'${:,.2f}'.format(bankroll)}.")
    playable = 1
    #It's been determined who won.
        
    #Would you like to play again?
    print("Would you like to play another hand?")
    while True:
        playagain = str(input("Yes (Y) or No (N)? "))
        if playagain.casefold() != "N".casefold() and playagain.casefold() != "Y".casefold():
            print("Please enter Y or N.")
            continue
        elif playagain.casefold() == "Y".casefold():
            #They chose to play again.
            if bankroll < minbet:
                print("But you don't have enough money!")
                quit()
            break
        else:
            #They chose not to play again.
            print("You get up and leave the blackjack table.")
            print(f"You finish with {'${:,.2f}'.format(bankroll)}.")
            quit()
            break
    #You've chosen whether or not to play again.
        
    #Did you reach the cut card?
    if topcardindex > len(shoe) - cutcard:
        print("The dealer shuffles the cards.")
        random.shuffle(shoe)
        topcardindex = 0
    #As written, this shuffles the deck only at the ends of hands. That's okay though. And the variable amount of cards in the last hand means that the deck penetration isn't quite hard coded.
