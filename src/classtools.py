"Assorted class utilities and tools"


class AttributeDisplay:
    """
    Provides an inheritable display overload method that shows
    instances with their class names and a name=value pair for
    each attribute stored on the instance itself (but not attrs
    inherited from its classes). Can be mixed into any class,
    and will work on any instance.
    """

    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append(f"{key}={getattr(self,key)}")
        return ", ".join(attrs)

    def __repr__(self) -> str:
        return f"[{self.__class__.__name__}: {self.gatherAttrs()}]"


if __name__ == "__main__":

    class TopTest(AttributeDisplay):
        """
        Test super class
        """

        count = 0

        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2

    class SubTest(TopTest):
        """
        Test sub class
        """

        pass

    X, Y = TopTest(), SubTest()
    print(X)
    print(Y)
