import platform
import subprocess

AI_VOICE_PORT = "5000"

def check_firewall():
    system = platform.system()

    if system == "Linux":
        print("Checking UFW firewall...")
        result = subprocess.getoutput("sudo ufw status")
        if AI_VOICE_PORT in result:
            print("Port already allowed ✅")
        else:
            print("Allowing AI Voice Bot Port...")
            subprocess.call(["sudo", "ufw", "allow", AI_VOICE_PORT])
            print("Port 5000 allowed 🔥")

    elif system == "Windows":
        print("Checking Windows Firewall...")
        rule_check = subprocess.getoutput("netsh advfirewall firewall show rule name=AI_VOICE_BOT")
        if "No rules match" in rule_check:
            print("Creating Firewall Rule...")
            subprocess.call([
                "netsh", "advfirewall", "firewall",
                "add", "rule",
                "name=AI_VOICE_BOT",
                "dir=in",
                "action=allow",
                "protocol=TCP",
                "localport=5000"
            ])
            print("Firewall rule added ✅")
        else:
            print("Firewall rule already exists ✅")

if __name__ == "__main__":
    check_firewall()
