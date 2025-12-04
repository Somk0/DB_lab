import os
import yaml

def load_config():
    # Отримуємо абсолютний шлях до директорії "app"
    app_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # Формуємо шлях до файлу конфігурації
    config_path = os.path.join(app_dir, "config", "app.yml")

    print("CONFIG PATH =", config_path)  # Діагностика

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config not found at: {config_path}")

    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
