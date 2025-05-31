from pydantic import Basemodel

class settings(basesettings):
    app_name: str
    admin_email: str
    items_per_user: int = 50


settings = Settings()