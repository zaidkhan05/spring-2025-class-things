package complexnum is
   type Complex is record
      Real : Float;
      Imag : Float;
   end record;

   function Add(A, B : Complex) return Complex;
   function Subtract(A, B : Complex) return Complex;
   function Multiply(A, B : Complex) return Complex;
   function Divide(A, B : Complex) return Complex;
   procedure Print_Complex(C : Complex);
end complexnum;