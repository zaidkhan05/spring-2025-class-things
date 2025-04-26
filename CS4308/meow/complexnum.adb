
package body complexnum is
   function Add(A, B : Complex) return Complex is
   begin
      return (A.Real + B.Real, A.Imag + B.Imag);
   end Add;

   function Subtract(A, B : Complex) return Complex is
   begin
      return (A.Real - B.Real, A.Imag - B.Imag);
   end Subtract;

   function Multiply(A, B : Complex) return Complex is
   begin
      return ((A.Real * B.Real - A.Imag * B.Imag), (A.Real * B.Imag + A.Imag * B.Real));
   end Multiply;

   function Divide(A, B : Complex) return Complex is
      Denom : Float := B.Real * B.Real + B.Imag * B.Imag;
   begin
      return ((A.Real * B.Real + A.Imag * B.Imag) / Denom, (A.Imag * B.Real - A.Real * B.Imag) / Denom);
   end Divide;

   procedure Print_Complex(C : Complex) is
   begin
      Put_Line(Float'Image(C.Real) & " + " & Float'Image(C.Imag) & "i");
   end Print_Complex;
end complexnum;
