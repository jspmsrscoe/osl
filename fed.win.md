### 11) File Transfer

---

#### A) Fedora to Fedora using `scp` (Secure Copy)

The standard and most secure way to transfer files between Linux systems is using `scp` (Secure Copy Protocol). It leverages SSH (Secure Shell) to encrypt the file and the connection, ensuring data is transferred safely.

**Prerequisites:**

1.  **Two Fedora machines:** Let's call them `Fedora-A` (the source) and `Fedora-B` (the destination). They must be on the same network.
2.  **SSH Server on Destination:** The destination machine (`Fedora-B`) must have an SSH server running so it can accept incoming connections.
    - To install it, run: `sudo dnf install openssh-server`
    - To enable and start it, run: `sudo systemctl enable sshd` and `sudo systemctl start sshd`
3.  **IP Address of Destination:** You need to know the IP address of `Fedora-B`. On `Fedora-B`, open a terminal and type `ip a` to find it (e.g., `192.168.1.55`).
4.  **User Account on Destination:** You need the username and password for an account on `Fedora-B`.

**Steps to Transfer a File:**

Let's say on `Fedora-A`, you are logged in as the user `userA` and you have a file named `report.txt` in your home directory (`/home/userA/report.txt`). You want to copy this file to the home directory of `userB` on `Fedora-B`.

1.  **Open a Terminal on the source machine (`Fedora-A`).**

2.  **Use the `scp` command with the following syntax:**

    ```bash
    scp [options] /path/to/source/file username@destination_ip:/path/to/destination/
    ```

3.  **Execute the command:**

    ```bash
    scp /home/userA/report.txt userB@192.168.1.55:/home/userB/
    ```

4.  **Enter the Password:**
    - You will be prompted to enter the password for `userB` on `Fedora-B`.
    - If this is the first time you are connecting, you might be asked to verify the authenticity of the host's key. Type `yes` and press Enter.

5.  **Verification:**
    - Once the command completes, the file `report.txt` will be in the `/home/userB/` directory on `Fedora-B`. You can log into `Fedora-B` and use the `ls` command to confirm it's there.

**To copy an entire directory**, use the `-r` (recursive) flag:

```bash
scp -r /home/userA/MyProject/ userB@192.168.1.55:/home/userB/
```

---

#### B) Windows to Windows using File Sharing (SMB)

Windows uses the SMB (Server Message Block) protocol for its built-in File Sharing. This is the familiar "shared folder" functionality that most Windows users have seen.

**Prerequisites:**

1.  **Two Windows machines:** Let's call them `Windows-A` (source) and `Windows-B` (destination), connected to the same network.
2.  **Network Discovery and File Sharing Enabled:** On both machines, go to `Control Panel` -> `Network and Sharing Center` -> `Change advanced sharing settings`. Ensure that for your current network profile (Private, Guest, or Public), "Network discovery" and "File and printer sharing" are turned **on**.

**Steps to Share and Access Files:**

**On the Source Machine (`Windows-A`):**

1.  **Create a Folder and a File:**
    - On your Desktop or in your Documents, create a new folder. Let's name it `SharedDocs`.
    - Inside this folder, create a simple text file named `testfile.txt`.

2.  **Share the Folder:**
    - Right-click the `SharedDocs` folder and select **Properties**.
    - Go to the **Sharing** tab.
    - Click the **"Share..."** button.
    - From the dropdown menu, choose `Everyone` and click **Add**.
    - By default, `Everyone` will have "Read" permission. You can change this to "Read/Write" if you want the other user to be able to modify files.
    - Click **Share**, then **Done**.

3.  **Find the IP Address of `Windows-A`:**
    - Open the Command Prompt (`cmd`).
    - Type `ipconfig` and press Enter.
    - Look for the "IPv4 Address" line (e.g., `192.168.1.60`). Note this down.

**On the Destination Machine (`Windows-B`):**

1.  **Access the Shared Folder:**
    - Press the `Windows Key + R` to open the "Run" dialog box.
    - Type two backslashes `\\` followed by the IP address of `Windows-A`.
    - Example: `\\192.168.1.60`
    - Press **Enter**.

2.  **View the Files:**
    - A window will open showing all the shared folders on `Windows-A`, including `SharedDocs`.
    - Double-click the `SharedDocs` folder. You will see `testfile.txt` inside.

3.  **Transfer the File:**
    - You can now simply drag and drop `testfile.txt` from the network folder to your desktop on `Windows-B`. You have successfully transferred the file.

This method is very intuitive for graphical user interfaces and is the standard for file sharing in a Windows environment.
