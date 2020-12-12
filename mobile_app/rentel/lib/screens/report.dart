import 'package:flutter/material.dart';

import "../models/fault.dart";
import "../helpers/database.dart";

class Report extends StatefulWidget {
  static const routeName = '/report';
  @override
  _ReportState createState() => _ReportState();
}

class _ReportState extends State<Report> {
  final _formKey = GlobalKey<FormState>();

  var _numberController = TextEditingController();
  var _descriptionController = TextEditingController();

  void _completeForm() async {
    if (_formKey.currentState.validate()) {
      await HelperDB.insertFault(
        Fault(
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
        title: Text("Nahlásit závadu"),
      ),
      body: Padding(
        padding: const EdgeInsets.all(10),
        child: Form(
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
                    border: OutlineInputBorder(),
                    labelText: "Popis závady",
                  ),
                  validator: (value) {
                    if (value.isEmpty) {
                      return 'Prosím, popište závadu.';
                    } else if (value.length <= 9) {
                      return 'Popis závady je příliš stručný.';
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
      ),
    );
  }
}
