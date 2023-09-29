import core.ioc as spring_ioc
import core.logger as spring_log
class UserService:
    @spring_ioc.autowired()
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def get_user(self, user_id):
        return self.user_repository.get_user(user_id)
    
class UserRepository:
    def get_user(self, user_id):
        return f"User {user_id}"
    
context = spring_ioc.ApplicationContext()
context.register_bean(spring_ioc.BeanDefinition("userRepository", UserRepository))
context.register_bean(spring_ioc.BeanDefinition("userService", UserService, dependencies=["userRepository"]))
userService = context.get_bean("userService")
context.autowire(userService)

user = userService.get_user(123)
print(user)  # 输出: User 123

with spring_log('2023.log') as logger:
    logger.writeNewLog('Exit.')

