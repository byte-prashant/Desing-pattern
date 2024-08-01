from state import State
from buldOffState import BulbOffState

class BulbOnState(State):

    def change_state(self):
        print("Bulb turned off -------------------")
        self.context.setState(BulbOffState())



