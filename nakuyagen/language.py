import os
import shutil


class Language:
    project_name: str | None
    format_path: str = ""
    dst: str
    src: str

    def __init__(self, project_name=None):
        self.project_name = project_name

    def _generate_project(self):
        if self.project_name is None:
            self.project_name = input("Project name: ").strip()

    def _display(self, lang="Unknown") -> str:
        return f"Project Language: {lang}"

    def __str__(self) -> str:
        return self._display()

    def _copy_tree(self):
        for item in os.listdir(self.src):
            s = os.path.join(self.src, item)
            d = os.path.join(self.dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks=False, ignore=None)
            else:
                shutil.copy2(s, d)

    def create(self) -> None | BaseException:
        if self.project_name is None:
            self.project_name = input("Project name: ").strip()

        self.dst = os.path.join(os.getcwd(), self.project_name)
        self.src = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), self.format_path
        )

        if not os.path.exists(self.dst):
            os.makedirs(self.dst)
        else:
            return FileExistsError("Folder Already Exists")
        print("[SYSTEM]: Copying format")
        self._copy_tree()
