import os
import sys

# Add the frontend directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'frontend'))

# Import and run the main app
from app import * 