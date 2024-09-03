from dotenv import load_dotenv, find_dotenv
from hackathon.paths import DOTENV_PATH


def load_dotenv_file(reupload_dotenv_colab=False):
    is_in_colab = 'google.colab' in str(get_ipython())  # noqa F821

    if is_in_colab:
        if reupload_dotenv_colab:
            dotenv_file = False
        else:
            dotenv_file = find_dotenv()

        if not dotenv_file:
            print("Please upload the .env file. We will rename it correctly, so don't worry about that.")  # noqa E501
            from google.colab import files  # noqa E402
            files.upload_file(
                filename=DOTENV_PATH
            )

        _ = load_dotenv(dotenv_file)
    else:
        dotenv_file = find_dotenv()
        if dotenv_file:
            _ = load_dotenv(dotenv_file)
        else:
            raise RuntimeError("No .env file found")
