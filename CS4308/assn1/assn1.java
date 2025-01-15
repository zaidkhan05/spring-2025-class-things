import java.util.Scanner;

class ComplexNumber {
    private double real;
    private double imaginary;

    // Constructor
    public ComplexNumber(double real, double imaginary) {
        this.real = real;
        this.imaginary = imaginary;
    }

    // Getter methods
    public double getReal() {
        return real;
    }

    public double getImaginary() {
        return imaginary;
    }

    // Addition
    public ComplexNumber add(ComplexNumber other) {
        return new ComplexNumber(this.real + other.real, this.imaginary + other.imaginary);
    }

    // Subtraction
    public ComplexNumber subtract(ComplexNumber other) {
        return new ComplexNumber(this.real - other.real, this.imaginary - other.imaginary);
    }

    // Multiplication
    public ComplexNumber multiply(ComplexNumber other) {
        double realPart = this.real * other.real - this.imaginary * other.imaginary;
        double imaginaryPart = this.real * other.imaginary + this.imaginary * other.real;
        return new ComplexNumber(realPart, imaginaryPart);
    }

    // Division
    public ComplexNumber divide(ComplexNumber other) {
        double denominator = other.real * other.real + other.imaginary * other.imaginary;
        if (denominator == 0) {
            throw new ArithmeticException("Division by zero is not allowed.");
        }
        double realPart = (this.real * other.real + this.imaginary * other.imaginary) / denominator;
        double imaginaryPart = (this.imaginary * other.real - this.real * other.imaginary) / denominator;
        return new ComplexNumber(realPart, imaginaryPart);
    }

    // Display complex number
    @Override
    public String toString() {
        return real + " + " + imaginary + "i";
    }
}

public class assn1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input for first complex number
        System.out.print("Enter the real part of the first complex number: ");
        double real1 = scanner.nextDouble();
        System.out.print("Enter the imaginary part of the first complex number: ");
        double imaginary1 = scanner.nextDouble();
        ComplexNumber num1 = new ComplexNumber(real1, imaginary1);

        // Input for second complex number
        System.out.print("Enter the real part of the second complex number: ");
        double real2 = scanner.nextDouble();
        System.out.print("Enter the imaginary part of the second complex number: ");
        double imaginary2 = scanner.nextDouble();
        ComplexNumber num2 = new ComplexNumber(real2, imaginary2);

        // Perform operations
        System.out.println("\nResults:");
        System.out.println("Addition: " + num1.add(num2));
        System.out.println("Subtraction: " + num1.subtract(num2));
        System.out.println("Multiplication: " + num1.multiply(num2));
        try {
            System.out.println("Division: " + num1.divide(num2));
        } catch (ArithmeticException e) {
            System.out.println("Division: " + e.getMessage());
        }

        scanner.close();
    }
}
