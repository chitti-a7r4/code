public class javamath {
    public static void main(String[] args) {
         int number = 20;
         float square = (float)Math.sqrt(number); //this is to find squareroot
         System.out.println(square);

         int randomNo = (int)(Math.random()*101); //to get a random no from 0 to 100 we are using Math.random(), its range is [0,1) , so we are multiplying by 101
         System.out.println(randomNo);
         
         
        
    }
    
}
