
# Postgresql
table_name = 'HRMTABLE'
table_column_headers = ['ID', 'USERROLE', 'USERSTATUS', 'USERNAME', 'PASSWORD']

testdb=# create table HRM_ADMIN(ID int NOT NULL, USERROLE VARCHAR(20), USERSTATUS VARCHAR(20),                                                                                                  USERNAME VARCHAR(20), PASSWORD VARCHAR(20), Primary Key(ID));
CREATE TABLE
testdb=# \d hrm_admin
             Table "public.hrm_admin"
    Column    |         Type          | Modifiers
--------------+-----------------------+-----------
 id           | integer               | not null
 userrole     | character varying(20) |
 userstatus   | character varying(20) |
 username     | character varying(20) |
 password     | character varying(20) |
Indexes:
    "hrm_admin_pkey" PRIMARY KEY, btree (id)



# MongoDB


# ini file

