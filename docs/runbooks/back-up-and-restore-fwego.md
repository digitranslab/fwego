# Back-up Fwego Runbook

## Backing Up Fwego
1. Please ensure you only back-up a Fwego database which is not actively being used
   by a running Fwego instance or any other process which is making changes to the 
   database.
2. Please create PGPASS file to store the password for your database, see
   https://www.postgresql.org/docs/11/libpq-pgpass.html for more details on this file. 
3. Please read and understand the output of `./fwego backup_fwego --help`
4. Run the following command to back-up Fwego.
    `PGPASSFILE=PATH_TO_YOUR_PGPASSFILE ./fwego backup_fwego -h YOUR_DB_HOST -d YOUR_DB_NAME -U YOUR_DB_USER -p YOUR_DB_PORT`

## Restoring Fwego
1. Please ensure you never restore Fwego using a pooled connection but instead do
   the restoration via direct database connection.
1. Make a new, empty database to restore the back-up file into, please do not overwrite
   existing databases as this might cause database inconsistency errors.
1. Get a fwego backup tar gz file produced by the `./fwego backup_fwego` command 
   and its file path.
1. Please create PGPASS file to store the password for your database, see
   https://www.postgresql.org/docs/11/libpq-pgpass.html for more details on this file.
1. Please read and understand the output of `./fwego restore_fwego --help`
1. To restore Fwego run the following command: 
   `PGPASSFILE=PATH_TO_YOUR_PGPASSFILE ./fwego restore_fwego -h YOUR_DB_HOST -d YOUR_FRESH_DB_TO_RESTORE_INTO -U YOUR_DB_USER -p YOUR_DB_PORT -f PATH_TO_BACKUP_TAR_GZ` 
