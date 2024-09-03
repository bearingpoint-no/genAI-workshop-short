import os
from dotenv import load_dotenv, find_dotenv


def say_hello():
    print("hello")


# This function can only be run by importing to a IPython environment


def load_dotenv_file(reupload_dotenv_colab=False):
    in_colab = 'google.colab' in str(get_ipython())
    PATH_REPOSITORY = "/content/genaiworkshop2"
    PATH_LESSONS = os.path.join(PATH_REPOSITORY, "lessons")

    if in_colab:
        dotenv_file = find_dotenv() or (reupload_dotenv_colab and files.upload())

        if not dotenv_file:
            print("Please upload the .env file")
            from google.colab import files
            %cd {PATH_REPOSITORY}
            dotenv_file = files.upload()
            os.rename(dotenv_file, os.path.join(PATH_REPOSITORY, "hei.env"))
            %cd {PATH_LESSONS}

        _ = load_dotenv(dotenv_file)
    else:
        dotenv_file = find_dotenv()
        if dotenv_file:
             _ = load_dotenv(dotenv_file)
        else:
            raise RuntimeError("No .env file found")