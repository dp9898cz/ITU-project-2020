import 'package:flutter/foundation.dart';

class Fault {
  final int roomNumber;
  final String description;
  final DateTime date;

  Fault({
    @required this.description,
    @required this.date,
    @required this.roomNumber,
  });
}
