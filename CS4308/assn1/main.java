



public class main {


    public static String convertBinaryToString(int binary) {
        char[] result = new char[32]; // Array to hold the bits (32 for a 32-bit integer)
        int index = 31; // Start filling the array from the last position
        boolean started = false; // To skip leading zeros

        for (int i = 31; i >= 0; i--) {
            // Extract the bit at position i using a bitwise AND
            int bit = (binary >> i) & 1;
            if (bit == 1) {
                started = true; // Start recording once we find the first '1'
            }
            if (started) {
                result[index--] = (char) (bit + '0'); // Convert the bit to a character '0' or '1'
            }
        }

        // Build the final string by trimming unused spaces
        return new String(result, index + 1, 31 - index);
    }

    public static void main(String[] args) {
        int i = 0b0110;

        String output = convertBinaryToString(i);

        System.out.println(output);
        System.out.println(i);

    }
}