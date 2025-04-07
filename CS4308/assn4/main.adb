with Ada.Text_IO;           use Ada.Text_IO;
with complexnum;
with io;
procedure Main is
   A, B, Result : complexnum.Complex;
begin
   -- Read two complex numbers from the user.
   io.Read_Complex("Enter the first complex number:", A);
   io.Read_Complex("Enter the second complex number:", B);

   -- Perform addition.
   Result := complexnum.Add(A, B);
   io.Print_Complex("Addition result:", Result);

   -- Perform subtraction.
   Result := complexnum.Subtract(A, B);
   io.Print_Complex("Subtraction result:", Result);

   -- Perform multiplication.
   Result := complexnum.Multiply(A, B);
   io.Print_Complex("Multiplication result:", Result);

   -- Perform division.
   begin
      Result := complexnum.Divide(A, B);
      io.Print_Complex("Division result:", Result);
   exception
      when Constraint_Error =>
         Put_Line("Error: Division by zero encountered.");
   end;
end Main;
