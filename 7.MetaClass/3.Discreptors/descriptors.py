

# Non-Data Descriptors
class Yes:
  """A non-data descriptor that just returns 'yes'"""

  def __get__(self, instance, owner):
      return "yes"






 # Data Descriptors

class NoisyDescriptor:
  '''A data descriptor that prints messages when accessed or modified'''

  def __set_name__(self, owner, name): # The main role of __set_name__ is to bind the descriptor to the owner class
    print(f'Received {name=} of type {owner=}') #
    self.private_name = f'_{name}'



  def __get__(self, obj, objcls):
    print(f'Getting {self.private_name} from {obj=} of type {objcls}')
    if obj:  # Check if the instance is not None
      return getattr(obj, self.private_name, "Nothing here !!!")
    return getattr(objcls, self.private_name, "Nothing here !!!")

  def __set__(self, obj, value):
    print(f"Setting {value=} on {obj=}")
    setattr(obj, self.private_name, value)

  def __delete__(self, obj):
    print(f"Deleting value on {obj=}")
    delattr(obj, self.private_name)


class Constant:

  def __init__(self, value, strict=False):

    self.value = value
    self.strict = strict

  def __get__(self, obj, objels):
    return self.value

  def __set__(self, obj, value):
    if self.strict: #is means
      raise AttributeError("Can't change a constant value")









class TestClass:
  alpha  = Yes()
  beta = NoisyDescriptor()
  gamma = NoisyDescriptor()
  delta = Constant(42)
  epsilon = Constant("I'm Strict!", strict=True)



  def __init__(self, value):
    self.beta = value

  @property
  def zeta(self):
    return "I'm "


