import requests
import time
import base64
import ecdsa


def wallet():
    response = None
    while response not in ["1", "2", "3"]:
        response = input("""What do you want to do?
        1. Generate new liquet wallet
        2. Send coins to another liquet wallet
        3. Check liquet transactions\n""")LIQUET COIN v1.0.0 - BLOCKCHAIN SYSTEM\n
    if response == "1":
        # Generate new wallet
        print("""=========================================\n
IMPORTANT: take note of credentials or all will be lost\n
=========================================\n""")
        generate_ECDSA_keys()
    elif response == "2":
        addr_from = input("From: introduce your liquet wallet address (public key)\n")
        private_key = input("Introduce your private liquet key\n")
        addr_to = input("To: introduce destination liquet wallet address\n")
        amount = input("Amount: number stating how much liquet do you want to send\n")
        print("=========================================\n\n")
        print("Is everything correct?\n")
        print("From: {0}\nPrivate Key: {1}\nTo: {2}\nAmount: {3}\n".format(addr_from, private_key, addr_to, amount))
        response = input("y/n\n")
        if response.lower() == "y":
            send_transaction(addr_from, private_key, addr_to, amount)
    else:
        check_transactions()


def send_transaction(addr_from, private_key, addr_to, amount):
    if len(private_key) == 64:
        signature, message = sign_ECDSA_msg(private_key)
        url = 'http://localhost:5000/txion'
        payload = {"from": addr_from,
                   "to": addr_to,
                   "amount": amount,
                   "signature": signature.decode(),
                   "message": message}
        headers = {"Content-Type": "application/json"}

        res = requests.post(url, json=payload, headers=headers)
        print(res.text)
    else:
        print("Wrong address or key length! Verify and try again.")


def check_transactions():
    res = requests.get('http://localhost:5000/blocks')
    print(res.text)


def generate_ECDSA_keys():
    """private_key: str
    public_ley: base64 (to make it shorter)
    """
    sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1) #this is your sign (private key)
    private_key = sk.to_string().hex() #convert your private key to hex
    vk = sk.get_verifying_key() #this is your verification key (public key)
    public_key = vk.to_string().hex()
    #we are going to encode the public key to make it shorter
    public_key = base64.b64encode(bytes.fromhex(public_key))

    filename = input("Write the name of your new address: ") + ".txt"
    with open(filename, "w") as f:
        f.write("Private key: {0}\nWallet address / Public key: {1}".format(private_key, public_key.decode()))
    print("Your new address and private key are now in the file {0}".format(filename))

def sign_ECDSA_msg(private_key):
    """Sign the message to be sent
    private_key: must be hex

    return
    signature: base64 (to make it shorter)
    message: str
    """
    # Get timestamp, round it, make it into a string and encode it to bytes
    message = str(round(time.time()))
    bmessage = message.encode()
    sk = ecdsa.SigningKey.from_string(bytes.fromhex(private_key), curve=ecdsa.SECP256k1)
    signature = base64.b64encode(sk.sign(bmessage))
    return signature, message


if __name__ == '__main__':
    print("""       =========================================\n
        LIQUET COIN v1.0.0 \n
       =========================================\n\n
        """)
    wallet()
    input("Press ENTER to exit")

css/style.cs
