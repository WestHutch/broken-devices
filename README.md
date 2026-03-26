## broken-devices
> Python script that automates broken device workflows in a school district, including reporting, email notifications, inventory updates, and repair requests.

This is only to be used by THS/TMS techs to automate the process when receiving a broken MacBook. This script prompts the user for information regarding the broken device, then uses playwright to automate the reporting, check-in, and repair order processes.

## Installation & Setup

  1. Ensure python is installed on your machine
  2. Ensure your label printer is set as your default printer
  3. Download this repo and save it to your desktop

## First Use

  1. In the command prompt, naviate to where you have this repo saved

  ```
  cd Desktop\broken_devices-main
  ```

  2. Run the following commands sequentially. This will ensure you have all necessary packages installed

  ```
  py -m venv venv
  venv\Scripts\activate.bat
  pip install -r requirements.txt
  ```

### pip not recognized as a command
If pip is not being recognized as a command, you may need to add a couple paths to your system's PATH environment variable  
  * Search for "environment variables" in the Windows search bar and open the first result
  * Click Environment Variables, and select the Path variable under User Variables
  * Click New and add the path to your Python installation (ex: C:\Users\yourname\AppData\Local\Programs\Python\Python313)
  * Also add the path to the Scripts folder within your Python installation (ex: C:\Users\yourname\AppData\Local\Programs\Python\Python313\Scripts)
  * You can then restart command prompt and type the following to ensure pip is working

    ```
    pip --version
    ```

### Execution of scripts is disabled
If your system is blocking the execution of the venv exe, you'll need to do the following:
  * Open Windows Security, and go to Virus & threat protection
  * Click "Manage settings" under Virus & threat protection settings
  * Under Exclusions, click "Add or remove exclusions"
  * Add the path to your Python folder (ex: C:\Users\yourname\AppData\Local\Programs\Python)
  * Add the path to the project folder (ex: C:\Users\yourname\Desktop\broken_devices)
       
If it's your first time using playwright, you'll also need to run the following:

  ```
  playwright install
  ```

  3. Run the main script

  ```
  py broken_device_script.py
  ```

  4. Upon first running the program, you will be prompted to enter your credentials for each step. After that, the program will never ask you again. If you entered these incorrectly, you can simply edit them in the userinfo.txt file that was created, or delete this file to be prompted again the next run.

  ## Subsequent Uses

  After your first successful use of the program, you can run it again by doing the following:

  1. In the terminal, navigate to this repo

  ```
  cd Desktop\broken_devices-main
  ```

  2. Start the virtual environment

  ```
  venv\Scripts\activate.bat
  ```

  3. Run the script

  ```
  py broken_device_script.py
  ```
