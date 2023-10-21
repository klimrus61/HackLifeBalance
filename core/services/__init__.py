from .auth_config import CookiesAuthentication, CookiesAuthenticationExtension
from .email_template import get_email_template as GetEmailTemplateService
from .exception_handler import custom_exceptions_handler as CustomExceptionsHandler
from .image_service import ImageFileManager as ImageFileManagerService
from .string_generator import RandomString as GenerateRandomStringService
from .zip_service import ZipService

zip_service = ZipService()

__all__ = (
    "GenerateRandomStringService",
    "GetEmailTemplateService",
    "ImageFileManagerService",
    "CustomExceptionsHandler",
    "zip_service",
    "CookiesAuthentication",
    "CookiesAuthenticationExtension",
)
