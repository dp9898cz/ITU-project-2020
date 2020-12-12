import 'package:flutter/foundation.dart';

class Discovery {
  final int roomNumber;
  final String description;
  final DateTime date;

  Discovery({
    @required this.description,
    @required this.date,
    @required this.roomNumber,
  });
}
