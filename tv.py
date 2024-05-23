# Create a class
class TV:
    # Create constructor
    def __init__(self):
        # Instance Variable
        self.channel = 1
        self.volume_level = 1
        self.is_on = False

    # Create the turn on method
    def turn_on(self):
        self.is_on = True

    # Create the turnoff method
    def turn_off(self):
        self.is_on = False

    # Set the channel
    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        if 1 <= channel <= 120:
            self.channel = channel

    # Get the volume
    # Channel up
    # Channel down
    # Volume up
    # Volume down
