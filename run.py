# run.py

import argparse

from src import start

parser = argparse.ArgumentParser()
parser.add_argument('--env', required=True)
args = parser.parse_args()

config_name = args.env
app = start(config_name)

if __name__ == '__main__':
    app.run()