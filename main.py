import asyncio
from bleak import BleakClient

address = "BE:58:A6:00:5B:C4"

async def main (address):
    async with BleakClient(address) as client:
        param = bytes.fromhex("7e04016401ffff00ef")
        model_number = await client.write_gatt_char("0000fff3-0000-1000-8000-00805f9b34fb", param)

asyncio.run(main(address))
