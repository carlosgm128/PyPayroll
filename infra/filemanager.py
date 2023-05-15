"""
    this module is in charge of handling files IO
"""
import sys

from application.util.utils import Utils


class FileManager:
    @staticmethod
    def get_data_from_archive():
        """
            method created to retrieve data from an archive or a path indicated
        """
        file = None
        tries = 3
        while tries != 0:
            try:
                if len(sys.argv) > 1 and sys.argv[1].find('--path') != -1:
                    path = sys.argv[1].rsplit('=')[1]
                    Utils.check_extension(path)
                else:
                    path = input("inserte la ruta del archivo de pagos para procesar ")
                    Utils.check_extension(path)
                file = open(path, 'rt', encoding='UTF-8')
                if file is not None:
                    break
            except FileNotFoundError:
                print(f'Archivo no encontrado. {tries - 1} intentos restantes')
                if tries == 1:
                    print('numero de intentos posibles terminados\nsaliendo...')
                    sys.exit()
            finally:
                tries -= 1
        try:
            data = file.readlines()
            return data
        except FileNotFoundError as ex:
            raise FileNotFoundError(f"Archivo con el nombre de {path} no encontrado\nError\n {ex}")
        finally:
            file.close()
