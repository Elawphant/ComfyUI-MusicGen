import torchaudio
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write


class GenMusic:

    def __init__(self) -> None:
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        """
            Return a dictionary which contains config for all input fields.
            Some types (string): "MODEL", "VAE", "CLIP", "CONDITIONING", "LATENT", "IMAGE", "INT", "STRING", "FLOAT".
            Input types "INT", "STRING" or "FLOAT" are special values for fields on the node.
            The type can be a list for selection.

            Returns: `dict`:
                - Key input_fields_group (`string`): Can be either required, hidden or optional. A node class must have property `required`
                - Value input_fields (`dict`): Contains input fields config:
                    * Key field_name (`string`): Name of a entry-point method's argument
                    * Value field_config (`tuple`):
                        + First value is a string indicate the type of field or a list for selection.
                        + Secound value is a config for type "INT", "STRING" or "FLOAT".
        """
        return {
            "required": {
                "modelName": ("STRING", {
                    "default": "melody",
                    "display": "combo",
                    "values": ["melody", "small", "medium", "large"],
                }),
                "descriptions": ("STRING", {
                    "default": "",
                    "display": "text",
                }),
                "duration": ("INT", {
                    "default": 8, 
                    "min": 1, #Minimum value
                    "max": 180, #Maximum value
                    "step": 1, #Slider's step
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                }),
            },
            "hidden" : { 
                "prompt": "PROMPT",
                "extra_info": "EXTRA_PNGINFO",
                "id": "UNIQUE_ID",
            }

        }

    RETURN_TYPES = ("AUDIO", "STRING",)
    RETURN_NAMES = ("AUDIO", "FILENAME", )

    FUNCTION = "process"

    #OUTPUT_NODE = False

    CATEGORY = "MusicGen"

    def process(self, modelName: str, descriptions: str, melody, sr):
        model = MusicGen.get_pretrained(modelName)

        result = model.generate_with_chroma(descriptions.split(","), melody[None].expand(3, -1, -1), sr)
        return (result,)

    """
        The node will always be re executed if any of the inputs change but
        this method can be used to force the node to execute again even when the inputs don't change.
        You can make this node return a number or a string. This value will be compared to the one returned the last time the node was
        executed, if it is different the node will be executed again.
        This method is used in the core repo for the LoadImage node where they return the image hash as a string, if the image hash
        changes between executions the LoadImage node is executed again.
    """
    #@classmethod
    #def IS_CHANGED(s, image, string_field, int_field, float_field, print_to_screen):
    #    return ""

# Set the web directory, any .js file in that directory will be loaded by the frontend as a frontend extension
# WEB_DIRECTORY = "./somejs"

# # A dictionary that contains all nodes you want to export with their names
# # NOTE: names should be globally unique
# NODE_CLASS_MAPPINGS = {
#     "GenMusic": GenMusic
# }

# # A dictionary that contains the friendly/humanly readable titles for the nodes
# NODE_DISPLAY_NAME_MAPPINGS = {
#     "Generate Music": "GenMusic"
# }
