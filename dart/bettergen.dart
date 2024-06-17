void main() {
  var icecream = Flavours(["Choco,Strawberry,Watermelon"], "Vanilla", 30);
  var pizza = MenuItem("pizza", 200);
  var burger = MenuItem("Chicken", 99);
  var desert = MenuItem("Black Forest", 50);

  print(icecream.format());
  print(pizza.format());
  print(burger.format());
  print(desert.format());

  var food = Collection<MenuItem>("Menu", [icecream]);
  var random = food.randomItem();
  print(random);
}

class MenuItem {
  String itemName;
  double price;

  MenuItem(this.itemName, this.price);

  String format() {
    return '$itemName --> $price';
  }

  @override
  String toString() {
    return format();
  }
}

class Flavours extends MenuItem {
  List<String> flavour;

  Flavours(this.flavour, super.itemName, super.price);
  @override
  String format() {
    var typesofflavours = 'The various flavours are:';

    for (final f in flavour) {
      typesofflavours = '$typesofflavours $f';
    }
    return '$itemName is ₹$price, and $typesofflavours';
  }

  @override
  String toString() {
    return 'Your random suggestion is : $itemName,$price,$flavour';
  }
}

class Collection<T> {
  String name;
  List<T> data;

  Collection(this.name, this.data);

  T randomItem() {
    data.shuffle();
    return data[0];
  }
}
