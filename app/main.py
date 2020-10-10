from flask import Flask
from dotenv import load_dotenv

load_dotenv(".env")

app = Flask(__name__)
