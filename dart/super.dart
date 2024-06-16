void main() {
  var biography = BookItem("Shoe dog", 299);
  var story = Types(["Sci-fi", "Fiction"], "Magic Tree house", 150.2);
  //here we take types rather than BookItem because we extended it
  print(biography.goodlooking());
  print(story.goodlooking());
}

//Imp --> start the identifier names in lower case
//only classes should be started with Capital letter
class BookItem {
  String bookName;
  double price;
  BookItem(this.bookName, this.price);
  String goodlooking() {
    return "$bookName --> $price";
  }
}

class Types extends BookItem {
  List<String> categories;
  Types(this.categories, super.bookName, super.price);
}
