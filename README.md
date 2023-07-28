## Led-Controls


# Custom CLI tool for controlling ELK-BLEDOM Led strips

[How](#how)
[Setup](#setup)
[Options](#options)

## How?

This tool was made by reverse engineering the "Lotus Lantern" App.
I used wireshark to dump all of the bluetooth commands 

## Setup

To clone and run this application, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/) (which comes with [pip](https://pypi.org/project/pip/)) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/expo1337/led-controls

# Go into the repository
$ cd led-controls

# Install dependencies
$ pip install bleak asyncio

# Run the app
$ python ./main.py --options....
```

## Options

* --use
  - Defines the script usage
  - Options: color, brightness, power
* --value
  - Defines the value for the use option 
  - Color: 6 Digit Color HEX Code
  - Brightness: Value between 0 and 100
  - Power: true or false