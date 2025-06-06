package javaProjects;
import java.util.Objects;
import java.util.Scanner;

class NoughtsNCrosses {
    public static void main(String[] args) {
        clear();
        Scanner scanner = new Scanner(System.in);
        int turn = 1;

        String[][] board = {{" "," "," "},{" "," "," "},{" "," "," "}};
        
        
        for (int move = 0; move < 9; move++) {
            Boolean win = displayBoard(board);
            if (win) {
                break;
            }

            System.out.println("Enter your move:");
            String input = scanner.nextLine();
            clear();
            if (input.length() != 2 || !isInt(input)) {
                move -= 1;
                continue;
            }

            int xcoord = Integer.parseInt(Character.toString(input.charAt(0)));
            int ycoord = Integer.parseInt(Character.toString(input.charAt(1)));

            if ((xcoord > 3 || xcoord < 0) || (ycoord > 3 || ycoord < 0)) {
                move -= 1;
                continue;

            } else if (board[ycoord-1][xcoord-1] != " ") {
                move -= 1;
                continue;
            }

            if (turn==1) {
                board[ycoord-1][xcoord-1] = "X";
                turn = 2;
            } else {
                board[ycoord-1][xcoord-1] = "O";
                turn = 1;
            }

        }
        scanner.close();
    }


    public static Boolean displayBoard(String[][] board) {
        for (int i = 0; i < board.length; i++) {
            if (i != 0) {
                System.out.print("-----------\n");
            }

            for (int j = 0; j < board[i].length-1; j++) {
                if (j == 0) {
                    System.out.print(" ");
                }
                System.out.print(board[i][j]+" | ");
            }
            
            System.out.print(board[i][2]+"\n");
        }

        String winner = winCondition(board);
        if (!Objects.equals(winner, " ")) {
            System.out.println(winner+" has won!");
            return true;
        }

        return false;
    }

    public static void clear() {
        System.out.print("\033[H\033[2J");
        System.out.flush();
    }

    public static boolean isInt(String str) {
        try {
            Integer.parseInt(str);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }

    public static String winCondition(String[][] board) {
        
        for (int i = 0; i < board.length; i++) {
            if (areEqual(board[i])) {
                return board[i][0];
            } 
            
            String[] row = {board[0][i], board[1][i], board[2][i]};
            if (areEqual(row)) {
                return board[0][i];
            }
        }
        
        String[] diagonal1 = {board[0][0], board[1][1], board[2][2]};
        String[] diagonal2 = {board[0][2], board[1][1], board[2][0]};
        if (areEqual(diagonal1) || areEqual(diagonal2)) {
            return board[1][1];
        }

        return " ";
    }

    public static boolean areEqual(String[] line) {

        return Objects.equals(line[0], line[1]) && Objects.equals(line[1], line[2]);
    }

}





