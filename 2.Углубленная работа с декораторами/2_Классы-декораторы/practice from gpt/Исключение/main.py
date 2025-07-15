

def main():
    data = {'surname': 'Suleimenov', 'name' : 'Yeldos'}

    try:
        print(sdf)
        print(data['surname'])
        print(data['name'])
        
    except KeyError:
    
        sum = 1 + 1
        print(sum)

    except Exception:
        print("oops")
    finally:
        print("finished")


main()