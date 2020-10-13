from flask import Flask
from src.app import main

http_server = main(Flask)
