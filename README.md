# convex-hull
Open algorithm for building the convex hull

## Installation
Tested on mac and linux (python 3.8 and python 3.9)

**NOTE**: does not work for Ubuntu 16

For linux (tested on Ubuntu 20.04) you need to install:

```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt-get install build-essential python3.<VERSION>-dev libpython3.<VERSION>-dev gcc
```

For example, for python3.9:
```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt-get install build-essential python3.9-dev libpython3.9-dev gcc
```

To use venv:
```bash
sudo apt install python3.<VERSION>-venv
python3.<VERSION> -m venv ./venv
source ./venv/bin/activate
```

Install requirements:
```bash
pip3 install -r requirements.txt
cd blist-py39
python3 setup.py install
cd ..
```

## Using Docker
You need to have Docker Engine running on your computer
```bash
docker build -t convex-hull .
docker run -it convex-hull
```
Bash terminal will appear in the project root folder. 

To edit files please use `vim` or `nano` (they are already installed).

## Usage
`python3 main.py`