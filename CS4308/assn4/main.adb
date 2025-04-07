with Ada.Text_IO;           use Ada.Text_IO;
with Complex_Numbers_Pkg;
with Input_Output_Pkg;
procedure Main is
   A, B, Result : Complex_Numbers_Pkg.Complex;
begin
   -- Read two complex numbers from the user.
   Input_Output_Pkg.Read_Complex("Enter the first complex number:", A);
   Input_Output_Pkg.Read_Complex("Enter the second complex number:", B);

   -- Perform addition.
   Result := Complex_Numbers_Pkg.Add(A, B);
   Input_Output_Pkg.Print_Complex("Addition result:", Result);

   -- Perform subtraction.
   Result := Complex_Numbers_Pkg.Subtract(A, B);
   Input_Output_Pkg.Print_Complex("Subtraction result:", Result);

   -- Perform multiplication.
   Result := Complex_Numbers_Pkg.Multiply(A, B);
   Input_Output_Pkg.Print_Complex("Multiplication result:", Result);

   -- Perform division.
   begin
      Result := Complex_Numbers_Pkg.Divide(A, B);
      Input_Output_Pkg.Print_Complex("Division result:", Result);
   exception
      when Constraint_Error =>
         Put_Line("Error: Division by zero encountered.");
   end;
end Main;
