#!/bin/bash
# Ce script ajoute la configuration SSL à PostgreSQL

# Activer SSL dans PostgreSQL
echo "ssl = on" >> /var/lib/postgresql/data/postgresql.conf
echo "ssl_cert_file = '/var/lib/postgresql/certs/server.crt'" >> /var/lib/postgresql/data/postgresql.conf
echo "ssl_key_file = '/var/lib/postgresql/certs/server.key'" >> /var/lib/postgresql/data/postgresql.conf