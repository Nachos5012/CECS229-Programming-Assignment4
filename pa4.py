'''
import math

""" ----------------- PROBLEM 1 ----------------- """
def translate(S, z0):
  """
    translates the complex numbers of set S by z0
    INPUT: 
        * S - set of complex numbers
        * z0 - complex number
    OUT:
        * a set consisting of points in S translated by z0
    """
  # FIXME: Implement this function
  # FIXME: Return correct output
  return None


""" ----------------- PROBLEM 2 ----------------- """
def scale(S, k):
  """
    scales the complex numbers of set S by k.  
    INPUT: 
        * S - set of complex numbers
        * k - positive float, raises ValueError if k <= 0
    OUT:
        * T - set consisting of points in S scaled by k
        
    """
  # FIXME: Implement this function.
  # FIXME: Return correct output
  return None


""" ----------------- PROBLEM 3 ----------------- """
def rotate(S, tau):
    """
    rotates the complex numbers of set S by tau radians.  
    INPUT: 
        * S - set of complex numbers
        * tau - float. If negative, the rotation is clockwise. If positive the rotation is counterclockwise. 
                If zero, no rotation.
    OUT:
        * a set consisting of points in S rotated by tau radians
        
    """
    # FIXME: Implement this function. 
    # FIXME: Return correct output
    return None


""" ----------------- PROBLEM 4 ----------------- """
class Vec:

  def __init__(self, contents=[]):
    """
        Constructor defaults to empty vector
        INPUT: list of elements to initialize a vector object, defaults to empty list
        """
    self.elements = contents
    return

  def __abs__(self):
    """
        Overloads the built-in function abs(v)
        returns the Euclidean norm of vector v
        """
    # FIXME: Implement this method
    # FIXME: Return correct output
    return None

  def __add__(self, other):
    """
        overloads the + operator to support Vec + Vec
        RAISES ValueError if vectors are not same length 
        RETURNS a Vec object that is the sum vector of this Vec and 'other' Vec
        """
    # FIXME: Finish the implementation
    # FIXME: Return correct output
    return None

  def __sub__(self, other):
    """
        overloads the - operator to support Vec - Vec
        RAISES ValueError if vectors are not same length 
        RETURNS a Vec object that is the difference vector of this Vec and 'other' Vec
        """
    # FIXME: Finish the implementation
    # FIXME: Return correct output
    return None

  def __mul__(self, other):
    """
        Overloads the * operator to support 
            - Vec * Vec (dot product) raises ValueError if vectors are not 
              same length in the case of dot product; returns scalar
            - Vec * float (component-wise product); returns Vec object
            - Vec * int (component-wise product); returns Vec object
            
        """
    if type(other) == Vec:  #define dot product
      # FIXME: Complete the implementation
      # FIXME: Return the correct output
      return 0

    elif type(other) == float or type(
        other) == int:  #scalar-vector multiplication
      # FIXME: Complete the implementation
      # FIXME: Return the correct output
      return None

  def __rmul__(self, other):
    """Overloads the * operation to support 
            - float * Vec; returns Vec object
            - int * Vec; returns Vec object
        """
    # FIXME: Complete the implementation
    # FIXME: Return the correct output
    return None

  def __str__(self):
    """returns string representation of this Vec object"""
    return str(self.elements)  # does NOT need further implementation

'''

import math

""" ----------------- PROBLEM 1 ----------------- """
def translate(S, z0):
    """
    Translates the complex numbers of set S by z0.
    INPUT:
        * S - set of complex numbers
        * z0 - complex number
    OUT:
        * a set consisting of points in S translated by z0
    """
    # Implement this function
    return {z + z0 for z in S}

""" ----------------- PROBLEM 2 ----------------- """
def scale(S, k):
    """
    Scales the complex numbers of set S by k.
    INPUT:
        * S - set of complex numbers
        * k - positive float, raises ValueError if k <= 0
    OUT:
        * T - set consisting of points in S scaled by k
    """
    if k <= 0:
        raise ValueError("k must be greater than 0")
    # Implement this function.
    return {z * k for z in S}

""" ----------------- PROBLEM 3 ----------------- """
def rotate(S, tau):
    """
    Rotates the complex numbers of set S by tau radians.
    INPUT:
        * S - set of complex numbers
        * tau - float. If negative, the rotation is clockwise. If positive, the rotation is counterclockwise. If zero, no rotation.
    OUT:
        * a set consisting of points in S rotated by tau radians
    """
    # Implement this function.
    return {z * math.e**(1j * tau) for z in S}

""" ----------------- PROBLEM 4 ----------------- """
class Vec:

    def __init__(self, contents=[]):
        """
        Constructor defaults to an empty vector.
        INPUT: list of elements to initialize a vector object, defaults to an empty list.
        """
        self.elements = contents

    def __abs__(self):
        """
        Overloads the built-in function abs(v).
        Returns the Euclidean norm of vector v.
        """
        # Implement this method.
        return math.sqrt(sum([x**2 for x in self.elements]))

    def __add__(self, other):
        """
        Overloads the + operator to support Vec + Vec.
        RAISES ValueError if vectors are not the same length.
        RETURNS a Vec object that is the sum vector of this Vec and 'other' Vec.
        """
        if len(self.elements) != len(other.elements):
            raise ValueError("Vectors must be of the same length for addition.")
        # Finish the implementation.
        return Vec([a + b for a, b in zip(self.elements, other.elements)])

    def __sub__(self, other):
        """
        Overloads the - operator to support Vec - Vec.
        RAISES ValueError if vectors are not the same length.
        RETURNS a Vec object that is the difference vector of this Vec and 'other' Vec.
        """
        if len(self.elements) != len(other.elements):
            raise ValueError("Vectors must be of the same length for subtraction.")
        # Finish the implementation.
        return Vec([a - b for a, b in zip(self.elements, other.elements)])

    def __mul__(self, other):
        """
        Overloads the * operator to support:
            - Vec * Vec (dot product) raises ValueError if vectors are not
              the same length in the case of the dot product; returns scalar
            - Vec * float (component-wise product); returns Vec object
            - Vec * int (component-wise product); returns Vec object
        """
        if type(other) == Vec:
            if len(self.elements) != len(other.elements):
                raise ValueError("Vectors must be of the same length for dot product.")
            # Complete the implementation and return the correct output.
            return sum([a * b for a, b in zip(self.elements, other.elements)])

        elif type(other) == float or type(other) == int:
            # Complete the implementation and return the correct output.
            return Vec([x * other for x in self.elements])

    def __rmul__(self, other):
        """Overloads the * operation to support:
            - float * Vec; returns Vec object
            - int * Vec; returns Vec object
        """
        # Complete the implementation and return the correct output.
        return Vec([other * x for x in self.elements])

    def __str__(self):
        """Returns a string representation of this Vec object."""
        return str(self.elements)
