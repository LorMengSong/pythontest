import math
def equation(a,b,c):
    delta = b * b - 4 * a * c;
    sqrt_delta = math.sqrt(abs(delta));
    if delta>0 :
        print('Two roots')
        x1 = (-b - sqrt_delta)/(2*a)
        x2 = (-b + sqrt_delta)/(2*a)
        print('root1: ',round(x1,3));
        print('root2: ',round(x2,3));
    elif delta == 0 : 
        print('Only one root');
        x = -b/(2*a);
        print('x=',round(x,3));
    else :
        print('Complex Roots');
        real = round(-b/(2*a),3)
        imaginary = round(sqrt_delta/(2*a),3)
        print(real,'+',imaginary,'i')
        print(real,'-',imaginary,'i') 
   
if __name__ == '__main__':
    a = float(input("Enter A: "))
    b = float(input("Enter B: "))
    c = float(input("Enter C: "))
    if a == 0:
        print("Not a second degree equarion");
    else:
        equation(a, b, c)    
