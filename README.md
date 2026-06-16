# Brave Origin Patcher Utilities
![Alt Text](SmallLogo.png)


This repo contains two simple utilities designed for Windows 10/11 and macOS that allows you to get Brave Origin for free, telling Brave Origin that you purchased the product, even if you didn't!

**Feel free to report issues using the Github Issues!**


## Features: 
* No prerequsite software or manual file editing.
* Easy apply, easy revert with simple GUI.
* Works with Brave Origin, Brave Origin Beta and Brave Origin Nightly.
* Windows **and** MacOS versions.


## Usage:

1. Download the latest release from the releases section relevent to your OS.
2. Download and install Brave Origin. After installing, close the purchase dialog.
3. Follow OS-specific instructions:


### **Windows:**
 * Double-click on the executable.
 * Select the version(s) you want patched.
 * It'll patch Brave Origin and print a success/fail.
### **MacOS:**
  * Open and expand the ZIP Archive.
  * Double click on the Brave Origin Unlocker. Note: If it says that "Apple could not verify that is app is free from malware", then disable Gatekeeper.
    * To disable Gatekeeper, first type in terminal `sudo spctl --master-disable`.
    * Then go to Settings -> Privacy and Security -> Allow applications from (Anywhere).

   
   <img width="744" height="644" alt="image" src="https://github.com/user-attachments/assets/dc1ff67d-f1a9-42a3-99a8-ae51c263c5db" />
   
   * Then, for security purposes, you may run `sudo spctl --master-enable` to enable Gatekeeper.



## Screenshots:
### **Windows:**

<img width="636" height="470" alt="image" src="https://github.com/user-attachments/assets/f7b3d37b-76ae-4943-bdc6-b9a3045eb5f3" />

### **MacOS:**

<img width="472" height="223" alt="image" src="https://github.com/user-attachments/assets/ee063e0a-78f0-4c45-ac8a-3837ba9c7ed0" />

## Building: 
* The Windows Python script was built using auto-py-to-exe, however, you can choose to compile however you like, or run the .py directly.
* The MacOS version was created using native Apple scripts, compiled in a single package. If you wish, you can view the source in the repository. 


## Credits:

* [**@RouterCFW**](https://github.com/routercfw) for the MacOS build.
* [**@winui64**](https://github.com/winui64) for the Windows build.
