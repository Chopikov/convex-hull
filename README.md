# convex-hull
Tested on python 3.8 and python 3.9
## Prerequisites
For linux (tested on Ubuntu 20.04) you need to install:

- `sudo add-apt-repository ppa:deadsnakes/ppa` - add repository with `python#.#-dev` package
- `sudo apt update`
- `sudo apt-get install build-essential python3.<VERSION>-dev libpython3.<VERSION>-dev gcc`

For example, for python3.9:
```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt-get install build-essential python3.9-dev libpython3.9-dev gcc
```

## Installation
To use venv:
- `sudo apt install python3.<VERSION>-venv`
- `python3.<VERSION> -m venv ./venv`
- `source ./venv/bin/activate`

Install requirements:
- `pip install -r requirements.txt`
- `cd blist-py39`
- `python setup.py install`

## Usage
`python main.py`