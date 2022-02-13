from brownie import accounts, config, SimpleStorage


def deploy_simple_storage():
    ## For Ganache accounts
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from":account})
    print(simple_storage)

    ## For accounts added with 'brownie accounts new'
    #account = accounts.load("angel-account")
    #print(account)

    ## For accounts with private keys as env variables (using .env and brownie-config.yaml)
    #account = accounts.add(config["wallets"]["from_key"])
    #print(account)

def main():
    deploy_simple_storage()