from fastapi import FastAPI

from app.credit_defaulter.main import credit_defaulter

def create_app():
    app = FastAPI(title = "Ankit's ApiSite", redoc_url = None, docs_url = None)

    @app.get('/')
    async def get_all_urls():
        url_list = [{"path": route.path, "name": route.name} for route in app.routes]
        return url_list
    
    app.include_router(credit_defaulter)
    return app