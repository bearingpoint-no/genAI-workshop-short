from dotenv import load_dotenv, find_dotenv
from hackathon.paths import DOTENV_PATH
import os


def load_dotenv_file(reupload_dotenv_colab=False):
    is_in_colab = 'google.colab' in str(get_ipython())
    # PATH_REPOSITORY = "/content/genAI-workshop2"
    # PATH_LESSONS = os.path.join(PATH_REPOSITORY, "lessons")

    if is_in_colab:
        if reupload_dotenv_colab:
            dotenv_file = False
        else:
            dotenv_file = find_dotenv()

        if not dotenv_file:
            # %cd {PATH_REPOSITORY}
            print("Please upload the .env file")
            from google.colab import files
            print(DOTENV_PATH)
            files.upload_file(
                filename=DOTENV_PATH
            )
            # dotenv_file_upload = files.upload()
            # filename, _ = next(iter(dotenv_file_upload.items()))
            # os.rename(filename, ".env")
            # %cd {PATH_LESSONS}

        _ = load_dotenv(dotenv_file)
    else:
        dotenv_file = find_dotenv()
        if dotenv_file:
             _ = load_dotenv(dotenv_file)
        else:
            raise RuntimeError("No .env file found")
