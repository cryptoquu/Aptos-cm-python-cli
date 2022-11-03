from pick import pick
import create_candy_machine
import util
import constants
from candy_machine import CandyMachine

if __name__ == "__main__":
    title = 'Please choose what you want to do: '
    options = [
        'Create candy machine', 
        "Retry failed uploads",
        'Update WL for existing collection',
        'Update public mint time',
        'Update presale mint time',
        'Update mint fee per mille',
        'Mint',
        'Token count in wallet',]
    option, index = pick(options, title)
    if index == 0 :
        candy_machine = CandyMachine(constants.MODE, constants.BATCH_NUMBER)
        candy_machine.create()
    elif index == 1:
        candy_machine = CandyMachine(constants.MODE, constants.BATCH_NUMBER)
        candy_machine.retryFailedUploads()
    elif index == 2:
        util.update_whitelist()
    elif index == 3:
        util.update_public_mint_time()
    elif index  == 4:
        util.update_presale_mint_time()
    elif index == 5:
        util.update_mint_fee()
    elif index == 6:
        suboptions = [
            'Mint 1',
            'Mint 10',
            'Mint 100'
        ]

        _, subIndex = pick(suboptions, 'How many?')

        if subIndex == 0:
            util.mint(num_mints = 1, amount_per_mint = 1)
        elif subIndex == 1:
            util.mint(num_mints = 2, amount_per_mint = 5)
        else:
            util.mint(num_mints = 20, amount_per_mint = 5)
    elif index == 7:
        util.printOwnedCount() # todo