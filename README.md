# apik-thief
A small script to automate finding unprotected API keys, supports Google Maps only for now.

**Disclaimer:** This script is provided "AS IS", without any warranties and should be used at your own risk.

## Getting Started

```git clone``` this repository

```
git clone https://github.com/Yiidiir/apik-thief.git && cd apik-thief
```

```pip install``` requirements

```
pip install -r requirements.txt
```
Rename `.env.example` to `.env` and set `SHODAN_API` to your [Shodan.io API Key](https://account.shodan.io/)
```
mv .env.example .env
```
```
SHODAN_API=myApiKeysfdgfhgjhkdfxg
```

## Usage

```
usage: apik.py [-h] [-s {googleMaps}]

optional arguments:
  -h, --help            show this help message and exit
  -s {googleMaps}, --service {googleMaps}
                        Specify what service to look for
```

### Example

The only existing input is a boolean declaring whenever writing should be allowed or not:

```
python apik.py --service googleMaps
```
If any unprotected Google Maps API keys are spotted, you'll find them appended in `maps_keys.txt`

### TODO:
- [ ] Support more services
- [ ] Add to PyPi

Licensed under the MIT License
