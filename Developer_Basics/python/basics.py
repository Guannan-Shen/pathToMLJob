# TODO: define main
def main():
    print("Hello World!")
    # TODO: define the global variable 
    global f 
    f = "global variable"
    print(f)

# # TODO: call main function
# if __name__ == "__main__":
#     main()

# TODO: delete defined variable 
del f

# TODO: use * argument to pass a variable number of multiple arguments 
def testFun(*num):
    print(sum(num))

testFun(1,2,3,4,5)