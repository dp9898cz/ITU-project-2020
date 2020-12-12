import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import './screens/rooms_list.dart';
import './screens/report.dart';
import './screens/lost.dart';
import 'providers/data_provider.dart';
import './screens/completed.dart';
import './screens/login_screen.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider.value(
      value: DataProvider(),
      child: MaterialApp(
        title: 'Great Places',
        theme: ThemeData(
          primarySwatch: Colors.brown,
          accentColor: Colors.orange,
        ),
        home: LoginScreen(),
        routes: {
          RoomList.routeName: (ctx) => RoomList(),
          Report.routeName: (ctx) => Report(),
          Lost.routeName: (ctx) => Lost(),
          CompletedRooms.routeName: (ctx) => CompletedRooms(),
        },
      ),
    );
  }
}
