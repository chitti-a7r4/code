import 'package:http/http.dart' as http;
import 'dart:convert' as convert;

void main() async {
  final post = await fetchPost();
  print(post.title);
  print(post.userId);
  print(post.body);
}

Future<Post> fetchPost() async {
  var url = Uri.https('jsonplaceholder.typicode.com', '/posts/1');
  final response = await http.get(url);

  Map<String, dynamic> data = convert.jsonDecode(response.body);
  return Post(data["title"], data["userId"], data["body"]);
}

class Post {
  String title;
  int userId;
  String body;
  Post(this.title, this.userId, this.body);
}
