void main() {
  var biography = BookItem("Shoe dog", 299);
  var story =
      Types(["Sci-fi", "Fiction", "History"], "Magic Tree house", 150.2);
  var motivational = BookItem("Rich dad , Poor Dad", 100);
  var Ullu = BookItem("Do Epic Shit", 200);

  print("$biography,$Ullu,$motivational,$story");

  var books =
      Collection<BookItem>("Catalogue", [biography, story, motivational, Ullu]);

  var random = books.ranndomItem();
  print(random);
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

class Collection<T> {
  String name;
  List<T> data;
  Collection(this.name, this.data);

  T ranndomItem() {
    data.shuffle();
    return data[0];
  }
}
