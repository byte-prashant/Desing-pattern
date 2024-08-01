from __future__ import annotations
from abc import ABC, abstractmethod
from state import State
# the context class contains a _state that references the concrete state and setState method to change between states.
class Button:

    _state = None

    def __init__(self, state: State) -> None:
        self.setState(state)

    def setState(self, state: State):

        print(f"Context: Transitioning to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def press_button(self):
        self._state.change_state()