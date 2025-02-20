import json


class MenuDataLoader:
    """Class to load menu data from JSON file"""
    def __init__(self, file_path: str):
        self.file_path = file_path
        self._cached_menu_data: dict = {}

    def _load_data(self) -> dict:
        """Load data from JSON file"""
        try:
            with open(self.file_path) as file:
                return json.load(file)
        except FileNotFoundError as error:
            raise FileNotFoundError(f"File {self.file_path} not found") from error
        except json.JSONDecodeError as error:
            raise json.JSONDecodeError(
                f"File {self.file_path} is not a valid JSON file"
            ) from error
        except Exception as e:
            raise e

    def get_menu_data(self) -> dict:
        """Get menu data from JSON file"""
        if not self._cached_menu_data:
            self._cached_menu_data = self._load_data()
        return self._cached_menu_data
