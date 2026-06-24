'''


Why @dataclass python decorator is used ?




Class InformaticaConfig(login_url:str, username:str, password:str, api_base_url:str):
    def __init__(self, login_url, username, password, api_base_url):
        self.login_url = login_url
        self.username = username
        self.password = password
        self.api_base_url = api_base_url



InformaticConfig_obj = InformaticaConfig(login_url="https://dm-us.informaticacloud.com", username="edg-datahub-api-prd", password="X99fe45#bvr", api_base_url="https://idmc-api.dm-us.informaticacloud.com")


TO AVOID THE above boilerplat code, we can use @dataclass decorator


@dataclass(frozen=True)
class InformaticaConfig:
    login_url: str
    username: str
    password: str
    api_base_url: str


InformaticConfig_obj = InformaticaConfig(login_url="https://dm-us.informaticacloud.com", username="edg-datahub-api-prd", password="X99fe45#bvr", api_base_url="https://idmc-api.dm-us.informaticacloud.com")


'''