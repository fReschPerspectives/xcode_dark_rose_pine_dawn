import os


class SampleTheme:    
    def __init__(self):
        self.name = "Sample Theme"
        self.author = "OpenAI"
        self.version = "1.0.0"
        self.description = "A sample theme for demonstration purposes."
        self.assets_path = os.path.join(os.path.dirname(__file__), 'assets')
        self.major_version = 1
        self.minor_version = 0
        self.release_version = 0

    def get_asset_path(self, asset_name):
        return os.path.join(self.assets_path, asset_name)
    
    def get_version(self):
        return f"{self.major_version}.{self.minor_version}.{self.release_version}"