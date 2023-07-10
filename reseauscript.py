import wmi

input("Appuyez sur Entrée pour continuer...")

def check_network_status():
    # Vérifier l'état du réseau
    c = wmi.WMI()
    network_interface = c.Win32_NetworkAdapter(NetConnectionID="Ethernet")
    
    if network_interface[0].NetEnabled:
        print("Le réseau est activé.")
    else:
        print("Le réseau est désactivé.")

def disable_network():
    # Désactiver le réseau
    c = wmi.WMI()
    network_interface = c.Win32_NetworkAdapter(NetConnectionID="Ethernet")
    
    if network_interface[0].NetEnabled:
        network_interface[0].Disable()
        print("Le réseau a été désactivé.")
    else:
        print("Le réseau est déjà désactivé.")

def enable_network():
    # Activer le réseau
    c = wmi.WMI()
    network_interface = c.Win32_NetworkAdapter(NetConnectionID="Ethernet")
    
    if not network_interface[0].NetEnabled:
        network_interface[0].Enable()
        print("Le réseau a été activé.")
    else:
        print("Le réseau est déjà activé.")

# Boucle principale du programme
while True:
    print("1. Vérifier l'état du réseau")
    print("2. Désactiver le réseau")
    print("3. Activer le réseau")
    print("4. Sortir")

    choice = input("Choisissez une option : ")
    
    if choice == "1":
        check_network_status()
    elif choice == "2":
        disable_network()
    elif choice == "3":
        enable_network()
    elif choice == "4":
        break
    else:
        print("Option invalide. Veuillez réessayer.")
