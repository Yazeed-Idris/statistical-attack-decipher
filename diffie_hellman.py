def compute_key(private_key, p=23, g=9):
    return int(pow(g, private_key, p))      # g^private_key mod p


def compute_shared_key(recieved_key, private_key, p=23):
    return int(pow(recieved_key, private_key, p))
