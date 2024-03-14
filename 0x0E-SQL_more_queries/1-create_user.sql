-- creates the MYSQL server user user_0d_1
-- user_0d_1 should have all privileges on your MySQL serve
-- The user_0d_1 password should be set to user_0d_1_pwd
-- If the user user_0d_1 already exists, your script should not fail
SELECT user FROM mysql.user WHERE user = 'user_0d_1';

IF @@rowcount = 0 THEN
	CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
	GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
END IF;