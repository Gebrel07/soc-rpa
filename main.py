import os

from dotenv import load_dotenv
from selenium.webdriver import Firefox

from src.login import LoginHandler


def main():
    load_dotenv(".env")

    with Firefox() as driver:
        login_handler = LoginHandler(
            url=os.getenv("URL"),
            username=os.getenv("SOC_USERNAME"),
            password=os.getenv("SOC_PASSWORD"),
            id=os.getenv("SOC_ID"),
            driver=driver,
        )

        login_handler.login()


if __name__ == "__main__":
    main()
