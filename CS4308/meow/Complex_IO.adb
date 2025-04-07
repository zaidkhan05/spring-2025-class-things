with Ada.Text_IO; use Ada.Text_IO;
with Complex_Types;

package body Complex_IO is
   procedure Read_Complex(C : out Complex_Types.Complex) is
   begin
      Put("Enter Real part: ");
      Get(C.Real);
      Put("Enter Imaginary part: ");
      Get(C.Imag);
   end Read_Complex;

   procedure Print_Complex(C : Complex_Types.Complex) is
   begin
      Put_Line(Float'Image(C.Real) & " + " & Float'Image(C.Imag) & "i");
   end Print_Complex;
end Complex_IO;