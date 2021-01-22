//basic implementation of "this" reference

class Point
{
    int x, y;
    
    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
    
    Point() {
    	this(10,10);  //used "this" for changing constructor and set values default
    }

    void print(){
        System.out.println(x + y);
    }

    Point setX(int x){
    	this.x = x;
    	return this;  //returning "this" ensures to add more functions in same line of code(LOC:36)
    }

    Point setY (int y){
    	this.y = y;
    	return this;
    }
}

class Main
{
    public static void main(String[] args) {
        Point p = new Point(10,20);
        p.print();
        p.setX(20).setY(30);
    }
}
