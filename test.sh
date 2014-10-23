#!/bin/bash -ex

sudo fig up -d
sleep 3

ssh_params="-i insecure_key -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no root@localhost -p 2201"
ssh ${ssh_params} -t "cd /tests && nosetests --verbose"
ssh ${ssh_params} -t "smbclient //samba/test_share_1 --user=guest --no-pass -c \"get test_file test_file\" && ls -lh test_file"

