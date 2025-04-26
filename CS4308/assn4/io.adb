with Ada.Text_IO;         use Ada.Text_IO;
with Ada.Float_Text_IO;   use Ada.Float_Text_IO;
with complexnum; use complexnum;

package body io is

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
      Put(Value.Re, Fore=>0, Aft=>3, Exp=>0);
      Put("+");
      Put(Value.Im, Fore=>0, Aft=>3, Exp=>0);
      Put("i");
      New_Line;
   end Print_Complex;

end io;
