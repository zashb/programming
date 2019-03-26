--Courses: CourseID*, CourseName, TeacherID
--Teachers: TeacherID*, TeacherName
--Students: StudentID*, StudentName
--StudentCourses: CourseID * , StudentID *

-- Implement a query to get a list of all students and how many courses each student is enrolled in.

/* Solution 1 inner query*/
select StudentName, StudentID, cnt
from(
    select s.StudentID, count(sc.CourseID) as cnt
    from Students as s left join StudentCourses as sc
    on s.StudentID = sc.StudentID
    group by s.StudentID
) T inner join Students as s1
on T.StudentID = s1.StudentID

/* Solution 2: Add StudentName to GROUP BY clause. */
SELECT StudentName, Students.StudentID, count(StudentCourses.CourseID) as [Cnt]
FROM Students LEFT JOIN StudentCourses
ON Students.StudentID = StudentCourses.StudentID
GROUP BY Students.StudentID, Students.StudentName

-- Implement a query to get a list of all teachers and how many students they each teach. If a teacher teaches the same student in two courses, you should double count the student. Sort the list in descending order of the number of students a teacher teaches.

select TeacherName, isnull(studentsize.cnt,0)
from Teachers left join (
    select TeacherID, count(StudentID) as cnt
    from Courses inner join StudentCourses
    on Courses.CourseID = StudentCourses.CourseID
    group by TeacherID
) studentsize
on Teachers.TeacherID = studentsize.TeacherID
order by studentsize.cnt desc