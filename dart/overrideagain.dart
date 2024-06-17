void main() {
  var biography = BookItem("Shoe dog", 299);
  var story =
      Types(["Sci-fi", "Fiction", "History"], "Magic Tree house", 150.2);
  print(biography);
  print(story);
}

class BookItem {
  String bookName;
  double price;
  BookItem(this.bookName, this.price);
  String goodlooking() {
    return "$bookName --> $price";
  }

  @override
  String toString() {
    return goodlooking();
  }
}

class Types extends BookItem {
  List<String> categories;
  Types(this.categories, super.bookName, super.price);
  @override
  String goodlooking() {
    var goodlookingCategories = 'Category of:';
    for (final c in categories) {
      goodlookingCategories = '$goodlookingCategories $c';
    }
    return '$bookName --> $price \n$goodlookingCategories';
  }

  @override
  String toString() {
    return "Instance of Book : $bookName,$price,$categories";
  }
}
