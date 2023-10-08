import uuid

from backend.config import STARTING_BALANCE
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec


class Wallet:
    """
    An individual wallet for a miner.
    Keeps track of the miner's balance.
    Allows a miner to authorize transactions.
    """

    def __init__(self):
        self.address = str(uuid.uuid4())[0:8]
        self.private_key = ec.generate_private_key(
            ec.SECP256K1(), default_backend())
        self.public_key = ec.generate_public_key()
        
def main(): 
