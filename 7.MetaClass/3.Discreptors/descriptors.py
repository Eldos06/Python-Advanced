

# Non-Data Descriptors
class Yes:
  """A non-data descriptor that just returns 'yes'"""

  def __get__(self, instance, owner):
      return "yes"






 # Data Descriptors

class NoisyDescriptor:
  '''A data descriptor that prints messages when accessed or modified'''

  def __get__(self, obj, objcls):
    print(f'Getting value from {obj=} of type {objcls}')
    if obj:  # Check if the instance is not None
      return getattr(obj, "_noisy", "Nothing here !!!")
    return getattr(objcls, "_noisy", "Nothing here !!!")

  def __set__(self, obj, value):
    print(f"Setting {value=} on {obj=}")
    setattr(obj, "_noisy", value)

  def __delete__(self, obj):
    print(f"Deleting value on {obj=}")
    delattr(obj, "_noisy")



class TestClass:
  alpha  = Yes()
  beta = NoisyDescriptor()
  gamma = NoisyDescriptor()

  def __init__(self, value):
    self.beta = value