import sys
import os
from pathlib import Path


def suma(a,b):
    return a+b


# def find_root_dir(start_path: Path = None, marker_file: str = "auto_importer.py") -> Path:
#     """
#     Traverse upward to locate the project root directory by finding a marker file.
    
#     Args:
#         start_path (Path): Starting path to begin the search. Defaults to the current working directory.
#         marker_file (str): The name of the file that identifies the root directory.
        
#     Returns:
#         Path: Resolved path of the root directory.
#     """
#     if start_path is None:
#         try:
#             # Start from the current file's directory
#             start_path = Path(__file__).resolve().parent
#         except NameError:
#             # Fallback to the current working directory if __file__ isn't defined
#             start_path = Path.cwd()

#     current_dir = start_path
#     while current_dir != current_dir.parent:  # Stop at the filesystem root
#         if (current_dir / marker_file).exists():
#             return current_dir
#         current_dir = current_dir.parent

#     raise FileNotFoundError(f"Marker file '{marker_file}' not found in any parent directories.")

# Use the function to define ROOT_DIR



# GEMINI
# import sys
# from pathlib import Path

# class AutoImporter:
#     def __init__(self, base_dir=None):
#         self.base_dir = Path(base_dir or Path.cwd())
#         self.add_to_sys_path()

#     def add_to_sys_path(self):
#         for path in self.base_dir.rglob("*"):
#             if path.is_dir():
#                 sys.path.insert(0, str(path))


# mi_auto_importer = AutoImporter ()



# GPT

# import sys
# from pathlib import Path

# class AutoImporter:
#     def __init__(self, base_dir=None):
#         """
#         Constructor que inicializa el directorio base y configura las rutas para la importación.

#         :param base_dir: Ruta del directorio base (opcional). Si no se proporciona, utiliza el directorio actual.
#         """
#         self.base_dir = Path(base_dir) if base_dir else Path.cwd()
#         self.add_to_sys_path()

#     def add_to_sys_path(self):
#         """
#         Añade recursivamente todos los subdirectorios del base_dir a sys.path.
#         """
#         for subdir in self.base_dir.rglob("*"):
#             if subdir.is_dir() and str(subdir) not in sys.path:
#                 sys.path.append(str(subdir))