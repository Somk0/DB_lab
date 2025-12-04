import os
import yaml


def load_config():
    
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    config_path = os.path.join(base_dir, "app", "config", "app.yml")

    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
