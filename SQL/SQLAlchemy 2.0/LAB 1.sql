
--1. Write the SQL to determine the student born in the city of Seattle in 1976 
-- who received a grade between 3.3 and 3.6 in any class from the college of Engineering.

SELECT StudentFname, StudentLname, StudentPermCity, Grade, BuildingName, QuarterName,
	   [Year], CourseName, CollegeName
FROM tblSTUDENT S
	JOIN tblCLASS_LIST CL ON S.StudentID = CL.StudentID
	JOIN tblCLASS CS ON CL.ClassID = CS.ClassID
	JOIN tblCOURSE CR ON CS.CourseID = CR.CourseID
	JOIN tblQUARTER Q ON CS.QuarterID = Q.QuarterID
	JOIN tblDEPARTMENT D ON CR.DeptID = D.DeptID
	JOIN tblCOLLEGE COL ON D.CollegeID = COL.CollegeID
	JOIN tblCLASSROOM CM ON CS.ClassroomID = CM.ClassroomID
	JOIN tblBUILDING B ON CM.BuildingID = B.BuildingID
WHERE S.StudentPermCity LIKE 'Seattle%'
	  AND YEAR(S.StudentBirth) = 1976
	  AND CL.Grade BETWEEN 3.3 AND 3.6
	  AND COL.CollegeName = 'Engineering';

--------------------------------------------------------
-- 2. Write the SQL to determine the instructors from the state of ‘Michigan, MI’ or ‘Wisconsin, WI’
-- who were assigned to teach a PHYSICS class during the 1930s that was held
-- in a classroom type ‘small lecture hall’.
SELECT InstructorFName, InstructorLName, InstructorState, ClassroomTypeName, [YEAR], CourseName
FROM tblINSTRUCTOR T
	JOIN tblINSTRUCTOR_CLASS IC ON T.InstructorID = IC.InstructorID
	JOIN tblCLASS C ON C.ClassID = IC.ClassID
	JOIN tblCLASSROOM R ON R.ClassroomID = C.ClassroomID
	JOIN tblCLASSROOM_TYPE CR ON CR.ClassroomTypeID = R.ClassroomTypeID
	JOIN tblCOURSE CO ON CO.CourseID = C.CourseID
WHERE T.InstructorState IN ('Michigan, MI', 'Wisconsin, WI')
	  AND C.[YEAR] BETWEEN 1930 AND 1939
	  AND CR.ClassroomTypeName = 'small lecture hall'
	  AND CO.CourseName LIKE 'PHYS%';



---------------------------------------------------------------------------
-- 3. Write the SQL to find the students from the states of New York, California, 
-- or Texas who were assigned a dorm room of type ‘single-suite’ in the building of
-- Elm Hall beginning January 1, 2000.

SELECT StudentFname, StudentLname, StudentPermState, DRT.DormRoomTypeName, SR.BeginDate, BuildingName
FROM tblSTUDENT T
	JOIN tblSTUDENT_DORMROOM SR ON T.StudentID = SR.StudentID
	JOIN tblDORMROOM DR ON SR.DormRoomID = DR.DormRoomID
	JOIN tblBUILDING B ON DR.BuildingID = B.BuildingID
	JOIN tblDORMROOM_TYPE DRT ON DR.DormRoomTypeID = DRT.DormRoomTypeID
WHERE T.StudentPermState IN ('New York, NY', 'California, CA', 'Texas, TX')
	  AND DRT.DormRoomTypeName = 'Single-Suite'	
	  AND SR.BeginDate >= '2000-01-01'
	  AND B.BuildingName LIKE 'Elm Hall';

---------------------------------------------------------------------------

-- 4. Write the SQL to determine the staff hired in the position of 'Library Assistant'
-- by the college of Business (Foster) between 1996 and 1998.

SELECT ST.StaffFName, ST.StaffLName ,PositionName, c.CollegeName , cl.YEAR
FROM tblSTAFF_POSITION sp
JOIN tblPOSITION p ON sp.PositionID =  p.PositionID
JOIN tblDEPARTMENT d ON sp.DeptID = d.DeptID
JOIN tblCOLLEGE c ON d.CollegeID = c.CollegeID
JOIN tblCOURSE cr ON cr.DeptID = d.DeptID
JOIN tblCLASS cl ON cr.CourseID = cl.CourseID
JOIN tblSTAFF ST ON sp.StaffID = ST.StaffID
WHERE cl.YEAR BETWEEN 1996 AND 1998
 AND p.PositionName = 'Library Assistant' 
 AND c.CollegeName LIKE 'Business%';
---------------------------------------------------------------------- 
 
 -- 5. Write the SQL to determine which courses had classes that were held in classrooms located
 -- in buildings on Stevens Way during Winter quarter during the decade of 2000 - 2010.

SELECT CourseName, L.LocationName, Q.QuarterName, CL.YEAR
FROM tblCOURSE C
	  JOIN tblDEPARTMENT D ON C.DeptID = D.DeptID
	  JOIN tblCLASS CL ON C.CourseID = CL.CourseID
	  JOIN tblCLASSROOM CR ON CL.ClassroomID = CR.ClassroomID
	  JOIN tblBUILDING B ON CR.BuildingID = B.BuildingID
	  JOIN tblLOCATION L ON B.LocationID = L.LocationID
	  JOIN tblQUARTER Q ON CL.QuarterID = Q.QuarterID
WHERE L.LocationName LIKE 'Stevens Way'
	  AND Q.QuarterName = 'Winter'
	  AND CL.YEAR BETWEEN 2000 AND 2010;

------------------------------------------------------------------
-- 6. Write the SQL to determine the students from Florida that resided
-- on the 5th floor of a dormitory during the 1980s.


SELECT StudentFname, StudentLname, StudentPermState, D.DormRoomNumber
FROM tblSTUDENT S
	 JOIN tblSTUDENT_DORMROOM DR ON S.StudentID = DR.StudentID
	 JOIN tblDORMROOM D ON DR.DormRoomID = D.DormRoomID
WHERE D.DormRoomNumber LIKE '5%'
	  AND S.StudentPermState = 'Florida, FL'
	  AND YEAR(DR.BeginDate) = 1989
	  AND YEAR(DR.EndDate) >= 1980;


-- 7. Write the SQL to determine the students who had a class that was held 
-- in the building named 'Mary Gates Hall' during the quarter of spring in the year 2004 that met on Wednesdays.

SELECT StudentFname, StudentLname, B.BuildingName, Q.QuarterName, D.Day_Name, C.YEAR
FROM tblSTUDENT S
	JOIN tblCLASS_LIST CL ON CL.StudentID = S.StudentID
	JOIN tblCLASS C ON C.ClassID = CL.ClassID
	JOIN tblQUARTER Q ON Q.QuarterID = C.QuarterID
	JOIN tblCLASSROOM CR ON CR.ClassroomID = C.ClassroomID
	JOIN tblBUILDING B ON B.BuildingID = CR.BuildingID
	JOIN tblCLASSROOM_TYPE CT ON CT.ClassroomTypeID = CR.ClassroomTypeID
	JOIN tblSCHEDULE SC ON SC.ScheduleID = C.ScheduleID
	JOIN tblSCHEDULE_DAY SCD ON SC.ScheduleID = SCD.ScheduleID
	JOIN tblDAY D ON D.DayID = SCD.DayID
WHERE B.BuildingName LIKE 'Mary Gates Hall'
	AND Q.QuarterName = 'Spring'
	AND D.Day_Name = 'Wednesday'
	AND C.YEAR = 2004
