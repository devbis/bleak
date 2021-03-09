import logging
import uuid
from typing import Callable, Union

from bluepy.btle import Peripheral

from ..characteristic import BleakGATTCharacteristic
from ..client import BaseBleakClient
from ..device import BLEDevice
from ..service import BleakGATTServiceCollection

logger = logging.getLogger(__name__)


class QueuePeripheral(Peripheral):
    # add async code
    pass


class BleakClientBluePy(BaseBleakClient):

    def __init__(self, address_or_ble_device: Union[BLEDevice, str], **kwargs):
        super().__init__(address_or_ble_device, **kwargs)
        self._address_type = (
            kwargs["address_type"]
            if "address_type" in kwargs
            and kwargs["address_type"] in ("public", "random")
            else None
        )

        self.peripheral = None

    async def stop_notify(self, char_specifier: Union[
            BleakGATTCharacteristic, int, str, uuid.UUID]) -> None:
        pass

    async def start_notify(
            self,
            char_specifier: Union[BleakGATTCharacteristic, int, str, uuid.UUID],
            callback: Callable[[int, bytearray], None],
            **kwargs) -> None:
        pass

    async def write_gatt_descriptor(self, handle: int, data: bytearray) -> None:
        pass

    async def write_gatt_char(
            self,
            char_specifier: Union[BleakGATTCharacteristic, int, str, uuid.UUID],
            data: bytearray,
            response: bool = False) -> None:
        pass

    async def read_gatt_descriptor(self, handle: int, **kwargs) -> bytearray:
        pass

    async def read_gatt_char(
            self,
            char_specifier: Union[BleakGATTCharacteristic, int, str, uuid.UUID],
            **kwargs) -> bytearray:
        pass

    async def get_services(self, **kwargs) -> BleakGATTServiceCollection:
        pass

    async def unpair(self) -> bool:
        pass

    async def pair(self, *args, **kwargs) -> bool:
        pass

    async def disconnect(self) -> bool:
        pass

    async def is_connected(self) -> bool:
        pass

    async def connect(self, **kwargs) -> bool:
        self.peripheral = QueuePeripheral(self.address, self._address_type)
