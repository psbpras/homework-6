import os
import logging
import dotenv
from app.commands import add
from app.commands import subtract
from app.commands import multiply
from app.commands import divide

# Load environment variables
dotenv.load_dotenv()
ENV = os.getenv("ENV", "production")

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.info(f"Running in {ENV} mode")

# Command pattern dispatcher
COMMANDS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}


from app.repl import repl

if __name__ == "__main__":
    repl()
