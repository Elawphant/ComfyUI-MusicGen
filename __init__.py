from .audio_loader import AudioLoader
from.music_generator import GenMusic

# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "AudioLoader": AudioLoader,
    "MusicGen": GenMusic
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "Load Simple": "AudioLoader",
    "Make Music": "MusicGen",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]