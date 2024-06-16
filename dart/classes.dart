void main() {
  var biography = BookItem("Shoe dog", 299);
  var Story = BookItem("Magic tree house", 150);
  print(biography.BookName);
  print(biography.Price);
  print(Story.BookName);
  print(Story.Price);
}

class BookItem {
  String BookName;
  double Price;
  BookItem(this.BookName, this.Price);
}
