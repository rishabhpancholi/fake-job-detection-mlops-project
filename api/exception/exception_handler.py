from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse

def register_exception_handlers(app: FastAPI)->None:
    """Registers exception handlers"""
    @app.exception_handler(Exception)
    async def custom_exception_handler(request: Request, exc: Exception)->JSONResponse:
        return JSONResponse(content={"detail": str(exc)}, status_code=500)