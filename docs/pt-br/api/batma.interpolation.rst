``batma.interpolation`` --- Interpolation
=========================================

.. module:: batma.interpolation
   :synopsis: Interpolation functions.

Functions
---------

.. function:: catmullrom(value1, value2, value3, value4, amount)
   
   Performs a Catmull-Rom interpolation using the specified positions.


.. function:: hermite(value1, tangent1, value2, tangent2, amount)

   Performs a Hermite spline interpolation.


.. function:: highpower(value1, value2, amount, power=2)

   Performs a interpolation using the following equation:

   .. math::
    
      value1 + (value2 - value1) * amount^{power}


.. function:: ihighpower(value1, value2, amount, power=2)

   The inverse of the :func:`highpower` function. Performs a interpolation 
   using the following equation:

   .. math::
    
      value1 + (value2 - value1) * (1 - (1 - amount)^{power})


.. function:: isin(value1, value2, amount)

   The inverse of the :func:`sin` function, using the following equation:

   .. math::
    
      value1 + (value2 - value1) * \left ( 1-\sin \left ( (1 - amount) * {\pi \over 2} \right ) \right )


.. function:: lerp(value1, value2, amount)

   This method performs the linear interpolation based on the following 
   formula.

   .. math::
    
      value1 + (value2 - value1) * amount

   Passing amount a value of 0 will cause value1 to be returned, a value of 1 
   will cause value2 to be returned.


.. function:: linear(value1, value2, amount)

   Alias for :func:`lerp`.


.. function:: sin(value1, value2, amount)

   Performs a sin interpolation using the following equation:

   .. math::
    
      value1 + (value2 - value1) * \sin \left ( amount * {\pi \over 2} \right )


.. function:: smoothstep(value1, value2, amount, power=1)

   Interpolates between two values using a recursive formula:

   .. math::
    
      amount = value1 + (value2 - value1) * (amount^2 * (3 - 2 * amount))

   This formula is repeated ``power`` times.
