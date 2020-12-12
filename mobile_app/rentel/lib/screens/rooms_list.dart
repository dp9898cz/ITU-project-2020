import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import 'package:provider/provider.dart';
import 'package:pull_to_refresh/pull_to_refresh.dart';
import 'package:rentel/helpers/database.dart';

import '../providers/data_provider.dart';
import '../screens/report.dart';
import '../screens/lost.dart';
import '../screens/completed.dart';

class RoomList extends StatefulWidget {
  static const routeName = '/cleanups';
  @override
  _RoomListState createState() => _RoomListState();
}

class _RoomListState extends State<RoomList> {
  RefreshController _controller = RefreshController(initialRefresh: false);

  void _onRefresh(BuildContext ctx) {
    Provider.of<DataProvider>(ctx, listen: false).fetchCleanups();
    _controller.refreshCompleted();
  }

  void _makeCleanupDone(int id) async {
    await HelperDB.makeCleanupDone(id);
    Provider.of<DataProvider>(context, listen: false).fetchCleanups();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Dnešní úkoly'),
        actions: [
          IconButton(
            icon: Icon(Icons.done_all_rounded),
            onPressed: () => {
              Navigator.of(context).pushNamed(CompletedRooms.routeName),
            },
          ),
          IconButton(
            icon: Icon(Icons.report_problem_outlined),
            onPressed: () => {
              Navigator.of(context).pushNamed(Report.routeName),
            },
          ),
          IconButton(
            icon: Icon(Icons.add_circle_outlined),
            onPressed: () => {
              Navigator.of(context).pushNamed(Lost.routeName),
            },
          )
        ],
      ),
      body: FutureBuilder(
        future: Provider.of<DataProvider>(
          context,
          listen: false,
        ).fetchCleanups(),
        builder: (context, snapshot) => Consumer<DataProvider>(
          child: Center(
            child: CircularProgressIndicator(),
          ),
          builder: (ctx, data, ch) => (data.cleanups.length <= 0)
              ? ch
              : SmartRefresher(
                  enablePullUp: false,
                  enablePullDown: true,
                  onRefresh: () => {_onRefresh(context)},
                  header: WaterDropMaterialHeader(
                    backgroundColor: Theme.of(context).accentColor,
                  ),
                  controller: _controller,
                  child: ListView.separated(
                    separatorBuilder: (context, index) => Divider(
                      endIndent: 18,
                      indent: 18,
                      height: 10,
                    ),
                    itemCount: data.cleanups.length,
                    itemBuilder: (ctx, i) => ListTile(
                      leading: Container(
                        width: 110,
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: [
                            Text(
                              DateFormat.Hm()
                                  .format(data.cleanups[i].to_be_completed),
                              style: TextStyle(fontSize: 17),
                            ),
                            CircleAvatar(
                              maxRadius: 25,
                              minRadius: 20,
                              child: Text(
                                data.cleanups[i].room_number,
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
                        data.cleanups[i].type,
                        style: TextStyle(
                          fontSize: 18,
                        ),
                      ),
                      subtitle: Text(data.cleanups[i].room_type),
                      trailing: Container(
                        width: 110,
                        child: ElevatedButton(
                          child: Text(
                            "HOTOVO",
                            style: TextStyle(
                              fontSize: 18,
                            ),
                          ),
                          onPressed: () =>
                              {_makeCleanupDone(data.cleanups[i].id)},
                        ),
                      ),
                      onTap: () {},
                    ),
                  ),
                ),
        ),
      ),
    );
  }
}
