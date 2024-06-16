void main() {
  var biography = BookItem("Shoe dog", 299);
  var Story = BookItem("Magic tree house", 150);
  print(biography.goodlooking());
  print(Story.goodlooking());
}

class BookItem {
  String BookName;
  double Price;
  BookItem(this.BookName, this.Price);
  String goodlooking() {
    return "$BookName --> $Price";
  }
}
