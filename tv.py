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
    def get_volume(self):
        return self.volume_level

    def set_volume(self, volume_level):
        if 1 <= volume_level <= 7:
            self.volume_level = volume_level

    # Channel up
    def channel_up(self):
        if self.channel <= 120:
            self.channel += 1
    # Channel down
    # Volume up
    # Volume down
