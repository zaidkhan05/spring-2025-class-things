with Complex_Types;
with Complex_Operations;
with Complex_IO;

use Complex_Types;
use Complex_Operations;
use Complex_IO;

procedure Main is
   A, B, Result : Complex;
begin
   Put_Line("Input for first complex number:");
   Read_Complex(A);
   Put_Line("Input for second complex number:");
   Read_Complex(B);

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