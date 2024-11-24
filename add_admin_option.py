import winreg
import os
import sys
import ctypes
import subprocess

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    """Re-run the script with admin privileges"""
    script_path = os.path.abspath(__file__)
    try:
        if sys.argv[-1] != 'asadmin':
            subprocess.run(['powershell', 'Start-Process', 'python', f'"{script_path}"', 'asadmin', '-Verb', 'RunAs'])
            return True
    except Exception as e:
        print(f"Error elevating privileges: {e}")
    return False

def fix_registry():
    try:
        # Add Python to right-click menu
        python_cmd = sys.executable
        
        # For .py files
        key_path = r"Python.File\shell\runasadmin"
        with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, key_path) as key:
            winreg.SetValueEx(key, "", 0, winreg.REG_SZ, "Run as &administrator")
            winreg.SetValueEx(key, "HasLUAShield", 0, winreg.REG_SZ, "")
        
        # Add command
        cmd_path = key_path + r"\command"
        with winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, cmd_path) as key:
            command = f'"{python_cmd}" "%1" %*'
            winreg.SetValueEx(key, "", 0, winreg.REG_SZ, command)
        
        print("Successfully added 'Run as administrator' option!")
        return True
    except Exception as e:
        print(f"Error modifying registry: {e}")
        return False

def main():
    print("Checking privileges...")
    
    if not is_admin():
        print("Requesting administrative privileges...")
        if run_as_admin():
            print("Please respond to the UAC prompt...")
            return
        else:
            print("Failed to get admin privileges.")
            print("\nTry this instead:")
            print("1. Press Win + X")
            print("2. Select 'Windows PowerShell (Admin)' or 'Command Prompt (Admin)'")
            print("3. Navigate to this script's location:")
            print(f"   cd {os.path.dirname(os.path.abspath(__file__))}")
            print("4. Run:")
            print("   python add_admin_option.py")
    else:
        print("Running with admin privileges...")
        if fix_registry():
            print("\nSuccess! You should now see 'Run as administrator'")
            print("when right-clicking Python files.")
        else:
            print("\nFailed to modify registry settings.")
    
    print("\nPress Enter to exit...")
    input()

if __name__ == "__main__":
    main()