class DataStorageError(Exception):
    pass

    def get_explanation(self):
        return "Что то не так с файлом данных, " \
               "мы тут храним данные в json и скорее всего " \
               "файл поврежден или не найден"
