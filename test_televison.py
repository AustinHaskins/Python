from television import Television


def test_init():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_power():
    tv = Television()

    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


def test_mute():
    tv = Television()

    tv.mute()
    assert tv._Television__muted is False

    tv.power()
    tv.mute()
    assert tv._Television__muted is True

    tv.mute()
    assert tv._Television__muted is False


def test_channel_up():
    tv = Television()

    tv.channel_up()
    assert "Channel = 0" in str(tv)

    tv.power()
    tv.channel_up()
    assert "Channel = 1" in str(tv)

    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert "Channel = 0" in str(tv)


def test_channel_down():
    tv = Television()

    tv.channel_down()
    assert "Channel = 0" in str(tv)

    tv.power()
    tv.channel_down()
    assert "Channel = 3" in str(tv)


def test_volume_up():
    tv = Television()

    tv.volume_up()
    assert "Volume = 0" in str(tv)

    tv.power()
    tv.volume_up()
    assert "Volume = 1" in str(tv)

    tv.mute()
    tv.volume_up()
    assert tv._Television__muted is False

    tv.volume_up()
    tv.volume_up()
    assert "Volume = 2" in str(tv)


def test_volume_down():
    tv = Television()
    tv.power()

    tv.volume_up()
    tv.volume_up()

    tv.volume_down()
    assert "Volume = 1" in str(tv)

    tv.mute()
    tv.volume_down()
    assert tv._Television__muted is False

    tv.volume_down()
    tv.volume_down()
    assert "Volume = 0" in str(tv)