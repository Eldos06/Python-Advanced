def is_ascii(s: str) -> bool:
    try:
        s.encode("ascii")
        print(True) 
    except UnicodeEncodeError:
        print(False) 


is_ascii("hello") #→ True  
is_ascii("привет") #→ False  



