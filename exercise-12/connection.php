<?php
$servername="localhost";
$username="root";
$password="";
$dbname="sara";
$connect=mysqli_connect($servername,$username,$password,$dbname);
if(!$connect)
{
    echo "connection failed";
}
?>