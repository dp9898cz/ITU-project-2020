import 'package:postgres/postgres.dart';

import '../models/fault.dart';
import '../models/discovery.dart';

class HelperDB {
  static PostgreSQLConnection _getConnection() {
    return PostgreSQLConnection(
      "ec2-46-137-177-160.eu-west-1.compute.amazonaws.com",
      5432,
      "d9m4ru2ru00bk5",
      username: "hvahcpphomtrwf",
      password:
          "65e5d855c2ce0cec911a4ad1234bcbde34aaeca3e5245d54ffcaa0b9bee63679",
      useSSL: true,
    );
  }

  static Future<List<Map<String, dynamic>>> getDoneCleanup() async {
    var connection = _getConnection();
    await connection.open();
    List<
        Map<
            String,
            Map<String,
                dynamic>>> results = await connection.mappedResultsQuery(
        "SELECT * FROM Cleanup NATURAL JOIN Room WHERE Completed IS NOT NULL");
    connection.close();
    for (final row in results) {
      print(row);
    }
    return results;
  }

  static Future<List<Map<String, dynamic>>> getToDoCleanup() async {
    var connection = _getConnection();
    await connection.open();
    List<Map<String, Map<String, dynamic>>> results =
        await connection.mappedResultsQuery(
            "SELECT * FROM Cleanup NATURAL JOIN Room WHERE Completed IS NULL");
    connection.close();
    for (final row in results) {
      print(row);
    }
    return results;
  }

  static Future<void> makeCleanupDone(int cleanupId) async {
    var connection = _getConnection();
    await connection.open();
    await connection.query(
      "UPDATE Cleanup SET (Completed, Id) = (@date, @idd) WHERE id = @id",
      substitutionValues: {
        "date": DateTime.now(),
        "id": cleanupId,
        "idd": cleanupId,
      },
    );
    connection.close();
  }

  static Future<void> makeCleanupUnDone(int cleanupId) async {
    var connection = _getConnection();
    await connection.open();
    await connection.query(
      "UPDATE Cleanup SET (Completed, Id) = (null, @idd) WHERE id = @id",
      substitutionValues: {
        "id": cleanupId,
        "idd": cleanupId,
      },
    );
    connection.close();
  }

  static Future<void> insertFault(Fault f) async {
    var connection = _getConnection();
    await connection.open();
    var result = await connection.query(
      "SELECT id FROM Room WHERE number = @num",
      substitutionValues: {
        "num": f.roomNumber,
      },
    );
    if (result.isEmpty) {
      connection.close();
      return;
    }
    var roomIdList = result.map((e) => e[0]).toList();
    int roomId = roomIdList[0];
    await connection.query(
      "INSERT INTO Fault (room_id, description) VALUES (@id, @desc)",
      substitutionValues: {
        "id": roomId,
        "desc": f.description,
      },
    );
    connection.close();
  }

  static Future<void> insertDiscovery(Discovery d) async {
    var connection = _getConnection();
    await connection.open();
    var result = await connection.query(
      "SELECT id FROM Room WHERE number = @num",
      substitutionValues: {
        "num": d.roomNumber,
      },
    );
    if (result.isEmpty) {
      connection.close();
      return;
    }
    var roomIdList = result.map((e) => e[0]).toList();
    int roomId = roomIdList[0];
    await connection.query(
      "INSERT INTO Discovery (room_id, description) VALUES (@id, @desc)",
      substitutionValues: {
        "id": roomId,
        "desc": d.description,
      },
    );
    connection.close();
  }
}
