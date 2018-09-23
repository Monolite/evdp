import json

class ConfigLoader():

    def __init__(self, config_path):

        with open(config_path) as f:
            devconf = json.load(f)
        
        self.device_name = devconf['device_name']        

        self.model_path = devconf['model_path']
        self.model_texture_path = devconf['model_texture_path']
        self.dynamic_texture_path = devconf['dynamic_texture_path']

        self.initial_position = devconf['initial_position']
        self.model_transformation = devconf['model_transformation']
        
        self.images_path = devconf['images_path']
        self.music_path = devconf['music_path']
        self.background_path = self.images_path + '/' + devconf['background']

        


