void main() {
  Map<int, String> planets = {
    1: "Mercury",
    2: "Venus",
    3: "Earth",
    4: "Mars",
    5: "Jupiter",
    7: "Saturn",
    8: "Neptune",
    9: "Pluto"
  };
  planets[6] = "Uranus";
  //to remove the things after : , use keys only , values wont work
  var Removedplanet = (planets.remove(9));
  planets.removeWhere((key, value) {
    return key % 2 != 0;
  });
  print(planets);
  print("$Removedplanet is removed");
}
