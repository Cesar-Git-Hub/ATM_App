import logging

logging.basicConfig(
    filename="atm.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_action(action: str):
    logging.info(action)
