run: 
	@make clean
	@python stu_mean.py
	@clear
	@echo Entering the databse, enter \"SELECT \* FROM peeps_avg\" to view the table
	@sqlite3 database.db

clean:
	@if [ -f *.db ]; then \
		rm *.db; \
	fi;
