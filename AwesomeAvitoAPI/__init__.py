from .modules import *
from .responses import *


class AwesomeAvitoAPI(
    AvitoAuth,
    AvitoUser,
    AvitoAccountsHierarchy,
    AvitoAuction,
    AvitoItem,
    AvitoMessenger,
    AvitoRatings,
):
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        *args,
        **kwargs
    ):
        super().__init__(
            client_id=client_id,
            client_secret=client_secret,
            *args,
            **kwargs
        )
