import os
from dotenv import load_dotenv, find_dotenv

# This script can only be run by importing to a IPython environment

REUPLOAD_DOTENV_COLAB = False
IN_COLAB = 'google.colab' in str(get_ipython())




if IN_COLAB:
    path = '/content/genAI-workshop'
    if not os.path.isdir(path):
        %cd '/content'
        !git clone https://github.com/bearingpoint-no/genAI-workshop
        %cd {path}
        !git pull
        print("Installing required packages")
        %pip install -r requirements_colab.txt -q
        print("Finished installing packages")

    dotenv_file = find_dotenv() or (REUPLOAD_DOTENV_COLAB and files.upload())

    if not dotenv_file:
        print("Please upload the .env file")
        dotenv_file = files.upload()

    _ = load_dotenv(dotenv_file)
elif not find_dotenv():
    raise RuntimeError("No .env file found")
