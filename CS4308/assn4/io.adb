with Ada.Text_IO;         use Ada.Text_IO;
with Ada.Float_Text_IO;   use Ada.Float_Text_IO;
with Complex_Numbers_Pkg; use Complex_Numbers_Pkg;

package body Input_Output_Pkg is

   procedure Read_Complex (Prompt : String; Value : out Complex) is
   begin
      Put_Line(Prompt);
      Put("Real part: ");
      Get(Value.Re);
      New_Line;
      Put("Imaginary part: ");
      Get(Value.Im);
      New_Line;
   end Read_Complex;

   procedure Print_Complex (Message : String; Value : Complex) is
   begin
      Put_Line(Message);
      Put_Line(Float'Image(Value.Re) & " + " & Float'Image(Value.Im) & "i");
      New_Line;
   end Print_Complex;

end Input_Output_Pkg;
