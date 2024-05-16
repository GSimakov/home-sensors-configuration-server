from functools import lru_cache
from typing import Dict, Type

from app.core.configurations.app import AppSettings
from app.core.configurations.base import AppEnvTypes, BaseAppSettings
from app.core.configurations.development import DevAppSettings
from app.core.configurations.production import ProdAppSettings
from app.core.configurations.test import TestAppSettings

environments: Dict[AppEnvTypes, Type[AppSettings]] = {
    AppEnvTypes.dev: DevAppSettings,
    AppEnvTypes.prod: ProdAppSettings,
    AppEnvTypes.test: TestAppSettings,
}


@lru_cache
def get_app_settings() -> AppSettings:
    app_env = BaseAppSettings().app_env
    config = environments[app_env]
    return config()


settings = get_app_settings()
