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