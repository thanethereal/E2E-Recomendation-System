from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

router = APIRouter()


@router.post('/health', status_code=200)
async def health_check() -> JSONResponse:
    #respone status
    return JSONResponse({'OK': True})