import 'package:flutter/material.dart';
import 'package:rentel/models/discovery.dart';

import '../models/discovery.dart';
import '../helpers/database.dart';

class Lost extends StatefulWidget {
  static const routeName = '/lost';
  @override
  _LostState createState() => _LostState();
}

class _LostState extends State<Lost> {
  final _formKey = GlobalKey<FormState>();

  var _numberController = TextEditingController();
  var _descriptionController = TextEditingController();

  void _completeForm() async {
    if (_formKey.currentState.validate()) {
      await HelperDB.insertDiscovery(
        Discovery(
          description: _descriptionController.text,
          date: DateTime.now(),
          roomNumber: int.parse(_numberController.text),
        ),
      );
      Navigator.of(context).pop();
    }
  }

  @override
  Widget build(BuildContext context) {
    final node = FocusScope.of(context);
    return Scaffold(
      appBar: AppBar(
        title: Text("Přidat nález"),
      ),
      body: Form(
        key: _formKey,
        child: Column(
          children: [
            Container(
              padding: EdgeInsets.fromLTRB(10, 10, 10, 0),
              child: TextFormField(
                controller: _numberController,
                keyboardType: TextInputType.number,
                style: TextStyle(
                  fontSize: 22,
                ),
                decoration: new InputDecoration(
                  labelText: "Číslo pokoje",
                  border: OutlineInputBorder(),
                ),
                validator: (value) {
                  if (value.isEmpty) {
                    return 'Prosím, zadejte číslo pokoje.';
                  } else if (double.parse(value, (e) => null) == null) {
                    return 'Zadejte číslo.';
                  }
                  return null;
                },
                onEditingComplete: () => node.nextFocus(),
                textInputAction: TextInputAction.next,
              ),
            ),
            Container(
              padding: EdgeInsets.fromLTRB(10, 10, 10, 0),
              child: TextFormField(
                controller: _descriptionController,
                style: TextStyle(
                  fontSize: 22,
                ),
                maxLines: 3,
                decoration: new InputDecoration(
                  labelText: "Popis nálezu",
                  border: OutlineInputBorder(),
                ),
                validator: (value) {
                  if (value.isEmpty) {
                    return 'Prosím, popište nález.';
                  } else if (value.length <= 5) {
                    return 'Popis nálezu je příliš stručný.';
                  }
                  return null;
                },
              ),
            ),
            Container(
              padding: EdgeInsets.fromLTRB(10, 10, 10, 0),
              margin: EdgeInsets.only(
                top: 10,
              ),
              child: ElevatedButton(
                onPressed: () {
                  node.unfocus();
                  _completeForm();
                },
                style: ButtonStyle(
                  backgroundColor: MaterialStateProperty.all<Color>(
                      Theme.of(context).accentColor),
                ),
                child: Text(
                  'ODESLAT',
                  style: TextStyle(
                    fontSize: 25,
                    color: Colors.black,
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
