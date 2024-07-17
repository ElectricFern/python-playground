# Python Playground Code Snippets

## Purpose
A place to store snippets of code which I created that helped me learn python.  
Code I can refer back to, to help during problem solving.

## How To's

### How to run this code

#### Prerequisites
You have a linux machine (if on windows your commands may require amending).  
You have python3 installed.  
You have virtualenv installed.  
You have git installed.  
Additional python libraries to install (in the venv):
- pytz

#### Instructions

1. Clone this repository
```sh
git clone https://github.com/ElectricFern/python-playground.git
```
2. Create a virtual environment in the project directory
```sh
python3 -m venv .venv
```
3. Activate the virtual environment
```sh
source .venv/bin/activate
```
4. Run a snippet
```sh
python3 http_get_and_filter_json.py
```
5. If module not found when running a snippet

> ModuleNotFoundError: No module named 'pytz'
```sh
.venv/bin/pip install pytz
```