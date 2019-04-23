from .json_tools import JSONMixin

class LightSettings(JSONMixin):
    """
    Configuration of lights on the plane

    Parameters
    ---------
        lights_position : array
            TODO
        ambient_ratio : float
            TODO
        diffuse_ratio : float
            TODO
        specular_ratio : float
            TODO
        lights_strength : array
            TODO
        number_of_lights : int
            Number of lights in visualization
    """
    def __init__(
        self,
        lights_position=None,
        ambient_ratio=None,
        diffuse_ratio=None,
        specular_ratio=None,
        lights_strength=None,
        number_of_lights=2
    ):
        self.ambient_ratio = ambient_ratio
        self.diffuse_ratio = diffuse_ratio
        self.lights_position = lights_position
        self.lights_strength = lights_strength
        self.number_of_lights = number_of_lights
        self.specular_ratio = specular_ratio
