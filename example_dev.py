class A:
    @classmethod
    def class_method(cls):
        return "çlass method"

    def method(self):
        return "method"

    @classmethod
    def another_class_method(cls):
        return cls.class_method()

    def another_method(self):
        return self.method()


instance = A()
print(f"{A.class_method() = }")
print(f"{instance.method() = }")
