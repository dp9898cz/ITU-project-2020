import 'package:flutter/foundation.dart';

class Cleanup {
  final int id;
  // ignore: non_constant_identifier_names
  final String room_number;
  // ignore: non_constant_identifier_names
  final int room_id;
  // ignore: non_constant_identifier_names
  final String room_type;
  final String type;
  final DateTime completed;
  // ignore: non_constant_identifier_names
  final DateTime to_be_completed;

  Cleanup({
    @required this.id,
    // ignore: non_constant_identifier_names
    @required this.room_number,
    @required this.type,
    // ignore: non_constant_identifier_names
    @required this.room_id,
    // ignore: non_constant_identifier_names
    @required this.room_type,
    // ignore: non_constant_identifier_names
    @required this.to_be_completed,
    this.completed,
  });
}
