void main() async {
  final post = await fetchPost();
  print(post.name);
  print(post.userId);
}

Future<Post> fetchPost() {
  const delay = Duration(seconds: 3);
  return Future.delayed((delay), () {
    return Post('shiva', 32);
  });
}

class Post {
  String name;
  int userId;
  Post(this.name, this.userId);
}
