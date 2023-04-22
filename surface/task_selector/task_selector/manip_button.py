class ManipButton:
    def __init__(self, claw: str):
        self.claw: str = claw
        self.last_button_state: bool = False
        self.is_active: bool = False