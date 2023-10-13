import os
import typing
from PickleObjects.Pickler.Pickler import load_obj, save_obj


class Generator(object):
    UID_Value: int
    path: typing.Union[str, bytes, os.PathLike]

    def __init__(self, path: typing.Union[str, bytes, os.PathLike]):
        self.UID_Value = 0
        self.path = path

    def return_uid(self):
        self.UID_Value -= 1
        return self.UID_Value

    def return_uid_and_save(self):
        self.UID_Value -= 1
        self.save()
        return self.UID_Value

    def save(self):
        save_obj(self, self.path)


def return_generator(generator_path: typing.Union[str, bytes, os.PathLike]) -> Generator:
    if not generator_path.endswith(".pkl"):
        generator_path += ".pkl"
    if os.path.exists(generator_path):
        return load_obj(generator_path)
    else:
        return Generator(generator_path)


if __name__ == '__main__':
    pass
