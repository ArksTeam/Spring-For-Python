class ApplicationContext:
    def __init__(self):
        self.beans = {}

    def register_bean(self, bean_name, bean):
        self.beans[bean_name] = bean

    def get_bean(self, bean_name):
        return self.beans.get(bean_name)


class Bean:
    def __init__(self, bean_id=None):
        self.bean_id = bean_id

    def init(self):
        pass

    def destroy(self):
        pass
