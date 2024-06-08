public class userscore {
    public static void main(String[] args) {
        
        int totalScore = 1000;
        int userScore = 900;
        float scorePerc = (float)userScore/totalScore * 100f;
        // since we are converting int to float should use (float) in front

        System.out.println("Your score is : "+ scorePerc);
    }
    
}
