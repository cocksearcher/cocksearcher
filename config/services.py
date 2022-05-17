from config.exceptions import DependencyNotImplementedError


class BaseService:
    dependency_interfaces = ()

    @classmethod
    def check_dependencies(cls, *dependencies):
        for dependency, interface in zip(dependencies, cls.dependency_interfaces):
            if not isinstance(dependency, interface):
                raise DependencyNotImplementedError(dependency, interface)
