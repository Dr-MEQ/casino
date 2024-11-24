class GameState:
    def __init__(self):
        self.state = {
            # Application flow control
            'current_screen': 'casino_entrance',

            # Display text elements
            'header': '',
            'status_message': '',

            # Card states
            'player_cards': [],
            'banker_cards': [],

            # Game financial state   
            'bank_value': 100,
            'player_funds': 1000,
        }
    
    def get_state(self):
        return self.state
    
    def reset_game_state(self):
        persistent_funds = self.state['player_funds']
        self.state = {
            'current_screen': 'casino_entrance',
            'header': '',
            'status_message': '',
            'player_cards': [],
            'banker_cards': [],
            'bank_value': 100,
            'player_funds': persistent_funds,
        }

    def update_state(self, new_state):
        self.state.update(new_state)
        return self.state
    
    def update_funds(self, amount):
        self.state['player_funds'] += amount
        return self.state['player_funds']
    
    def update_bank(self, amount):
        self.state['bank_value'] += amount
        return self.state['bank_value']
    
    def update_cards(self, player_cards, banker_cards):
        self.state['player_cards'] = player_cards
        self.state['banker_cards'] = banker_cards
        return self.state
    
    def update_winner(self, winner):
        self.state['winner'] = winner
        return self.state
    
    def update_status_message(self, message):
        self.state['status_message'] = message
        return self.state
    
    def update_header(self, header):
        self.state['header'] = header
        return self.state
    
    def update_current_screen(self, screen):
        self.state['current_screen'] = screen
        return self.state
    
    def update_deck(self, deck):
        self.state['deck'] = deck
        return self.state
    
    