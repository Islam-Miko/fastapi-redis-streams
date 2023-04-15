from typing import Any

from fastapi import HTTPException, status


class APIException(HTTPException):
    STATUS_CODE = status.HTTP_500_INTERNAL_SERVER_ERROR
    DETAIL = "Server error"

    def __init__(self, **kwargs: dict[str, Any]) -> None:
        super().__init__(
            status_code=self.STATUS_CODE, detail=self.DETAIL, **kwargs
        )


class FileTooLarge(APIException):
    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    DETAIL = "File size too large"
