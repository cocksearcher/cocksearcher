class DependencyNotImplementedError(Exception):
    def __init__(self, dependency, interface):
        self.dependency = dependency
        self.interface = interface

    def __str__(self):
        return f"dependency is not implemented. dependency: {type(self.dependency)}, interface: {type(self.interface)}"
