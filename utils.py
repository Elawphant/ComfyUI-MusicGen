
import os

AUDIO_EXTENSIONS = ("wav", "mp3", "ogg", "flac")
AUDIO_INPUT_DIR = "audio"

PROMPT_SEQ_EXTENSIONS = ("json", )
PROMPT_SEQ_INPUT_DIR = "promptSequences"

# Functions
def fullpath(filepath: str) -> str:
    """
    Returns a full filepath for the given filepath.
    """
    return os.path.abspath(os.path.expanduser(filepath))

def audioInputDir() -> str:
    """
    Returns the audio input directory.
    """
    return os.path.join(os.path.dirname(__file__), AUDIO_INPUT_DIR)

def promptSeqInputDir() -> str:
    """
    Returns the prompt sequence input directory.
    """
    return os.path.join(os.path.dirname(__file__), PROMPT_SEQ_INPUT_DIR)
