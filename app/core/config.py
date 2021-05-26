import os
from pathlib import Path


class Config:
    """Application config class."""

    def __init__(self) -> None:
        self.project_name = os.getenv("PROJECT_NAME", "Test Project")
        self.version = os.getenv("VERSION", "0.0.0")
        self.port = os.getenv("PORT", 8000)

        base_dir = Path(__file__).resolve().parent.parent.parent
        self.files_path = f'{base_dir}/files'

        if not os.path.exists(self.files_path):
            os.makedirs(self.files_path)
