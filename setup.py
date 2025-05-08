
try:
    import sys
    import os

    if sys.platform.startswith("win"):
        os.system("cls")
        print("Installing the python modules required for Ocarina Tool:\n")
        os.system("python -m pip install --upgrade pip")
        os.system("python -m pip install -r requirements.txt")
        os.system("python ROcarina.py")

    elif sys.platform.startswith("linux"):
        os.system("clear")
        print("Installing the python modules required for the Ocarina Tool:\n")
        os.system("pip3 install --upgrade pip")
        os.system("pip3 install -r requirements.txt")
        os.system("python3 Ocarina.py")

except Exception as e:
    input(e)
