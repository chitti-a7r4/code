void main() {
  List marks = [5, 20, 18, 4, 15, 19, 0];
  for (int mark in marks.where((k) => k > 10)) {
    //here k is just an element(dynamic) which is filtering
    print("Your score is $mark");
  }
}
