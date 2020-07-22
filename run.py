#!/usr/bin/env python
from website import create_app

app, debug = create_app() # default config

if __name__ == '__main__':
    app.run(debug=debug)