

class Television:
    MIN_VOlUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self):
        self.status = False
        self.muted = False
        self.volume = 0
        self.channel = 0
    def power(self):
        pass
    def mute(self):
        pass
    def channel_up(self):
        pass
    def channel_down(self):
        pass
    def volume_up(self):
        pass
    def volume_down(self):
        pass
    def __str__(self):
        pass

