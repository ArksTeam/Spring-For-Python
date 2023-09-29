import inspect


class BeanDefinition:
    def __init__(self, bean_name, bean_class, dependencies=None):
        self.bean_name = bean_name
        self.bean_class = bean_class
        self.dependencies = dependencies or []


class ApplicationContext:
    def __init__(self):
        self.bean_registry = {}

    def register_bean(self, bean_definition):
        self.bean_registry[bean_definition.bean_name] = bean_definition

    def get_bean(self, bean_name):
        bean_definition = self.bean_registry.get(bean_name)
        if not bean_definition:
            raise Exception(f"Bean '{bean_name}' is not registered.")
        bean_instance = self.create_bean_instance(bean_definition)
        return bean_instance

    def create_bean_instance(self, bean_definition):
        dependencies = []
        for dependency_name in bean_definition.dependencies:
            dependency_instance = self.get_bean(dependency_name)
            dependencies.append(dependency_instance)
        bean_instance = bean_definition.bean_class(*dependencies)
        return bean_instance


def autowired():
    def wrapper(func):
        def inner(*args, **kwargs):
            dependencies = []
            for param_name in inspect.signature(func).parameters.keys():
                dependency_instance = ApplicationContext().get_bean(param_name)
                dependencies.append(dependency_instance)
            return func(*dependencies, *args, **kwargs)

        return inner

    return wrapper