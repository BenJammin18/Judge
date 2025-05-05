import yaml

def load_models():
    with open("config/models.yaml", "r") as f:
        return yaml.safe_load(f)['models']

def load_settings():
    with open("config/settings.yaml", "r") as f:
        return yaml.safe_load(f)
