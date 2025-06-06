import time
import random
import sys
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def fake_typing(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def fake_progress(task, duration=3):
    sys.stdout.write(f"{task}\n")
    sys.stdout.flush()
    steps = 20
    for i in range(steps + 1):
        percent = int((i / steps) * 100)
        bar = '=' * i + ' ' * (steps - i)
        sys.stdout.write(f"\r[{bar}] {percent}%")
        sys.stdout.flush()
        time.sleep(duration / steps)
    print()

def ascii_art():
    print("        WiFi Hacking Utility v1.20.25.21.1\n")

def scan_networks():
    fake_typing("Scanning for nearby WiFi networks...")
    fake_progress("Scanning", 2)
    networks = [
        {"SSID": "Home_WiFi", "Signal": "Strong"},
        {"SSID": "shyam_Shop", "Signal": "Medium"},
        {"SSID": "keshav_5G", "Signal": "Weak"},
        {"SSID": "hackit_WiFi", "Signal": "Medium"},
        {"SSID": "Tenda1249", "Signal": "Strong"}
    ]
    print("\nAvailable Networks:")
    for idx, net in enumerate(networks, 1):
        print(f"  {idx}. {net['SSID']} ({net['Signal']})")
    return networks

def select_network(networks):
    fake_typing("\nSelect a network to target (1-5): ", 0.02)
    choice = input()
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(networks):
            return networks[idx]
    except:
        pass
    fake_typing("Invalid choice. Defaulting to 1.")
    return networks[0]

def handshake_capture(ssid):
    fake_typing(f"\n[*] Setting interface wlan0 to monitor mode...")
    fake_progress("Enabling monitor mode", 2)
    fake_typing(f"[*] Listening for handshake packets on SSID: {ssid} ...")
    fake_progress("Capturing handshake", 3)
    fake_typing("[*] WPA2 handshake captured successfully!\n")

def crack_password(ssid):
    fake_typing(f"[*] Initiating dictionary attack on {ssid} ...")
    steps = 30
    sys.stdout.write("Cracking password: \n")
    sys.stdout.flush()
    for i in range(steps + 1):
        percent = int((i / steps) * 100)
        bar = '=' * i + ' ' * (steps - i)
        sys.stdout.write(f"\r[{bar}] {percent}%")
        sys.stdout.flush()
        time.sleep(0.15)
    print()
    fake_typing(f"\n[+] Password found: ********")
    fake_typing("[*] Connecting to network...")
    fake_progress("Connecting", 2)
    fake_typing("[+] Connected successfully!\n")

def show_tools():
    tools = [
        ("Nmap", "Scanning devices on the network..."),
        ("Hydra", "Brute-forcing router admin panel..."),
        ("SQLMap", "Checking for SQL vulnerabilities..."),
        ("TheHarvester", "Gathering emails from network..."),
        ("WiFi Users", "Listing connected devices...")
    ]
    for name, desc in tools:
        fake_typing(f"{name} - {desc}")
        fake_progress("Running", 1.5)
        time.sleep(0.3)
    fake_typing("\nAll tools completed.\n")

def main():
    clear()
    ascii_art()
    networks = scan_networks()
    selected = select_network(networks)
    clear()
    ascii_art()
    fake_typing(f"Targeting network: {selected['SSID']}\n")
    handshake_capture(selected['SSID'])
    crack_password(selected['SSID'])
    show_tools()
    fake_typing("you can not be a hacker by copying my code.")
    input()

if __name__ == "__main__":
    main()