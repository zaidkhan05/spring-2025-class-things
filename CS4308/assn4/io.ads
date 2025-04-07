with Complex_Numbers_Pkg;

package Input_Output_Pkg is
   procedure Read_Complex (Prompt : String; Value : out Complex_Numbers_Pkg.Complex);
   procedure Print_Complex (Message : String; Value : Complex_Numbers_Pkg.Complex);
end Input_Output_Pkg;
