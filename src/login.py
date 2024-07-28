from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class LoginHandler:
    def __init__(
        self,
        url: str,
        username: str,
        password: str,
        id: str,
        driver: WebDriver,
    ) -> None:
        self.url: str = url
        self.username: str = username
        self.password: str = password
        self.id: str = id
        self.driver: WebDriver = driver

    def login(self):
        """Realiza login no SOC com as credenciais passadas durante a inicializacao da classe"""
        self.driver.get(self.url)
        self.driver.find_element(By.ID, "usu").send_keys(self.username)
        self.driver.find_element(By.ID, "senha").send_keys(self.password)
        self.__input_id()
        self.driver.find_element(By.ID, "formularioLogin").submit()

    def __input_id(self):
        """Encontra os botoes correspondentes ao id do usuario e clica em cada um"""
        # div contendo os botoes
        numpad: WebElement = self.driver.find_element(By.ID, "pteclado")
        for num in self.id:
            # NOTE: cada botao e um elemento do tipo input, com atributo valor
            # correspondente a um numero da id de usuario
            numpad.find_element(By.XPATH, f".//input[@value='{num}']").click()
