with Ada.Text_IO;
with Complex_Numbers;
use Ada.Text_IO;
use Complex_Numbers;

procedure Main is
   A, B, Result : Complex;
begin
   Put_Line("Enter first complex number (Real Imag): ");
   Get(A.Real);
   Get(A.Imag);

   Put_Line("Enter second complex number (Real Imag): ");
   Get(B.Real);
   Get(B.Imag);

   Put_Line("Results:");
   Result := Add(A, B);
   Put_Line("Addition: ");
   Print_Complex(Result);

   Result := Subtract(A, B);
   Put_Line("Subtraction: ");
   Print_Complex(Result);

   Result := Multiply(A, B);
   Put_Line("Multiplication: ");
   Print_Complex(Result);

   Result := Divide(A, B);
   Put_Line("Division: ");
   Print_Complex(Result);
end Main;
