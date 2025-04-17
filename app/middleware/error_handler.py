from fastapi import Request, status
from fastapi.responses import JSONResponse
from sqlite3 import Error as SQLiteError

async def sql_error_handler(request: Request, call_next):
    try:
        return await call_next(request)
    except SQLiteError as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": "Database error occurred. Please try again."}
        )
    except ValueError as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"detail": str(e)}
        )
