import 'package:flutter/material.dart';

import '../screens/rooms_list.dart';

class LoginScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final node = FocusScope.of(context);
    return Scaffold(
      appBar: AppBar(
        title: Text("Rentel - správa úklidů"),
      ),
      body: Padding(
        padding: EdgeInsets.all(10),
        child: ListView(
          children: <Widget>[
            Container(
              margin: EdgeInsets.only(
                top: 40,
                bottom: 20,
              ),
              alignment: Alignment.center,
              padding: EdgeInsets.all(10),
              child: Text(
                'Přihlášení',
                style: TextStyle(
                    color: Theme.of(context).colorScheme.primary,
                    fontWeight: FontWeight.w500,
                    fontSize: 30),
              ),
            ),
            Container(
              padding: EdgeInsets.all(10),
              child: TextField(
                onEditingComplete: () => node.nextFocus(),
                textInputAction: TextInputAction.next,
                decoration: InputDecoration(
                  border: OutlineInputBorder(),
                  labelText: 'Login',
                ),
              ),
            ),
            Container(
              padding: EdgeInsets.fromLTRB(10, 10, 10, 0),
              child: TextField(
                keyboardType: TextInputType.text,
                onSubmitted: (_) => {node.unfocus()},
                obscureText: true,
                decoration: InputDecoration(
                  border: OutlineInputBorder(),
                  labelText: 'Heslo',
                ),
              ),
            ),
            Container(
              margin: EdgeInsets.only(
                top: 25,
              ),
              height: 50,
              padding: EdgeInsets.fromLTRB(10, 0, 10, 0),
              child: RaisedButton(
                textColor: Colors.black,
                color: Theme.of(context).accentColor,
                child: Text(
                  'Přihlásit se',
                  style: TextStyle(
                    fontSize: 18,
                  ),
                ),
                onPressed: () {
                  Navigator.of(context)
                      .pushReplacementNamed(RoomList.routeName);
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}
