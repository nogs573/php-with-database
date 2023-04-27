<!DOCTYPE html>
<html>
<head>
	<title>My Page</title>
</head>
<body>
	<?php
		// Set up database connection variables
		$servername = "localhost";
		$username = "myusername";
		$password = "mypassword";
		$dbname = "DnD";

		// Create connection
		$conn = mysqli_connect($servername, $username, $password, $dbname);

		// Check connection
		if (!$conn) {
			die("Connection failed: " . mysqli_connect_error());
		}
		echo "Connected successfully<br><br>";

		// Define the variable
		$primaryKey = 'CreatureName';

		// Define the query
		$sql = "SELECT * FROM Creature ORDER BY $primaryKey DESC LIMIT 5";

		// Execute the query and get the result set
		$result = mysqli_query($conn, $sql);

		// Loop through the result set and print the data
		if (mysqli_num_rows($result) > 0) {
			while($row = mysqli_fetch_assoc($result)) {
				echo "PrimaryKey: " . $row["$primaryKey"] . " - HP: " . $row["HP"] . " - AC: " . $row["AC"] . "<br>";
			}
		} else {
			echo "0 results";
		}

		// Close the database connection
		mysqli_close($conn);
	?>

	<h1>Welcome to my page!</h1>
	<p>This is some content on my page.</p>

</body>
</html>