CREATE SEQUENCE next_id START 1 INCREMENT 1;
CREATE TABLE students(
    student_id INT DEFAULT nextval('next_id') PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    enrollment_date DATE
)

INSERT INTO students (first_name, last_name,email,enrollment_date)
VALUES
    ('John','Doe','john.doe@example.com','2023-09-01'),
    ('Jane','Smith','jane.smith@example.com','2023-09-01'),
    ('Jim','Beam','jim.beam@example.com','2023-09-02');

CREATE FUNCTION getAllStudents()
returns table(student_id INT,first_name TEXT,last_name TEXT, email TEXT, enrollment_date DATE)
language plpgsql
AS
$$
begin
	return query
	select*
	from students;
end;
$$
CREATE FUNCTION addStudent(f_name TEXT, l_name TEXT, in_email TEXT, in_date DATE)
returns table(first_name TEXT,last_name TEXT, email TEXT, enrollment_date DATE)
language plpgsql
AS
$$
begin
	INSERT INTO students(first_name,last_name,email,enrollment_date)
	VALUES(f_name,l_name,in_email,in_date);
end;
$$;
SELECT* FROM addstudent('Michel','Gouombas-Lussamaki','michelgouombaslussam@cmail.carleton.ca','2019-09-04');