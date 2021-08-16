CREATE DEFINER=`root`@`localhost` PROCEDURE `Insertproduct`(
in barcode varchar(10),
in ProductName varchar(15),
in price int,
in quantityInStock int)
BEGIN
	 if price > 0 and quantityInStock >= 0 then
		insert into Product values(barcode,ProductName,price,quantityInStock);
     end if;
END