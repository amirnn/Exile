import os
from conan import ConanFile
from conan.tools.build import can_run


class pkgTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"

    def requirements(self):
        self.requires(self.tested_reference_str)
        self.requires("catch2/[~3]")

    def test(self):
        if can_run(self):
            self.run("mypkg", env="conanrun")
