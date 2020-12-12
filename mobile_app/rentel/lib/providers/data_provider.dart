import 'package:flutter/foundation.dart';

import '../models/Cleanup.dart';
import '../helpers/database.dart';

class DataProvider with ChangeNotifier {
  List<Cleanup> _cleanups = [];

  List<Cleanup> get cleanups {
    return [..._cleanups];
  }

  List<Cleanup> _doneCleanups = [];

  List<Cleanup> get doneCleanups {
    return [..._doneCleanups];
  }

  /* void addRoom(String title, String type) {
    final newRoom = Cleanup(
      id: DateTime.now().toString(),
      title: title,
      type: type,
    );
    HelperDB.insert('rooms', {
      'id': newRoom.id,
      'title': newRoom.title,
      'type': newRoom.type,
    });
    _items.add(newRoom);
    notifyListeners();
  } */

  Future<void> fetchCleanups() async {
    final list = await HelperDB.getToDoCleanup();
    _cleanups = list
        .map(
          (e) => Cleanup(
            id: e['cleanup']['id'],
            room_number: e['room']['number'].toString(),
            room_id: e['cleanup']['room_id'],
            type: e['cleanup']['c_type'].toString(),
            room_type: e['room']['r_type'].toString(),
            to_be_completed:
                DateTime.parse(e['cleanup']['to_be_completed'].toString()),
          ),
        )
        .toList();
    notifyListeners();
  }

  Future<void> fetchDoneCleanups() async {
    final list = await HelperDB.getDoneCleanup();
    _doneCleanups = list
        .map(
          (e) => Cleanup(
            id: e['cleanup']['id'],
            room_number: e['room']['number'].toString(),
            room_id: e['cleanup']['room_id'],
            type: e['cleanup']['c_type'].toString(),
            room_type: e['room']['r_type'].toString(),
            to_be_completed:
                DateTime.parse(e['cleanup']['to_be_completed'].toString()),
            completed: DateTime.parse(e['cleanup']['completed'].toString()),
          ),
        )
        .toList();
    notifyListeners();
  }

/*   Future<void> fetchCompletedRooms() async {
    final list = await HelperDB.getDat('rooms');
    _items = list
        .map(
          (e) => Room(
            id: e['room']['id'].toString(),
            title: e['room']['number'].toString(),
            type: e['room']['room_type'].toString(),
          ),
        )
        .toList();
    notifyListeners();
  }
} */
}
