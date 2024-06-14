void main() {
  List marks = [5, 20, 18, 4, 15, 19, 0];
  for (int mark in marks) {
    if (mark > 10) {
      print("Your score is $mark");
    } else {
      print("You are failed");
    }
  }
}
