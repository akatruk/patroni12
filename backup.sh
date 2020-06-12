PWD="3+lB6L8rntVpY5ik0BPT+1MbRCNiltYTcFvXJ8H8A94="
export PGPORT="5432"
backup_dir=/backup/$env
host=M1K8STLDB03
db=lsp_coupon
env=prod
echo -e "\n\nBackup Status: $(date +"%T-%d-%m-%y")" >> $backup_dir/Status.log
PGPASSWORD=$PWD /usr/pgsql-12/bin/pg_dump -U $db -d $db -h $host | gzip -c > $backup_dir/$host_$(date +"%T-%d-%m-%y").tar.gz

retention_duration=14
find $backup_dir/$host* -type d -mtime +$retention_duration -exec rm -rv {} \;



PGPASSWORD="3+lB6L8rntVpY5ik0BPT+1MbRCNiltYTcFvXJ8H8A94=" /usr/pgsql-12/bin/pg_dump -U lsp_coupon -d lsp_coupon -h M1K8STLDB03 | gzip -c > /backup/prod/M1K8STLDB03_.tar.gz