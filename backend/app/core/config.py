from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Основные настройки
    PROJECT_NAME: str = "Yurd"
    ENVIRONMENT: str = "development"
    DEBUG: bool = False

    # Безопасность и токен
    SECRET_KEY: str = "mock-insecure-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440

    # База данных PostgreSQL
    DATABASE_URL: str = (
        "postgresql+asyncpg://postgres:postgres@localhost:5432/yurd_db"
    )

    # ИИ провайдер (Gemini API)
    GEMINI_API_KEY: str = "mock-gemini-key"


settings = Settings()

