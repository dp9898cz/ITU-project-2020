import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import 'package:provider/provider.dart';

import '../helpers/database.dart';
import '../providers/data_provider.dart';

class CompletedRooms extends StatefulWidget {
  static const routeName = '/completed';
  @override
  _CompletedRoomsState createState() => _CompletedRoomsState();
}

class _CompletedRoomsState extends State<CompletedRooms> {
  void _makeUnDone(int id) async {
    await HelperDB.makeCleanupUnDone(id);
    Provider.of<DataProvider>(context, listen: false).fetchDoneCleanups();
    Provider.of<DataProvider>(context, listen: false).fetchCleanups();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Hotové úkoly'),
      ),
      body: FutureBuilder(
        initialData: Center(
          child: CircularProgressIndicator(),
        ),
        future: Provider.of<DataProvider>(
          context,
          listen: false,
        ).fetchDoneCleanups(),
        builder: (context, snapshot) => Consumer<DataProvider>(
          child: Center(
            child: Text("Žádné hotové úkoly."),
          ),
          builder: (ctx, data, ch) => (data.doneCleanups.length <= 0)
              ? ch
              : ListView.separated(
                  separatorBuilder: (context, index) => Divider(
                    endIndent: 18,
                    indent: 18,
                    height: 10,
                  ),
                  itemCount: data.doneCleanups.length,
                  itemBuilder: (ctx, i) => ListTile(
                    leading: Container(
                      width: 60,
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          CircleAvatar(
                            maxRadius: 25,
                            minRadius: 20,
                            child: Text(
                              data.doneCleanups[i].room_number,
                              style: TextStyle(
                                fontSize: 22,
                                color: Colors.black,
                              ),
                            ),
                            backgroundColor: Theme.of(context).accentColor,
                          ),
                        ],
                      ),
                    ),
                    title: Text(
                      data.doneCleanups[i].type,
                      style: TextStyle(
                        fontSize: 18,
                      ),
                    ),
                    subtitle: Text(
                      DateFormat.Hm().format(data.doneCleanups[i].completed),
                    ),
                    trailing: Container(
                      width: 150,
                      child: ElevatedButton(
                        child: Text(
                          "Nedokončené",
                          style: TextStyle(
                            fontSize: 18,
                          ),
                        ),
                        onPressed: () => {
                          _makeUnDone(data.doneCleanups[i].id),
                        },
                      ),
                    ),
                    onTap: () {},
                  ),
                ),
        ),
      ),
    );
  }
}
