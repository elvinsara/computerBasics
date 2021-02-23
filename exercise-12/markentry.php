<html>
<head></head>
<body>
<form action="markentry.php" method="post">
<table align="center" width="400" height="300">
<tr>
<th>Rollno</th>
<th><input type="text" name="rollno"/></th>
</tr>
<tr>
<th>Name</th>
<th><input type="text" name="name"/></th>
</tr>
<tr>
<th>gender</th>
<th><input type="radio" name="gender" value="male"/>Male<input type="radio" name="gender" value="female"/>Female</th>
</tr>
<tr>
<th>Mark</th>
<th><select name ="mark"><option value="select">Select</option>
<?php
for($i=0;$i<21;$i++)
{
    echo '<option value='.$i.'>'.$i.'</option>';
}
?>
</select>
</th>
</tr>
<tr>
<th><input type="submit" name="submit"/></th>
<th><input type="reset"/></th>
</tr>
</form>
</body>
</html>
<?php
include "connection.php";
if(isset($_POST["submit"]))
{
    $ROLLNO=$_POST["rollno"];
    $NAME=$_POST["name"];
    $GENDER=$_POST["gender"];
    $MARK=$_POST["mark"];
    $sql="insert into students values($ROLLNO,'$NAME','$GENDER',$MARK)";
    if(mysqli_query($connect,$sql))
    {
        echo '<script>alert("New record created")</script>';
    }
    else
    {
        echo "Error: " . $sql . "<br>" . mysqli_error($connect);
    }
    mysqli_close($connect);
}
?>
