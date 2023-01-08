# get_form_with_fastapi
FastAPI validation service

## Instruction for installation
### Install with local python
1. Use python 3.10
2. `git clone https://github.com/alexfomin1/get_form_with_fastapi.git`
3. `cd get_form_with_fastapi`
4. `pip install -e .`
5. `cd app`
6. `python main.py` -- to start server
7. `python test_your_request.py` -- to test your own request
8. `python test_requests.py` -- to test built-in requests

## Install with docker
!!! BUT you need to install `aiohttp asyncio` locally to run test requests files !!!

----- docker
1. Install docker
2. `git clone https://github.com/alexfomin1/get_form_with_fastapi.git`
3. `cd get_form_with_fastapi`
4. `docker build -t check_form .`
5. `docker run --name check_form_c -p 8000:8000 check_form`
----- locally
6. `cd app`
7. `pip install asyncio aiohttp`
8. `python test_your_request.py` -- to test your own request
9. `python test_requests.py` -- to test built-in requests

## Description
Elements of the project:
- FastAPI
- Docker
- aiohttp
- tinyDB

This project checks your POST-requests via pydantic and returns the pattern of the model

## Structure
.
├── Dockerfile
├── README.md
├── app
│   ├── __init__.py
│   ├── db.json -- database for tinyDB
│   ├── main.py -- FastAPI server
│   ├── test_requests.py -- built-in requests
│   └── test_your_request.py -- your own requests
├── db.json
├── poetry.lock
└── pyproject.toml