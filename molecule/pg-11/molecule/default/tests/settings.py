DEB_PKG_VERSIONS = ["11+204-2.buster", "204-2.buster", "2:11-5.2.buster", "2:11-5.2.stretch", "204-2.stretch",
                    "11+204-2.stretch", "2:11-5.2.bionic", '11+204-2.bionic', "204-2.bionic", "2:11-5.2.cosmic",
                    "11+204-2.cosmic", "204-2.cosmic", "2:11-5.2.disco", "11+204-2.disco", "204-2.disco"]

DEB_PACKAGES = ["percona-postgresql-11", "percona-postgresql-client", "percona-postgresql",
                "percona-postgresql-client-11", "percona-postgresql-client-common",
                "percona-postgresql-contrib", "percona-postgresql-doc", "percona-postgresql-server-dev-all",
                "percona-postgresql-doc-11", "percona-postgresql-plperl-11", "percona-postgresql-common",
                "percona-postgresql-plpython3-11", "percona-postgresql-pltcl-11", "percona-postgresql-all",
                "percona-postgresql-server-dev-11", "percona-postgresql-11-dbgsym",
                "percona-postgresql-client-11-dbgsym", "percona-postgresql-plperl-11-dbgsym",
                "percona-postgresql-plpython3-11-dbgsym", "percona-postgresql-pltcl-11-dbgsym",
                "percona-postgresql-server-dev-11-dbgsym"]

RPM_PACKAGES = ["percona-postgresql11", "percona-postgresql11-contrib", "percona-postgresql-common",
                "percona-postgresql11-debuginfo", "percona-postgresql11-devel", "percona-postgresql11-docs",
                "percona-postgresql11-libs", "percona-postgresql11-llvmjit", "percona-postgresql11-plperl",
                "percona-postgresql11-plpython", "percona-postgresql11-pltcl", "percona-postgresql11-server",
                "percona-postgresql11-test", "percona-postgresql-client-common", "percona-postgresql11-debuginfo",
                "percona-postgresql11-debugsource", "percona-postgresql11-devel-debuginfo",
                "percona-postgresql11-libs-debuginfo", "percona-postgresql11-plperl-debuginfo",
                "percona-postgresql11-plpython-debuginfo", "percona-postgresql11-plpython3-debuginfo",
                "percona-postgresql11-pltcl-debuginfo", "percona-postgresql11-server-debuginfo",
                "percona-postgresql11-test-debuginfo"]

RPM7_PACKAGES = ["percona-postgresql11", "percona-postgresql11-contrib", "percona-postgresql-common",
                 "percona-postgresql11-debuginfo", "percona-postgresql11-devel", "percona-postgresql11-docs",
                 "percona-postgresql11-libs", "percona-postgresql11-llvmjit", "percona-postgresql11-plperl",
                 "percona-postgresql11-plpython", "percona-postgresql11-pltcl", "percona-postgresql11-server",
                 "percona-postgresql11-test", "percona-postgresql-client-common"]

DEB_FILES = ["/etc/postgresql/11/main/postgresql.conf", "/etc/postgresql/11/main/pg_hba.conf",
             "/etc/postgresql/11/main/pg_ctl.conf", "/etc/postgresql/11/main/pg_ident.conf"]

RHEL_FILES = ["/var/lib/pgsql/11/data/postgresql.conf", "/var/lib/pgsql/11/data/pg_hba.conf",
              "/var/lib/pgsql/11/data/pg_ident.conf"]

EXTENSIONS = ['xml2', 'tcn', 'plpython3u', 'pltcl', 'hstore', 'plperlu', 'plperl', 'ltree',
              'hstore_plperlu', 'dict_xsyn', 'autoinc', 'hstore_plpython3u','insert_username', 'intagg', 'adminpack',
              'intarray', 'cube', 'lo', 'jsonb_plperl', 'jsonb_plperlu', 'btree_gin', 'pgrowlocks',
              'bloom', 'seg', 'pageinspect', 'btree_gist', 'sslinfo', 'pg_visibility', 'refint',
              'jsonb_plpython3u', 'moddatetime', 'dict_int', 'pg_freespacemap',
              'pgstattuple', 'uuid-ossp', 'tsm_system_time', 'tsm_system_rows', 'unaccent',
              'tablefunc', 'pgcrypto', 'pg_buffercache', 'amcheck', 'citext',  'timetravel',  'isn',
              'ltree_plpython3u', 'fuzzystrmatch', 'earthdistance', 'hstore_plperl', 'pg_prewarm',
              'dblink', 'pltclu', 'file_fdw', 'pg_stat_statements', 'postgres_fdw']

LANGUAGES = ["pltcl", "pltclu", "plperl", "plperlu", "plpython3u"]