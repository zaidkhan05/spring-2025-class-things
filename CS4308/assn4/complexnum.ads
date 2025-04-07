package complexnum is
   -- Define a complex number type with real and imaginary parts.
   type Complex is record
      Re : Float;
      Im : Float;
   end record;

   -- Function prototypes for arithmetic operations.
   function Add (A, B : Complex) return Complex;
   function Subtract (A, B : Complex) return Complex;
   function Multiply (A, B : Complex) return Complex;
   function Divide (A, B : Complex) return Complex;
end complexnum;
