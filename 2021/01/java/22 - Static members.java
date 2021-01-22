//simple implementation of static members (they are shared with every object of the class)

class Main {
  public static void main(String[] args) {

    System.out.println(Player.getPlayerCount()); //before creating object of the class, static member can be accessed
    Player p1 = new Player("xyz");
    Player p2 = new Player("abc");
    p1.printDetails();
    p2.printDetails();

    System.out.println(Player.getPlayerCount());  //static members can be called via class name
    System.out.println(p1.getPlayerCount()); //this will also generate same o/p
  }
}


class Player {
  String name;
  int id;
  private static int playerCount = 0;  //it's advised to access and modify static members using static member methods

  Player (String name) {
    this.name = name;
    id = ++playerCount;
  }

  Player () {
    this("Not Available!")
    //id = ++playerCount;
  }
  void printDetails () {
    System.out.println(id + ": " + name);
  }

  static int getPlayerCount () {  //this static method can't call non-static members bit not vice versa (eg: Player constructor)
    return playerCount;
  }
}