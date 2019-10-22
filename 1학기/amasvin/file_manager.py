import pickle

class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def save(self, data):
        f = open(self.filename, "wb")
        pickle.dump(data,f)
        f.close()

    def load(self):
        try:
            f = open(self.filename, "rb")
            data = pickle.load(f)
            f.close()
        except FileNotFoundError:
            raise FileNotFoundError #던짐 메인이 받아서 처리해줘야함

        return data