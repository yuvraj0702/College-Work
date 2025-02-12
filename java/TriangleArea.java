public class TriangleArea {
    
    public static double calculateArea(double base, double height) {
        return (base * height) / 2;
    }
    
    public static void main(String[] args) {
        double base = 5.0;
        double height = 4.0;
        
        double area = calculateArea(base, height);
        
        System.out.printf("The area of the triangle with base %.2f and height %.2f is: %.2f", base, height, area);
    }
}