
from app import create_app

from toubib.config.config import APPSettings

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app='main:app', host=APPSettings.APP_HOST, port=APPSettings.APP_PORT, reload=True)

