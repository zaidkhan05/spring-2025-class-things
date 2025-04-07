package body Complex_Numbers_Pkg is

   function Add (A, B : Complex) return Complex is
   begin
      return (Re => A.Re + B.Re, Im => A.Im + B.Im);
   end Add;

   function Subtract (A, B : Complex) return Complex is
   begin
      return (Re => A.Re - B.Re, Im => A.Im - B.Im);
   end Subtract;

   function Multiply (A, B : Complex) return Complex is
   begin
      return (Re => A.Re * B.Re - A.Im * B.Im,
              Im => A.Re * B.Im + A.Im * B.Re);
   end Multiply;

   function Divide (A, B : Complex) return Complex is
      Denom : Float := B.Re * B.Re + B.Im * B.Im;
   begin
      if Denom = 0.0 then
         raise Constraint_Error with "Division by zero is not allowed.";
      end if;
      return (Re => (A.Re * B.Re + A.Im * B.Im) / Denom,
              Im => (A.Im * B.Re - A.Re * B.Im) / Denom);
   end Divide;

end Complex_Numbers_Pkg;
