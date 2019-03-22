from wireless.bluetooth.sender_blue_tooth_fake import SenderBlueToothFake
from wireless.modem.sender_modem_fake import SenderModemFake
from wireless.sender import Sender


_BLUE_TOOTH_MAX_DISTANCE: int = 50


def sender_factory_impl(distance: int) -> Sender:
    if distance > _BLUE_TOOTH_MAX_DISTANCE:
        return SenderBlueToothFake()
    else:
        return SenderModemFake()
