import os
from typing import Literal
from dotenv import load_dotenv
from hackathon.paths import DOTENV_PATH


def upload_env_vars(
    upload_type: Literal[".env", "interactive"] = "interactive",
    use_defaults: bool = True,
    reupload_if_in_colab=False
):
    try:
        is_in_colab = 'google.colab' in str(get_ipython())  # noqa F821
    except NameError:
        is_in_colab = False

    if is_in_colab:
        if not os.path.exists(DOTENV_PATH) or reupload_if_in_colab:
            match(upload_type):
                case ".env":
                    print("Please upload the .env file. We will rename it correctly, so don't worry about that.")  # noqa E501
                    from google.colab import files  # noqa E402
                    files.upload_file(
                        filename=DOTENV_PATH
                    )
                case "interactive":
                    azure_api_key = input("Please enter your Azure API key: ")
                    # Delete the previous .env file using os.remove
                    if os.path.exists(DOTENV_PATH):
                        os.remove(DOTENV_PATH)

                    # Create new .env file with the Azure API key
                    with open(DOTENV_PATH, "w") as f:
                        f.write(f"AZURE_API_KEY={azure_api_key}")

                    # Add the Azure OpenAI endpoint, OpenAI API version, and model deployment name  # noqa E501
                    with open(DOTENV_PATH, "a") as f:
                        if use_defaults:
                            AZURE_OPENAI_ENDPOINT = "https://be-no-genai-courses-models-located-in-sweden.openai.azure.com"  # noqa E501
                            OPENAI_API_VERSION = "2024-07-01-preview"
                            MODEL_DEPLOYMENT_NAME = "gpt-4o-mini-for-new-hires"
                        else:
                            AZURE_OPENAI_ENDPOINT = input("Please enter your Azure OpenAI endpoint: ")  # noqa E501
                            OPENAI_API_VERSION = input("Please enter your OpenAI API version: ")  # noqa E501
                            MODEL_DEPLOYMENT_NAME = input("Please enter your model deployment name: ")  # noqa E501

                        f.write(f"\nAZURE_OPENAI_ENDPOINT = '{AZURE_OPENAI_ENDPOINT}'")  # noqa E501
                        f.write(f"\nOPENAI_API_VERSION = '{OPENAI_API_VERSION}'")  # noqa E501 
                        f.write(f"\nMODEL_DEPLOYMENT_NAME = '{MODEL_DEPLOYMENT_NAME}'")  # noqa E501
                case _:
                    raise ValueError(f"Invalid value for `upload_type`: {upload_type}")  # noqa E501

        _ = load_dotenv(DOTENV_PATH)
    else:
        if os.path.exists(DOTENV_PATH):
            _ = load_dotenv(DOTENV_PATH)
        else:
            raise RuntimeError("No .env file found")
