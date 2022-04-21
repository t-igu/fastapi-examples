CREATE ROLE testuser PASSWORD 'password' SUPERUSER CREATEDB CREATEROLE;
ALTER ROLE testuser login;

GRANT ALL ON ALL TABLES IN SCHEMA public TO testuser;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public TO testuser;
GRANT ALL ON ALL FUNCTIONS IN SCHEMA public TO testuser;

create database djangodb;
create database testdb;


CREATE FUNCTION set_updated_at() RETURNS TRIGGER AS $$
BEGIN
    IF (TG_OP = 'UPDATE') THEN
        NEW.updated_at := now();
        return NEW;
    END IF;
END;
$$ LANGUAGE plpgsql;

create table public.t_department (
  id serial not null
  , name character varying(64) not null
  , created_at timestamp(6) without time zone default CURRENT_TIMESTAMP not null
  , updated_at timestamp(6) without time zone default CURRENT_TIMESTAMP not null
  , primary key (id)
);

CREATE TRIGGER trigger_department_updated_at BEFORE UPDATE ON t_department FOR EACH ROW EXECUTE PROCEDURE set_updated_at();

insert into t_department (name) values 
('人事部'),
('経理部'),
('総務部'),
('法務部'),
('情報システム部'),
('技術部'),
('営業部')
;

create table public.t_employee (
  id serial not null
  , name character varying(64)
  , birthday date
  , department_id integer not null
  , foreign key (department_id) references t_department(id)
  , created_at timestamp(6) without time zone default CURRENT_TIMESTAMP not null
  , updated_at timestamp(6) without time zone default CURRENT_TIMESTAMP not null
  , primary key (id)
);

CREATE TRIGGER trigger_employee_updated_at BEFORE UPDATE ON t_employee FOR EACH ROW EXECUTE PROCEDURE set_updated_at();
