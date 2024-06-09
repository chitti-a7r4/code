public class doorCode {
    public static void main(String[] args) {
        int passKey = 2580;
        int inputKey = 1234;
        if(inputKey==passKey){
            System.out.println("Door opened");
        }
        else{
            System.out.println("Wrong key");
        }
    }
    
}
