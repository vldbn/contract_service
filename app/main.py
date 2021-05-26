import uvicorn
from fastapi import FastAPI

from app.core.config import Config
from app.handlers.router import router as api_router


def get_application(config: Config) -> FastAPI:
    application = FastAPI(title=config.project_name, version=config.version)
    application.include_router(api_router, prefix="/api")
    return application


conf = Config()

app = get_application(conf)

if __name__ == '__main__':
    uvicorn.run(app, port=conf.port)
