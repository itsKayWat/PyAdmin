# PyAdminContext

PyAdminContext is a Python script that adds a "Run as Administrator" option to the context menu for Python files on Windows. This allows you to execute your Python scripts with elevated privileges effortlessly, enhancing your workflow and simplifying administrative tasks.

## Why PyAdminContext Was Made

Managing Python scripts that require administrative privileges can be tedious. Manually running scripts as an administrator each time disrupts your workflow. PyAdminContext streamlines this process by integrating the option directly into the Windows context menu.

## Purpose

- **Ease of Use**: Quickly run Python scripts with administrative rights without additional steps.
- **Time-Saving**: Eliminate the need to manually open PowerShell or Command Prompt as an admin.
- **Enhanced Workflow**: Improve efficiency for developers and IT professionals who frequently work with scripts requiring elevated permissions.

## How It Was Made

PyAdminContext modifies the Windows Registry to add a new option to the right-click context menu for `.py` files. When selected, it reruns the script with administrative privileges using PowerShell.

## Requirements

- **Python 3.x**: Ensure Python is installed on your system.
- **Windows OS**: This script is designed for Windows operating systems.

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/PyAdminContext.git
    ```
2. **Navigate to the Directory**
    ```bash
    cd PyAdminContext
    ```
3. **Run the Script**
    ```bash
    python add_admin_option.py
    ```

## Usage

1. **Right-Click a Python File**
   
   After installation, right-click on any `.py` file.

2. **Select "Run as Administrator"**
   
   Choose the new "Run as Administrator" option from the context menu to execute the script with elevated privileges.

## Example Use Case

**Customer Situation**: A developer needs to run a Python script that modifies system settings. Instead of manually opening an elevated Command Prompt each time, they simply right-click the script and select "Run as Administrator." This streamlines their workflow and reduces repetitive tasks.

---

## Support

If you encounter any issues or have suggestions, feel free to open an [issue](https://github.com/yourusername/PyAdminContext/issues) on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.