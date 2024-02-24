from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    llm_model_name: str
    llm_model_host: str
    embedding_model_path: str
    database_media: str
    database_username: str
    database_password: str
    database_host_name: str
    database_port: str
    database_name: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    redis_db_host: str
    redis_db_port: str
    redis_db_no: int
    backend_server_host_name: str
    backend_server_port_no: str

    class Config:
        env_file = ".env"

settings = Settings()