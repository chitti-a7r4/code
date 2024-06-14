void main() {
  List scores = [0, 20, 18, 4, 4, "HI", 3];
  print(scores[4]);

  scores.add(200);
  scores.remove(20);
  scores.removeLast();
  // scores.shuffle; shuffles the list
  // scores.indexOf; finds index
  print(scores.indexOf(4));
}
