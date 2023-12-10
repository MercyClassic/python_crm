import logging
from logging import config

from fastapi import FastAPI
from starlette import status
from starlette.responses import JSONResponse

from app.application.config.config import Config, get_config
from app.application.config.logging import get_logging_dict
from app.main.di.dependencies.init_dependencies import init_dependencies
from app.presentators.api.root_router import root_router

app_config = get_config()


config.dictConfig(get_logging_dict(app_config.ROOT_DIR))
logger = logging.getLogger('main')


def create_app(config: Config) -> FastAPI:
    app = FastAPI()
    init_dependencies(app, config)
    return app


app = create_app(app_config)

app.include_router(root_router)


@app.exception_handler(Exception)
async def unexpected_error_log(request, ex):
    logger.error(ex, exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=None,
    )
