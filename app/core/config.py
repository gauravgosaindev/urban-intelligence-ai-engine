from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Application settings and environment configuration.
    """
    PROJECT_NAME: str = "Urban Intelligence AI Engine"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()