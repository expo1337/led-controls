import asyncio
import argparse
import string
from bleak import BleakClient
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

address = "BE:58:A6:00:5B:C4"
uuid = "0000fff3-0000-1000-8000-00805f9b34fb"
base = "7e04013701ffff00ef"

def parse_brightness(baseValue):
    temp = hex(int(baseValue))
    return str(temp[2:])

async def changeColor (color, address):
    async with BleakClient(address) as client:
        param = bytes.fromhex("7e070503" + color + "10ef")
        model_number = await client.write_gatt_char(uuid, param)

async def changeBrightness (brightness, address):
    async with BleakClient(address) as client:
        param = bytes.fromhex("7e0401" + parse_brightness(brightness) + "01ffff00ef")
        model_number = await client.write_gatt_char(uuid, param)

async def changePower (power, address):
    async with BleakClient(address) as client:
        if power == "false":
            param = bytes.fromhex("7e0004000000ff00ef")
        elif power == "true":
            param = bytes.fromhex("7e0004f00001ff00ef")
            print('power true')
        model_number = await client.write_gatt_char(uuid, param)

@app.route('/power', methods=['POST'])
@cross_origin()
def update_power():
    power = bytes(request.get_data()).decode('utf-8')
    asyncio.run(changePower(power, address))
    return "Power-State Changed!"

@app.route('/color', methods=['POST'])
@cross_origin()
def update_color():
    color = bytes(request.get_data()).decode('utf-8')
    print(color)
    asyncio.run(changeColor(color, address))
    return "Color Changed!"

@app.route('/brightness', methods=['POST'])
@cross_origin()
def update_brightness():
    brightness = bytes(request.get_data()).decode('utf-8')
    asyncio.run(changeBrightness(brightness, address))
    return "Brightness Changed!"

@app.route('/', methods=['GET'])
def random():
    return "Hewwo"
app.run(host="0.0.0.0")
