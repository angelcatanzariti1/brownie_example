from brownie import accounts, config, SimpleStorage
import brownie.network as network


def deploy_simple_storage():
    ## For Ganache accounts
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from":account})
    # Get stored value, calling retrieve function
    stored_value = simple_storage.retrieve()
    print("Stored value: ", stored_value)
    # Update stored value, calling store function
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print("Updated stored value: ", updated_stored_value)


    ## For accounts added with 'brownie accounts new'
    #account = accounts.load("angel-account")
    #print(account)

    ## For accounts with private keys as env variables (using .env and brownie-config.yaml)
    #account = accounts.add(config["wallets"]["from_key"])
    #print(account)

def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def main():
    deploy_simple_storage()