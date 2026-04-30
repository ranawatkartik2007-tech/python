try:
    a = int(input(" enter a numnber"))
    print(f"number is {a}")
    
except ValueError as v:
    print(f"error is {v}")
    print(" value error occurred")
        
except Exception as e:
    print(f"error is {e}")
    
    
# finallyusecase
 
def main():
    try:
        a = int(input(" enter a numnber"))
        print(f"number is {a}")
    
    except ValueError as v:
        print(f"error is {v}")
        print(" value error occurred")
        
    except Exception as e:
        print(f"error is {e}")
        
    finally:
        print(" this will always execute")
        
main()
        
        
           