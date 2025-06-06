USE UNIVERSITY;
GO

-- Төменде сұранысты жаз
-- SELECT 
--     S.StudentID, 
--     S.StudentFname, 
--     S.StudentLname, 
--     SUM(CR.Credits) AS Rex
-- FROM tbLSTUDENT S
-- JOIN tblCLASS_LIST CL ON S.StudentID = CL.StudentID
-- JOIN tblCLASS CS ON CL.ClassID = CS.ClassID
-- JOIN tblQUARTER Q ON CS.QuarterID = Q.QuarterID
-- JOIN tblCOURSE CR ON CS.CourseID = CR.CourseID
-- JOIN tblDEPARTMENT D ON CR.DeptID = D.DeptID
-- WHERE 
--     Q.QuarterName = 'Spring'
--     AND D.DeptName LIKE 'Math%'
--     AND CS.Year >= 1996
-- GROUP BY 
--     S.StudentID, S.StudentFname, S.StudentLname
-- HAVING 
--     SUM(CR.Credits) > 10
-- ORDER BY 
--     Rex DESC;

SELECT *
FROM tblSTUDENT
WHERE StudentBirth > DateAdd(Year, -75, GetDate())

SELECT GETDATE()