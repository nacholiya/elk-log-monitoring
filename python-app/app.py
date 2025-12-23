import logging
import time
import random

# Configure logging
logging.basicConfig(
    filename="/var/log/myapp/app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s"
)

logger = logging.getLogger("my-python-app")

users = [101, 102, 103, 104]

while True:
    user = random.choice(users)
    logger.info(f"User login successful user_id={user}")

    if random.random() > 0.7:
        logger.warning("Disk usage is above threshold")

    if random.random() > 0.85:
        logger.error("Database connection failed")

    time.sleep(2)
