import os

from nakuyagen.language import Language


class Cpp(Language):
    format_path = "format/cpp"

    def __init__(self, project_name=None):
        super().__init__(project_name)

    def __str__(self) -> str:
        return self._display("C++")

    def create(self) -> None | BaseException:
        res = super().create()
        if isinstance(res, BaseException):
            return res
        print("[SYSTEM]: Editing Makefile")
        buffer = str()
        with open(os.path.join(self.dst, "Makefile"), "r") as file:
            buffer = file.read()
        with open(os.path.join(self.dst, "Makefile"), "w") as file:
            if self.project_name is not None:
                buffer = buffer.replace("#PROJECT_NAME#", self.project_name)
                file.write(buffer)
            else:
                return ValueError("Cannot read project_name property")
