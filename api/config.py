import os
import sys
parent_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(parent_dir)


from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    llm_model_name: str
    llm_model_host: str
    embedding_model_path: str
    tokens_per_chunk: int
    use_gpu: int
    num_threds: int
    timeout: int
    temperature: float
    backend_server_host_name: str
    backend_server_port_no: str

    class Config:
        env_file = ".env"

settings = Settings()