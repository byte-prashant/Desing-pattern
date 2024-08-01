

from state import State
class BulbOffState(State):

    def change_state(self):
        from bulbOnState import BulbOnState
        print("Bulb turned on-------------------")
        self.context.setState(BulbOnState())



