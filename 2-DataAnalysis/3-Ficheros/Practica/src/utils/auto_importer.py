# import os

# class AutoImporter:

#     def __init__(self, base_dir=None):
#         self.base_dir = base_dir

#     def add_to_sys_path(self, path_carpeta):
#         for archivo in os.listdir(path_carpeta):
#             path_archivo = os.path.join(path_carpeta, archivo)
#             if os.path.isfile(path_archivo)
#                 for origen, carpetas, archivos in os.walk(self.base_dir):
#                     for dir in carpetas:
#                         path_carpeta = os.path.join(origen, dir)
#                         self.add_to_sys_path(path_carpeta) 