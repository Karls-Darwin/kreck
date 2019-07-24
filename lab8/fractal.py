import turtle

def tree(t,trunklength):

    t.speed(8)
    if trunklength<5:
        return
    else:
        t.fd(trunklength)
        t.right(30)
        tree(t,trunklength-15)
        t.left(60)
        tree(t,trunklength-15)
        t.right(30)
        t.backward(trunklength)

def main():
    t=turtle.Turtle()
    tree(t,100)

if __name__ == '__main__':
    main()
