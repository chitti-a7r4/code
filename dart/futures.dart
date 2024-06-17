void main() {
  FetchPost().then((p) {
    print(p.name);
    print(p.userId);
  });
}

Future<Post> FetchPost() {
  const delay = Duration(seconds: 2);
  return Future.delayed((delay), () {
    return Post('Shiva', 3232);
  });
}

class Post {
  String name;
  int userId;
  Post(this.name, this.userId);
}
