import subprocess
import sys
import os
import logging
from pathlib import Path

def get_current_directory():
    return os.getcwd()
def create_env():
    env_name = 'denis_env'
    env_path = Path(env_name)
    subprocess.check_call([sys.executable, '-m', 'venv', str(env_path)])
    return env_path

def pip_packages(env_path: str):
    pip_path = env_path / 'Scripts' / 'pip' if os.name == 'nt' else env_path / 'bin' / 'pip'
    command = f"{pip_path} install catboost scikit-learn optuna pandas numpy"
    logging.basicConfig(level=logging.INFO, filename='install.txt', filemode='w',
                        format='%(asctime)s - %(levelname)s - %(message)s')
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        logging.info("stdout: %s", result.stdout)
        if result.returncode != 0:
            logging.error("stderr: %s", result.stderr)
            logging.error("Проблема с установкой библиотек.")
        else:
            logging.info("Все нужные библиотеки успешно установлены.")
    except Exception as e:
        logging.exception("Не удалось выполнить команду установки библиотек.")

env_path = create_env()
pip_packages(env_path)

