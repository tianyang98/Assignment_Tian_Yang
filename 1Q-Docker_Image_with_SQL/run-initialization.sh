# Wait to be sure that SQL Server came up
sleep 30s

# Run the scripts to create the DB and the schema in the DB
# Note: make sure that your password matches what is in the Dockerfile
/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P CorrectPasswordForVisualBI$ -d master -i 01-create-database.sql
/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P CorrectPasswordForVisualBI$ -d master -i 02-create-table.sql
/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P CorrectPasswordForVisualBI$ -d master -i 03-insert-data.sql