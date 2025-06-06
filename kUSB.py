print("Demarrage 'USB.py'")
from DATA import *


def get_device_ids(device_name):
    if device_name == 'keyboard':
        device_name=config.name_keyboard
    else:
        device_name=config.name_scan
    try:
        # Exécuter la commande xinput list
        result = subprocess.run(['xinput', 'list'], capture_output=True, text=True, check=True)
        # Filtrer la sortie pour obtenir les IDs des périphériques
        lines = result.stdout.split('\n')
        device_ids = []
        for line in lines:
            if device_name in line:
                # Utiliser split pour extraire l'ID du périphérique
                parts = line.split('id=')
                if len(parts) > 1:
                    id_part = parts[1]
                    device_id = id_part.split()[0]
                    device_ids.append(device_id)
        return device_ids
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        return []


def command_usb(usb,type):
    ids=get_device_ids(usb)
    if id==None or len(ids)==0:
        return False
    for i in ids:
        command = f'xinput {type} {i}'
        os.system(command)
    return True
