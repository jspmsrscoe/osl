### 1) Installation of Cisco Packet Tracer on Windows and Fedora

Here's a step-by-step guide to installing Cisco Packet Tracer on both Windows and Fedora operating systems.

#### On Windows:

The installation of Cisco Packet Tracer on Windows is a straightforward process that involves downloading the official installer and following the setup wizard.

**Step 1: Download the Installer**

1.  To download Cisco Packet Tracer, you need a Cisco Networking Academy (NetAcad) account. If you don't have one, you can register for free.
2.  Log in to the Cisco NetAcad website.
3.  Navigate to the "Resources" section and select "Packet Tracer" to access the download page.
4.  Choose the Windows version that matches your system architecture (32-bit or 64-bit) and download the executable file (.exe).

**Step 2: Run the Installer**

1.  Once the download is complete, locate the installer file in your downloads folder.
2.  Double-click the installer file to launch the setup wizard.
3.  You will be prompted to accept the license agreement. Read it and click "I accept the agreement" to proceed.

**Step 3: Follow the Setup Wizard**

1.  **Choose Installation Location:** You can either accept the default installation directory or specify a different one.
2.  **Select Start Menu Folder:** Decide where you want the program's shortcuts to be created in the Start Menu.
3.  **Select Additional Tasks:** You will have the option to create a desktop icon for easy access.
4.  **Install:** Review your installation settings and click "Install" to begin the process.
5.  **Finish:** Once the installation is complete, you can choose to launch Cisco Packet Tracer immediately by checking the corresponding box and clicking "Finish".

**Step 4: Log in**

1.  The first time you launch Packet Tracer, you will be prompted to log in with your Cisco NetAcad credentials. This is required to use the full functionality of the software.

#### On Fedora:

Installing Cisco Packet Tracer on Fedora requires a few more steps as there isn't a direct installer for this Linux distribution. The process generally involves downloading the Debian (`.deb`) package and using a script to convert and install it.

**Step 1: Download the Debian Package**

1.  Log in to your Cisco Networking Academy account.
2.  Navigate to the Packet Tracer resources and download the `.deb` file for Ubuntu.

**Step 2: Use an Installation Script**

A community-created script is available on GitHub to facilitate the installation of Packet Tracer on Fedora.

1.  **Open a terminal.**
2.  **Install Git (if you don't have it):**
    ```bash
    sudo dnf install git
    ```
3.  **Clone the repository:**
    ```bash
    git clone https://github.com/thiagoojack/packettracer-fedora
    ```
4.  **Navigate to the cloned directory:**
    ```bash
    cd packettracer-fedora
    ```
5.  **Move the downloaded `.deb` file into this directory.**
6.  **Make the setup script executable:**
    ```bash
    chmod +x setup.sh
    ```
7.  **Run the installation script:**
    ```bash
    sudo ./setup.sh
    ```

This script will automatically handle the necessary dependencies, extract the files from the `.deb` package, and install Cisco Packet Tracer in the `/opt` directory. It will also create a desktop entry so you can launch it from your applications menu.

After the installation, you can launch Cisco Packet Tracer and log in with your NetAcad account to start using the simulation tool.
