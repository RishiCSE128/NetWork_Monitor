# Installation 
1. install python3 from the official website 
2. install virtual env `python -m pip install virtualenv`
3. create a virtual environment `python -m virtualenv venv`
4. activate the virtual env `source \venv\script\activate`
5. Test by the list of packeges installed `pip list`
6. Install Base packages 
    1. __paramiko__ for raw SSH communication
    2. __napalm__ advanced SSH communication for Network devices 
6. Create a requiremnt file `pip freeze --local > requirements.txt`
7. To use the requirement file `pip -r requirement.txt`

# SSH config 
1. Configure routers with SSH using `router_ssh_config.txt` script. 
2. Test ssh connectivity in powershell/terminal using `ssh admin@<management-IP>`. If key-exchege fails due to unsupported algorithm, use `ssh -c <kex-algo-name> admin@<management-IP>`