class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self) -> None:
        """ Default settings of the Tv. """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
    def power(self) -> None:
        """ Turning the Tv on or off. """
        self.__status = not self.__status
    def mute(self) -> None:
        """ Toggle mute when Tv is on. """
        if self.__status:
            self.__muted = not self.__muted
    def channel_up(self) -> None:
        """ This increases the channel by 1, also loops if at max. """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                 self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1
    def channel_down(self) -> None:
        """ Decrease channel by 1, loops if at min. """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1
    def volume_up(self) -> None:
        """ Increases volume by 1. """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
    def volume_down(self) -> None:
        """ Decreases volume by 1 when volume is greater than the minimum. """
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
    def __str__(self) -> str:
        """ Return string representation of the TV. """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"

