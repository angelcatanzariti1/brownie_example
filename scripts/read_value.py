from brownie import SimpleStorage, accounts, config

def read_contract():
    # Get the most recent deployment's address, taking the index that's one less than the length
    simple_storage = SimpleStorage[-1]
    print(simple_storage.retrieve())

def main():
    read_contract()