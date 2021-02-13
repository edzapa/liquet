# liquet
liquet is a cryptocurrency with a straighforward implementation of a blockchain all coded in python. 

### liquet-miner.py

This file is probably the most important. Running it will create a node (like a server). From here you can connect to the blockchain and process transactions (that other users send) by mining. As a reward for this work, you recieve some coins. The more nodes exist, the more secure the blockchain gets.

When run, this will create a node where you can connect the blockchain and process the transactions by mining. By doing this, you receive coins as an incentive. This in turn means that the more nodes that exist, the more secure the blockchain will get.

miner.py has 2 processes running in parallel:

1. The first process takes care of mining, updating new blockchains and finding the proof of work.
1. Does the mining and therefore updates new blockchains and finds proof-of-work

2. The second process runs the flask server where peer nodes and users can connect to ask for the entire blockchain or sumbmit new transactions.
2. This runs the flask server where peer nodes and users connect to either ask for an entire blockchain or it can submit new transactions



### liquet-wallet.py

This file is for those who don't want to be nodes but simple users. Running this file allows you to generate a new address, send coins and check your transaction history (keep in mind that if you are running this in a local server, you will need a "miner" to process your transaction).
When creating a wallet address, a new file will be generated with all your security credentials. You are supposed to keep it safe.
This file generates a new address (that is supposed to be kept safe), sends coins and checks the user's transaction history. 

More updates will come soon
