#Exception Handling: Exception handling in python allows you to handle
# error gracefully and take corrective action without stopping the execution of the program.

# Exception: Exceptions are events that disrupt the normal flow of the program.
# They occur when an error is encountered during program execution.common exceptions include:
#ZeroDivisionError:Dividing by zero
#FileNotFoundError:File not found
#ValueError:Invalid value

try:
    a=b;
except:
    print('the varibale is not defined')

try:
    a=b;
except NameError as ex:
    print(ex);

try:
    num=int(input('enter a number'));
    result=10/num;
except ValueError:
    print("This is not a valid number");
except ZeroDivisionError:
    print("Enter Denominatior greator than zero")

#try,except,else
try:
    num=int(input("Enter a number"));
    result=10/num;
except ValueError:
    print('This is not a valid number')
except ZeroDivisionError:
    print("Enter Denominator greator than zero");
except Exception as ex:
    print(ex);
else:
    print(f'the result is {result}')


#try,except,else,finally

try:
    num=int(input('Enter a Number'));
    result=num/10;
except ValueError as ex:
    print(ex);
except ZeroDivisionError as ex:
    print(ex);
except Exception as ex:
    print(ex);
else:
    print(f'The result is {result}');
finally:
    print("Execution Complete.")


#File Handling and Exception Handling
try:
    file=open('example.txt','r');
    content=file.read()
    print(content)
except FileNotFoundError:
    print('The file does not exists')
finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print('file close')