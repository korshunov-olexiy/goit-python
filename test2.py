from copy import deepcopy

class Property:
    def __init__(self, type_, default_value):
        self._type = type_
        self._default_value = default_value

    def generate_property(self, name):
        self._internal_name = '_' + name
        def getter(object_):
            return getattr(object_, self._internal_name)
        def setter(object_, value):
            if not isinstance(value, self._type):
                raise TypeError("Expect type {0}, got {1}.".format(self._type, type(value)))
            else:
                setattr(object_, self._internal_name, value)
        return property(getter, setter)


class AutoPropertyMeta(type):
    def __new__(meta, name, bases, attributes):
        defaults = {}
        for name, value in attributes.iteritems():
            if isinstance(value, Property):
                attributes[name] = value.generate_property(name)
                defaults[name] = value._default_value
        # create __init__ to inject into the class
        # our __init__ sets up our secret attributes
        if '__init__' in attributes:
            realInit = attributes['__init__']
            # we do a deepcopy in case default is mutable
            # but beware, this might not always work
            def injectedInit(self, *args, **kwargs):
                for name, value in defaults.iteritems():
                    setattr(self, '_' + name, deepcopy(value))
                # call the "real" __init__ that we hid with our injected one
                realInit(self, *args, **kwargs)
        else:
             def injectedInit(self, *args, **kwargs):
                for name, value in defaults.iteritems():
                    setattr(self, '_' + name, deepcopy(value))
        # inject it
        attributes['__init__'] = injectedInit
        return super(AutoPropertyMeta, meta).__new__(meta, name, bases, attributes)


class SomeClassWithALotAttributes:
    __metaclass__ = AutoPropertyMeta
    attribute_a = Property(str, "")
    attribute_z = Property(list, [])

    def __init__(self):
        print("This __init__ is still called")


x = SomeClassWithALotAttributes()
print(x.attribute_a._default_value)
