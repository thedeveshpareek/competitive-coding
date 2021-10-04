package Assigment;

public class FastPiece extends Piece {

    public FastPiece(String name, String Color, int[] position) {
        super(name, Color, position);
    }
    @Override
    public String toString() {
        return "SlowPiece{" +
                "name='" + Name + '\'' +
                ", Color='" + Color + '\'' +
                ", position=" + position[0] + "," + position[1] +
                '}';
    }
    // method
    public void move(String direction, int n) {
        if (direction.equals("left")) {
            if (position[0] - n >= 0) {
                position[0] -= n;
            }
        } else if (direction.equals("right")) {
            if (position[0] + n <= 7) {
                position[0] += n;
            }
        }
    }
}
