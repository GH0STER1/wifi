import subprocess
import random
import time

def check_hosted_network_support():
    result = subprocess.run("netsh wlan show drivers", shell=True, capture_output=True, text=True)
    if "Hosted network supported" in result.stdout and "Yes" in result.stdout:
        print("Your device supports hosted networks.")
    else:
        print("Hosted network is not supported by your device.")
        exit()

def start_wifi_network(ssid, password):
    command = f'netsh wlan set hostednetwork mode=allow ssid="{ssid}" key={password}'
    subprocess.run(command, shell=True)
    subprocess.run("netsh wlan start hostednetwork", shell=True)
    print(f"Zombie Network '{ssid}' started with password: {password}")

def stop_wifi_network():
    subprocess.run("netsh wlan stop hostednetwork", shell=True)
    print("Zombie Network stopped.")

def generate_ssid():
    return f"Swaggy_{random.randint(1, 10000)}"

def generate_password():
    symbols = "!@#$%^&*()_-+=<>?~"
    password = ''.join(random.choice(symbols) for i in range(12))
    return password

def main():
    check_hosted_network_support()

    while True:
        ssid = generate_ssid()
        password = generate_password()
        start_wifi_network(ssid, password)

        print(f"Zombie Network '{ssid}' with password '{password}' is live!")
        
        time.sleep(30)
        stop_wifi_network()

        print("Waiting for next zombie network...\n")
        time.sleep(5)

if __name__ == "__main__":
    main()
