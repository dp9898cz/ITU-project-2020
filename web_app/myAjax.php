<?php
# This function reads your DATABASE_URL config var and returns a connection
# string suitable for pg_connect. Put this in your app.
function pg_connection_string_from_database_url() {
  extract(parse_url($_ENV["DATABASE_URL"]));
  return "user=hvahcpphomtrwf password=65e5d855c2ce0cec911a4ad1234bcbde34aaeca3e5245d54ffcaa0b9bee63679 host=ec2-46-137-177-160.eu-west-1.compute.amazonaws.com dbname=d9m4ru2ru00bk5 " . substr($path, 1); # <- you may want to add sslmode=require there too
}

# Here we establish the connection. Yes, that's all.
$pg_conn = pg_connect(pg_connection_string_from_database_url());

# Now let's use the connection for something silly just to prove it works:
$result = pg_query($pg_conn, "SELECT number FROM room;");

print "<pre>\n";
if (!pg_num_rows($result)) {
  print("Your connection is working, but your database is empty.\nFret not. This is expected for new apps.\n");
} else {
  print "Tables in your database:\n";
  while ($row = pg_fetch_row($result)) { print("- $row[0]\n"); }
}
print "\n";
?>