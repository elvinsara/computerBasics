<?php
include "connection.php";
$sql="select *from students";
$res=mysqli_query($connect,$sql);
if(mysqli_num_rows($res))
{
    echo '<table border="1" style="border-collapse:collapse" align="center" width="300" height="300">
    <tr><th>ROLLNO</th><th>NAME</th><th>GENDER</th><th>MARK</th></tr>';
    while($row=mysqli_fetch_assoc($res))
    {
        echo '<tr><td>'.$row["ROLLNO"].'</td><td>'.$row["NAME"].'</td><td>'.$row["GENDER"].'</td><td>'
        .$row["MARK"].'</td></tr>';
    }
    echo '</table>';
}
else
{
    echo '<script>alert("table is empty")</script>';
}