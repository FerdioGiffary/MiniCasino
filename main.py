# ===================================
# MiniCasino
# ===================================
# Developed by. Ferdio Giffary
# JCDS - BSDAM29


# /************************************/
import random

def int_bet(bankroll, game_name):
    if bankroll < 10:
        bet = int(bankroll)
        print(f"Bankroll below $10 — auto ALL IN with ${bet}")
        return bet
    while True:
        s = input(f"{game_name} - Bankroll: ${int(bankroll)}. Enter your bet (whole dollars): $").strip()
        if not s.isdigit():
            print("Enter a whole number (no cents).")
            continue
        bet = int(s)
        if bet <= 0:
            print("Bet must be greater than 0.")
        elif bet > bankroll:
            print("You don't have enough funds.")
        else:
            return bet

# SLOT machine 777
def slot_round(bankroll):
    print("\n--- SLOT MACHINE 777 - GACOR ---")
    
    # Number emojis 0–9
    number_symbols = ['0️⃣','1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣']
    suit_symbols = ['♣️','♦️','♥️','♠️']
    symbols = number_symbols + suit_symbols
    
    bet = int_bet(bankroll, "Slot")
    bankroll -= bet

    # Spin 3 reels
    r1 = random.choice(symbols)
    r2 = random.choice(symbols)
    r3 = random.choice(symbols)
    spin = (r1, r2, r3)

    # rolling
    print(f"Spinning....")
    print(f"{r1} | {r2} | {r3}")

    payout = 0
    # JACKPOT
    if r1 == r2 == r3:
        payout = bet * 50
        print(f"JACKPOT! {r1} {r2} {r3} — You win ${payout} (50x)!")
    # ALL SUITS (but not all same)
    elif all(x in suit_symbols for x in spin):
        payout = bet * 3
        print(f"All suits! {r1} {r2} {r3} — You win ${payout} (3x)!")
    # ALL NUMBERS (but not all same)
    elif all(x in number_symbols for x in spin):
        payout = bet * 1
        print(f"All numbers! {r1} {r2} {r3} — You get your ${bet} back!")
    # LOSS
    else:
        print(f"Mixed symbols! {r1} {r2} {r3} — You lose your bet of ${bet}.")

    # Update bankroll
    if payout:
        bankroll += payout

    print(f"Bankroll now: ${int(bankroll)}")
    return int(bankroll)

# Magic Dice game
def dice_round(bankroll):
    print("\n--- Dice Game ---")
    bet = int_bet(bankroll, "Dice")
    bankroll -= bet

    # choose guess
    print("Choose your bet:")
    print("1) Higher than 7 (sum in 8..12)")
    print("2) Lower than 7  (sum in 2..6)")
    print("3) Exactly 7")
    while True:
        ch = input("Select 1/2/3: ").strip()
        if ch not in ('1','2','3'):
            print("Please pick 1, 2, or 3.")
            continue
        break

    # roll two dice
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    total = d1 + d2
    print(f"Dice roll: {d1} + {d2} = {total}")

    payout = 0
    if ch == '1':  # higher than 7
        if total > 7:
            payout = bet * 2
            print("You won (Higher than 7)!")
        else:
            print("You lost (not higher than 7).")
    elif ch == '2':  # lower than 7
        if total < 7:
            payout = bet * 2
            print("You won (Lower than 7)!")
        else:
            print("You lost (not lower than 7).")
    else:  # exactly 7
        if total == 7:
            payout = bet * 5
            print("Exact 7! You win big!")
        else:
            print("You lost (not exactly 7).")

    if payout:
        bankroll += int(payout)

    print(f"Payout: ${int(payout) if payout else 0}. Bankroll now: ${int(bankroll)}")
    return int(bankroll)

# Togel
def togel_round(bankroll):
    print("\n--- Togel ---")
    if bankroll < 10:
        bet = int(bankroll)
        print(f"Bankroll below $10 — auto ALL IN with ${bet}")
    else:
        while True:
            bet_input = input(f"Togel - Bankroll: ${int(bankroll)}. Enter your bet (whole dollars): $").strip()
            if not bet_input.isdigit():
                print("Enter a whole number (no cents).")
                continue
            bet = int(bet_input)
            if bet <= 0:
                print("Bet must be > 0.")
            elif bet > bankroll:
                print("You don't have enough funds.")
            else:
                break

    while True:
        num_input = input("Pick a 2-digit number (00-99): ").strip()
        if not num_input.isdigit():
            print("Enter digits only (0-99).")
            continue
        num = int(num_input)
        if 0 <= num <= 99:
            chosen = f"{num:02d}"
            break
        else:
            print("Number must be between 0 and 99.")

    bankroll -= bet

    lucky = set()
    while len(lucky) < 5:
        lucky.add(random.randint(0, 99))
    lucky_list = sorted([f"{n:02d}" for n in lucky])

    print(f"\nLucky numbers: {', '.join(lucky_list)}")
    print(f"Your pick: {chosen}")

    if chosen in lucky_list:
        payout = bet * 10
        bankroll += int(payout)
        print(f"Congratulations! {chosen} wins! You receive ${int(payout)} (10x).")
    else:
        print(f"Sorry — {chosen} not among the lucky numbers. You lose ${bet}.")

    print(f"Bankroll now: ${int(bankroll)}")
    return int(bankroll)

# Lucky 5 Toss (NEW)
def lucky5_round(bankroll):
    print("\n--- Lucky 5 Toss ---")
    bet = int_bet(bankroll, "Lucky 5 Toss")
    bankroll -= bet
    current_pot = bet

    print(f"\nYou staked ${bet}. You should've bet more, but thats okay.")
    print("Predict a coin toss: Head or Tail, if you correct your bet is doubled, easy as that")
    print("Get rich by guessing '50%' chance, what a great odds! isn't it? :)\n")

    for round_no in range(1, 6):
        next_multiplier = 2 ** round_no
        next_payout = bet * next_multiplier
        print(f"Round {round_no} — If you win this you'll get: ${next_payout} !! easy money :)")

        # get player's guess
        while True:
            guess = input("Guess coin (h for heads / t for tails): ").strip().lower()
            if guess in ('h','t','heads','tails'):
                guess_char = 'H' if guess.startswith('h') else 'T'
                break
            print("Please enter 'h' or 't' (or 'heads'/'tails').")

        # toss the coin
        coin = random.choice(['H', 'T'])
        result_str = "Heads" if coin == 'H' else "Tails"
        print(f"Coin: {result_str}  — You guessed: {'Heads' if guess_char=='H' else 'Tails'}")

        if guess_char == coin:
            # player wins this toss; double pot (we keep pot in variable but only add to bankroll at the end or on loss)
            current_pot *= 2
            print(f"Correct! Your pot is now: ${current_pot}")
            # If this was round 5, award the pot
            if round_no == 5:
                bankroll += int(current_pot)
                print(f"\n🎉 INCREDIBLE — you won all 5 tosses! You receive ${int(current_pot)} (×{2**5})")
                break
            else:
                print("Proceeding to next toss\n")
                continue
        else:
            # player lost the toss -> they lose the stake (pot)
            current_pot = 0
            print("Wrong! You lost the streak and your stake is gone.")
            print("Better luck next time, nice try:)")
            break

    print(f"Bankroll now: ${int(bankroll)}")
    return int(bankroll)

# BLACKJACK
def create_deck():
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    deck = []
    # single deck with 4 suits implied by 4 copies
    for r in ranks:
        deck.extend([r]*4)
    random.shuffle(deck)
    return deck

def card_value(rank):
    if rank in ['J','Q','K','10']:
        return 10
    if rank == 'A':
        return 11
    return int(rank)

def hand_value_and_soft(hand):
    """Return (total, is_soft) where is_soft True if an Ace counts as 11."""
    total = 0
    aces = 0
    for c in hand:
        if c == 'A':
            aces += 1
            total += 11
        elif c in ['J','Q','K','10']:
            total += 10
        else:
            total += int(c)
    # downgrade aces from 11 to 1 as needed
    while total > 21 and aces:
        total -= 10
        aces -= 1
    # is_soft True if there's still an ace counted as 11
    is_soft = (aces > 0)
    return total, is_soft

def deal_card(deck, hand):
    if not deck:
        deck.extend(create_deck())
        random.shuffle(deck)
    hand.append(deck.pop())

def show_hands(player_hand, dealer_hand, hide_dealer_first=True):
    if hide_dealer_first:
        dealer_display = f"{dealer_hand[0]}, ?"
        print(f"Dealer: [{dealer_display}]")
    else:
        dealer_display = ", ".join(dealer_hand)
        dealer_total, _ = hand_value_and_soft(dealer_hand)
        print(f"Dealer: [{dealer_display}]  (value: {dealer_total})")

    player_display = ", ".join(player_hand)
    player_total, _ = hand_value_and_soft(player_hand)
    print(f"You:    [{player_display}]  (value: {player_total})")



def is_blackjack(hand):
    total, _ = hand_value_and_soft(hand)
    return len(hand) == 2 and total == 21

def blackjack_round(bankroll):
    print("\n--- Blackjack ---")
    deck = create_deck()
    player_hand = []
    dealer_hand = []

    bet = int_bet(bankroll, "Blackjack")
    bankroll -= bet

    # initial deal
    for _ in range(2):
        deal_card(deck, player_hand)
        deal_card(deck, dealer_hand)

    # Check naturals BEFORE entering the player loop.
    player_natural = is_blackjack(player_hand)
    dealer_natural = is_blackjack(dealer_hand)

    if player_natural or dealer_natural:
        # reveal both hands for naturals
        show_hands(player_hand, dealer_hand, hide_dealer_first=False)
        if player_natural and not dealer_natural:
            payout = int(bet * 2.5)  # total returned on blackjack (3:2)
            bankroll += payout
            print(f"Blackjack! You win 3:2. You receive ${payout}.")
            return int(bankroll)
        elif dealer_natural and not player_natural:
            print("Dealer has Blackjack. You lose your bet.")
            return int(bankroll)
        else:
            bankroll += bet
            print("Both have Blackjack — push. Your bet returned.")
            return int(bankroll)

    # Player turn (show_hands at start of each player action)
    while True:
        show_hands(player_hand, dealer_hand, hide_dealer_first=True)
        player_total, _ = hand_value_and_soft(player_hand)
        if player_total > 21:
            print(f"You busted with {player_total}!")
            return int(bankroll)
        choice = input("Hit or Stand? (h/s): ").strip().lower()
        if choice in ('h','hit'):
            deal_card(deck, player_hand)
            continue
        elif choice in ('s','stand'):
            break
        else:
            print("Please type 'h' or 's'.")

    # Dealer turn — reveal and play (dealer hits soft 17)
    print("\n-- Dealer's Turn --")
    show_hands(player_hand, dealer_hand, hide_dealer_first=False)
    while True:
        dealer_total, dealer_soft = hand_value_and_soft(dealer_hand)
        # hit on <17 or on soft 17
        if dealer_total < 17 or (dealer_total == 17 and dealer_soft):
            deal_card(deck, dealer_hand)
            dealer_total, dealer_soft = hand_value_and_soft(dealer_hand)
            print(f"Dealer draws: {dealer_hand[-1]}  (value now {dealer_total}{' soft' if dealer_soft else ''})")
            continue
        else:
            if dealer_total > 21:
                print("Dealer busted!")
            else:
                print(f"Dealer stands at {dealer_total}.")
            break

    dealer_total, _ = hand_value_and_soft(dealer_hand)
    player_total, _ = hand_value_and_soft(player_hand)

    print("\n-- Final Hands --")
    show_hands(player_hand, dealer_hand, hide_dealer_first=False)

    # settlement
    if player_total > 21:
        print(f"You busted and lose your bet of ${bet}.")
        return int(bankroll)
    if dealer_total > 21:
        payout = bet * 2
        bankroll += payout
        print(f"Dealer busted. You win ${bet}!")
        return int(bankroll)
    if player_total > dealer_total:
        payout = bet * 2
        bankroll += payout
        print(f"You win! {player_total} vs {dealer_total}. You receive ${payout - bet} profit (total returned ${payout}).")
    elif player_total < dealer_total:
        print(f"You lose. {dealer_total} vs {player_total}. You lost ${bet}.")
    else:
        bankroll += bet
        print(f"Push. Both {player_total}. Your bet ${bet} returned.")

    return int(bankroll)


def readme():
    print("""
    Blackjack:
    - Simple blackjack: Ace = 1 or 11, dealer hits on soft 17.
    - Natural Blackjack pays 3:2.
    - No split, no double.
          
    Slot Machine 777:
    - 3 reels: digits 0-9 + suits ♣️ ♦️ ♥️ ♠️
    - Jackpot: all 3 identical → 50x payout!!!
    - All suits (mix of ♣️ ♦️ ♥️ ♠️ , not identical) → 3x payout
    - All numbers (mix of 0–9, not identical) → break-even (1x)
    - Otherwise lose bet
          
    Magic Dice:
    - YOU guesses: 'higher than 7' (8-12), 'lower than 7' (2-6), or 'exactly 7'.
    - Payouts:
      * Higher / Lower  -> you get 2x of your bet
      * Exactly 7       -> you get 5x of your bet
      * Else            -> you lose your bet
          
    Togel:
    - YOU guesses 2 digit number, casinos will generate 5 two-digits numbers, 
    - if your numbers in it : you get 10x bet
    - else                  : you lose your bet
    
    Lucky 5 Toss:
    - Guess Heads/Tails 5 times in a row. Each correct guess doubles your pot.
    - Win all 5 → final payout = bet × 32.
    - Lose any toss → you lose the stake.
    
    Happy Betting :)
          """)

def main_menu():
    print("Welcome to the Mini Casino!")
    print("Easy way to make you rich, just deposit as low as $100, have fun and happy betting!")
    bankroll = 100

    while True:
        print("\n--- Main Menu ---")
        print("1) Play Blackjack")
        print("2) Play Slot Machine 777")
        print("3) Play Lucky 5 Toss")
        print("4) Play Magic Dice")
        print("5) Play Togel")
        print("6) Show Bankroll")
        print("7) Read Me")
        print("8) Cash Out (Exit)")

        choice = input("Choose an option (1-8): ").strip()

        if choice == '1':
            bankroll = blackjack_round(bankroll)
        elif choice == '2':
            bankroll = slot_round(bankroll)
        elif choice == '3':
            bankroll = lucky5_round(bankroll)
        elif choice == '4':
            bankroll = dice_round(bankroll)
        elif choice == '5':
            bankroll = togel_round(bankroll)
        elif choice == '6':
            print(f"Current bankroll: ${int(bankroll)}")
        elif choice == '7':
            readme()
        elif choice == '8':
            if bankroll >= 1000:
                print(f"💵 You reached ${int(bankroll)} — You can now cash out. Thanks for playing!")
                break
            else:
                print(f"You can’t cash out yet — reach $1000 to leave the casino! (Current: ${int(bankroll)})")
        else:
            print("Invalid selection — choose 1-8.")

        if bankroll <= 0:
            print("You're out of money. Game over.")
            break

if __name__ == "__main__":
    main_menu()