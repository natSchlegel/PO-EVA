#### Crie um DB
```
sudo -u postgres createdb eva
```
#### Crie um usuário
```
sudo -u postgres createuser -P --interactive
>> user admin
>> senha admin
```
#### Mude o dono do DB
```
sudo -i -u postgres
psql
alter database eva owner to admin;
```
