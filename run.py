from app import app
from helpers.db_helpers import *
import sys

if len(sys.argv) > 1:
    mode = sys.argv[1]
else:
    print('Missing required arguments')
    exit

if mode == 'testing':
    from flask_cors import CORS
    CORS(app)
    app.run(debug=True)
elif mode == 'production':
    import bjoern
    bjoern.run(app, '0.0.0.0', 5005)
else :
    print('Mode must be in testing/production')
    exit()