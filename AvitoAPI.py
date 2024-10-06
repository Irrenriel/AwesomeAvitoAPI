from avitoapi.AvitoAdvertisements import AvitoAdvertisements
from avitoapi.AvitoProfile import AvitoProfile
from avitoapi.AvitoToken import AvitoToken


class AvitoAPI(
    AvitoToken,
    AvitoProfile,
    AvitoAdvertisements
):
    def __init__(
        self,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
