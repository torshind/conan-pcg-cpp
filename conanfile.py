from conans import ConanFile, CMake, tools


class PcgCppConan(ConanFile):
    name = "pcg-cpp"
    version = "latest"
    license = "MIT"
    url = "http://www.pcg-random.org/"
    description = "PCG — C++ Implementation"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    exports_sources = "*"

    def source(self):
        git = tools.Git()
        git.clone("https://github.com/imneme/pcg-cpp.git", "master")

    def build(self):
        self.run("make test")

    def package(self):
        self.copy("*.hpp", dst="include", src="include")

    def package_info(self):
        self.info.header_only()
