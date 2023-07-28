import asyncio
import argparse
import string
from bleak import BleakClient

parser = argparse.ArgumentParser(description="LED Control Script for ELK-BLEDOM")
parser.add_argument("--value", type=str, help="Value")
parser.add_argument("--use", type=str, help="Use: color, power, brightness")
args = parser.parse_args()

address = "BE:58:A6:00:5B:C4"
uuid = "0000fff3-0000-1000-8000-00805f9b34fb"
base = "7e04013701ffff00ef"

def parse_brightness(baseValue):
    temp = hex(int(baseValue))
    return str(temp[2:])


if args.use == "color":
    base = "7e070503" + args.value + "10ef"
elif args.use == "brightness":
    base = "7e0401" + parse_brightness(args.value) + "01ffff00ef"
elif args.use == "power":
    if args.value == "true":
        base = "7e0004f00001ff00ef"
    elif args.value == "false":
        base = "7e0004000000ff00ef"

async def main (address):
    async with BleakClient(address) as client:
        param = bytes.fromhex(base)
        model_number = await client.write_gatt_char(uuid, param)

asyncio.run(main(address))

