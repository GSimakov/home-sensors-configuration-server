from app.core.configurations.app import AppSettings


class ProdAppSettings(AppSettings):

    title: str = "Prod Valeria"

    class Config(AppSettings.Config):
        env_file = "prod.env"
