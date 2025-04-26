public class mai {
    public static void main(String[] args) {
        // Declare and initialize an Object array.
        // This array can hold any type of object.
        Object[] mixedArray = new Object[4];

        // Assign different types of elements
        mixedArray[0] = "Hello";     // String
        mixedArray[1] = 42;          // Integer (autoboxed from int)
        mixedArray[2] = 3.14;        // Double (autoboxed from double)
        mixedArray[3] = new Person("Alice", 30); // Custom object of type Person

        // Iterate and print each element along with its type.
        for (Object element : mixedArray) {
            System.out.println("Element: " + element + " | Type: " + element.getClass().getSimpleName());
        }
    }
}

class Person {
    private String name;
    private int age;

    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    @Override
    public String toString() {
        return name + " (" + age + ")";
    }
}
