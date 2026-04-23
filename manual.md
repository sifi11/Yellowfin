# Yellowfin Usage Manual
**1.** Download or git clone the repo.

**2.** Unzip the file using your computer's default tool or a tool like 7zip.

**3.** Run the `setup.py` and give it the IP of the desired server that you want to receive the connection on(We only support port 4444 right now).

**4.** Run the server file on the server with the IP you gave the setup file.

**5.** Run the main file(I reccomend compiling it so they can't figure out your IP) in on the target's machine(make sure you have the `config.json` and the `Modules` folder with it in the folder).

**6.** It should establish a connection to the target machine.

**7.** You can also use special commands like `clip`, `screenshot`, and `sysinfo` to run the modules.

## Web Dashboard (In Progress)
To use the web dashboard, run `python3 backend.py` and naviagte in your browser to `http://localhost:8080`. 

> Do Not use VS Code Live Server or just double click the HTML file.
