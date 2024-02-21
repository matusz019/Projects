import random
class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"
    
class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        return self.cards.pop()
    
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
    
    def add_card(self, card):
        self.cards.append(card)
        self.value = self.calculate_value()  # Update the value attribute

    def calculate_value(self):
        value = 0
        ace_count = 0
        word_to_number = {
        'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10
        }
    
    # Calculate the value of the hand
        for card in self.cards:
            if card.rank.lower() in word_to_number:  # Convert to lowercase for case-insensitive comparison
                value += word_to_number[card.rank.lower()]  # Add the numerical value directly
            elif card.rank in ['Jack', 'Queen', 'King']:
                value += 10
            elif card.rank == 'Ace':
                ace_count += 1
                value += 11  # Assume Ace as 11 initially

        # Adjust Ace value if necessary to avoid bust
        while value > 21 and ace_count:
            value -= 10
            ace_count -= 1
        
        return value



class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def hit_or_stand(self):
        while True:
            decision = input(f"{self.name}, do you want to hit or stand? (h/s): ").lower()
            if decision == 'h':
                return 'hit'
            elif decision == 's':
                return 'stand'
            else:
                print("Invalid input! Please enter 'h' to hit or 's' to stand.")
        
class Dealer:
    def __init__(self):
        self.hand = Hand()

    def hit_or_stand(self):
        pass  # Implement logic for dealer's hit or stand decision

class Game:
    def __init__(self, num_players):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = [Player(f"Player {i+1}") for i in range(num_players)]
        self.dealer = Dealer()

    def deal_initial_cards(self):
        # Deal two cards to each player and the dealer
        for _ in range(2):
            for player in self.players:
                player.hand.add_card(self.deck.deal())
            self.dealer.hand.add_card(self.deck.deal())

    def play_game(self):
        print("Welcome to Blackjack!")
        
        # Deal initial cards
        self.deal_initial_cards()

        # Show initial cards
        print("Dealer's Hand:")
        print(" <card hidden>")
        print(f" {self.dealer.hand.cards[1]}")
        print("\nPlayers' Hands:")
        for player in self.players:
            print(f"{player.name}: {', '.join(str(card) for card in player.hand.cards)} Total Value: {player.hand.calculate_value()}")
            

        # Players' turn
        for player in self.players:
            print(f"\n{player.name}'s Turn:")
            while True:
                decision = player.hit_or_stand()
                if decision == 'hit':
                    new_card = self.deck.deal()
                    player.hand.add_card(new_card)
                    print(f"{player.name} hits and draws {new_card}.")
                    print(f"New hand value: {player.hand.calculate_value()}")
                    if player.hand.calculate_value() > 21:
                        print(f"{player.name} busts!")
                        break
                else:
                    print(f"{player.name} stands.")
                    break

        # Dealer's turn
        print("\nDealer's Turn:")
        while self.dealer.hand.calculate_value() < 17:
            new_card = self.deck.deal()
            self.dealer.hand.add_card(new_card)
            print(f"Dealer hits and draws {new_card}.")
            print(f"New hand value: {self.dealer.hand.calculate_value()}")
            if self.dealer.hand.calculate_value() > 21:
                print("Dealer busts!")
                break
        else:
            print("Dealer stands.")
            self.determine_winner()  # Corrected method call

    def determine_winner(self):
        dealer_hand_value = self.dealer.hand.calculate_value()
        print("\nFinal Hands:")
        print("Dealer's Hand:")
        print(", ".join(str(card) for card in self.dealer.hand.cards))
        print(f"Total value: {dealer_hand_value}")

        for player in self.players:
            player_hand_value = player.hand.calculate_value()
            print(f"\n{player.name}'s Hand:")
            print(", ".join(str(card) for card in player.hand.cards))
            print(f"Total value: {player_hand_value}")

            if player_hand_value > 21:
                print(f"{player.name} busts! Dealer wins.")
            elif dealer_hand_value > 21 or player_hand_value > dealer_hand_value:
                print(f"{player.name} wins!")
            elif player_hand_value == dealer_hand_value:
                print(f"{player.name} ties with the dealer.")
            else:
                print(f"Dealer wins against {player.name}.")

    def print_result(self):
        self.determine_winner()

if __name__ == '__main__':
    num_players = int(input("Enter the number of players: "))
    game = Game(num_players)
    game.play_game()
