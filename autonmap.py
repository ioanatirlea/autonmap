import subprocess
import os

def run_nmap_scan():
    print("=" * 40)
    print("         AUTOMATED NMAP SCANNER        ")
    print("=" * 40)
    
    target = input("Enter target IP or Domain: ").strip()
    if not target:
        print("[-] Target cannot be empty.")
        return

    print("\nSelect Scan Type:")
    print("1. Quick Scan (-F)")
    print("2. TCP SYN / Stealth Scan (-sS -T4)")
    print("3. Comprehensive Scan (-sV -sC -A)")
    print("4. Vulnerability Script Scan (--script vuln)")
    
    choice = input("\nEnter choice (1-4): ").strip()
    
    scan_types = {
        "1": ("Quick Scan", ["nmap", "-F", target]),
        "2": ("Stealth Scan", ["nmap", "-sS", "-T4", target]),
        "3": ("Comprehensive Scan", ["nmap", "-sV", "-sC", "-A", target]),
        "4": ("Vuln Script Scan", ["nmap", "-sV", "--script", "vuln", target])
    }

    if choice not in scan_types:
        print("[-] Invalid choice.")
        return

    scan_name, command = scan_types[choice]
    
    os.makedirs("results", exist_ok=True)
    output_file = f"results/{target}_{choice}.txt"
    
    print(f"\n[+] Running {scan_name} on {target}...")
    
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        
        with open(output_file, "w") as f:
            f.write(result.stdout)
            
        print(f"[+] Scan finished! Results saved to: {output_file}")
    
    except PermissionError:
        print("[-] Error: Root/Sudo privileges required for raw socket scans (e.g., -sS). Run with sudo.")
    except FileNotFoundError:
        print("[-] Error: Nmap is not installed or not in your system PATH.")
    except Exception as e:
        print(f"[-] An error occurred: {e}")

if __name__ == "__main__":
    run_nmap_scan()
