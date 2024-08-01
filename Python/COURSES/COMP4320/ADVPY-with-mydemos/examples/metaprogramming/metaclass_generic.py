class Meta(type):

    def __prepare__(class_name, bases):
        """ "Prepare" the new class. Here you can update the base classes.

        :param name: Name of new class as a string
        :param bases: Tuple of base classes
        :return: Initializes the namespace for the new class (must be a dict)
        """
        print('=' * 60)
        print(f"In metaclass (class={class_name}) __prepare__()",
              f"with: name={class_name}, bases={bases}", sep=' ==> ')
        return {'animal': 'wombat', 'id': 100}

    def __new__(metatype, name, bases, attrs):
        """Create the new class. Called after __prepare__(). Note this is
        only called when classes

        :param metatype: The metaclass itself
        :param name: The name of the class being created
        :param bases: bases of class being created (may be empty)
        :param attrs: Initial attributes of the class being created
        """
        print('=' * 60)
        print(f"In metaclass (class={name}) __new__()",
              f"with: type={metatype} name={name} bases={bases} attrs={attrs}",
              sep=' ==> ')
        return super().__new__(metatype, name, bases, attrs)

    def __init__(cls, *args):
        """
        :param cls: Class being created (compare with 'self' in normal class)
        :param args: Any arguments to the class
        """
        print('=' * 60)
        print(f"In metaclass (class={cls.__name__}) __init__()")
        print(f"params: cls={cls}, args={args}", sep=' ==> ')
        super().__init__(cls)

    def __call__(self, *args, **kwargs):
        """ Called when the metaclass is called, like NewClass = Meta(...)"""
        print('-' * 60)
        print("in metaclass (class={self.__name__)})__call__()")
