

# Non-Data Descriptors
class Yes:
  """A non-data descriptor that just returns 'yes'"""

  def __get__(self, instance, owner):
      return "yes"

class TestClass:
  alpha  = Yes()




 # Data Descriptors





