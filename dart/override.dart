void main() {
  var biography = BookItem("Shoe dog", 299);
  var story = Types(["Sci-fi", "Fiction","History"], "Magic Tree house", 150.2);
  print(biography.goodlooking());
  print(story.goodlooking());
}

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

  String goodlooking() {
    var goodlookingCategories = 'Category of:';
    for (final c in categories) {
      goodlookingCategories = '$goodlookingCategories $c';
    }
    return '$bookName --> $price \n$goodlookingCategories';
  }
}
