public class logicop{
    public static void main(String[] args) {
        int x = 2;
        int y = 3;
        int z = 4;
        boolean great = x < y;
        boolean greater = y < z;
        System.out.println(great && greater);
        // for any one to be true use || 
    }
}