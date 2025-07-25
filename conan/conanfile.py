from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps


class pkgRecipe(ConanFile):
    name = "Exile"
    version = "1.0.0"
    package_type = "application"

    # Optional metadata
    license = "MIT"
    author = "Amir Nourinia amir.nouri.nia@gmail.com"
    url = "github.com/amirnn/exile"
    description = "Graphics Programming"
    topics = ("OpenGL", "Vulkan", "Game")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"

    # Sources are located in the same place as this recipe, copy them to the recipe
    exports_sources = "CMakeLists.txt", "src/*"

    def layout(self):
        cmake_layout(self, src_folder="..", build_folder="out")
        
    def requirements(self):
        self.requires("opengl/system")
        self.requires("glad/[~0.1]")
        self.requires("glfw/[~3]")
        self.requires("eigen/[~3]")
        # self.requires("zlib/1.3.1")
        # self.requires("boost/1.88.0")
        # self.requires("glm/1.0.1")
        

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.user_presets_path = "ConanPresets.json"
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    # def package(self):
    #     cmake = CMake(self)
    #     cmake.install()

    

    
