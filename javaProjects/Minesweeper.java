package javaProjects;

import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Minesweeper {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[][] field = {
            {"?", "?", "?", "?", "?", "?", "?", "?", "?"},
            {"?", "?", "?", "?", "?", "?", "?", "?", "?"},
            {"?", "?", "?", "?", "?", "?", "?", "?", "?"},
            {"?", "?", "?", "?", "?", "?", "?", "?", "?"},
            {"?", "?", "?", "?", "?", "?", "?", "?", "?"},
            {"?", "?", "?", "?", "?", "?", "?", "?", "?"},
            {"?", "?", "?", "?", "?", "?", "?", "?", "?"},
            {"?", "?", "?", "?", "?", "?", "?", "?", "?"},
        };

        // first dig

        int xcoord;
        int ycoord;

        while (true) {

            printBoard(field);
            System.out.println("\nEnter your move: ");
            String input = scanner.nextLine();
            clear();

            if (input.length() != 2 || !isInt(input)) {
                continue;
            }

            xcoord = Integer.parseInt(Character.toString(input.charAt(0)));
            ycoord = Integer.parseInt(Character.toString(input.charAt(1)));

            if ((xcoord > 9 || xcoord < 0) || (ycoord > 8 || ycoord < 0)) {
                continue;
            } 
            else {break;}
        }

        String[][] bombLayout;
        while (true) {
            bombLayout = generateBombs(field);
            if (bombLayout[ycoord-1][xcoord-1] == " ") {
                break;
            }
        }

        //field = digHandler(field, bombLayout, xcoord-1, ycoord-1);
        printBoard(field);
        scanner.close();
    }

    public static void printBoard(String[][] field) {
        clear();
        System.out.println("minesweeper\n");
        System.out.print("  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |\r\n" +
                        "--|---|---|---|---|---|---|---|---|---|-");
        for (int i = 0; i < 8; i++) {

            System.out.print("\n "+(i+1)+"|");
            for (int j = 0; j < field.length; j++) {
                System.out.print(" "+field[i][j]+"  ");
            }
            System.out.print(" "+field[i][8]+" |");

            if (i == 7) {System.out.print("\n--|---|---|---|---|---|---|---|---|---|-");} 
            else {System.out.print("\n--|                                   |-");}
        }
    }

    public static String[][] digHandler(String[][] field, String[][] bombLayout, int x, int y) {
        if (isInt(bombLayout[y][x])) {
            field[y][x] = bombLayout[y][x];
        } else if (bombLayout[y][x] == " ") {
            List<int[]> aliveTiles = new ArrayList<>();
            List<int[]> deadTiles = new ArrayList<>();
            int[] position = {x, y};
            aliveTiles.add(position);

            while (true) {
                if (aliveTiles.size() == 0) {
                    break;
                }
                position = aliveTiles.get(0);
                aliveTiles.remove(0);
                field[position[1]][position[0]] = bombLayout[position[1]][position[0]];
                deadTiles.add(position);

                int[][] directions = {{1, 1}, {1, 0}, {1, -1}, {0, -1}, {-1, -1}, {-1, 0}, {-1, 1}, {0, 1}};
                for (int[] direction : directions) {
                    int newX = position[0] + direction[0];
                    int newY = position[1] + direction[1];
                    int[] newpos = {newX, newY};

                    if (newX >= 0 && newX < field[position[1]].length && newY >= 0 && newY < field.length) {
                        if (bombLayout[newY][newX].equals(" ") && !containsPosition(deadTiles, newpos)) {
                            aliveTiles.add(new int[]{newX, newY});
                        }
                    }
                }
            }

        }

        return field;
    }

    public static String[][] generateBombs(String[][] field) {
        Random random = new Random();
        String[][] bombLayout = field.clone();
        for (int y = 0; y < bombLayout.length; y++) {
            Arrays.fill(bombLayout[y], " ");
        }

        int[][] directions = {{1, 1}, {1, 0}, {1, -1}, {0, -1}, {-1, -1}, {-1, 0}, {-1, 1}, {0, 1}};

        for (int i = 0; i < 7; i++) {
            int x = random.nextInt(9);
            int y = random.nextInt(8);

            if (bombLayout[y][x] == " ") {
                bombLayout[y][x] = "*";
            } else {
                i--;
            }
        }

        for (int i = 0; i < bombLayout.length; i++) {
            for (int j = 0; j < bombLayout[i].length; j++) {
                if (bombLayout[i][j] == "*") {
                    for (int[] direction : directions) {
                        int newX = j + direction[0];
                        int newY = i + direction[1];

                        if (newX >= 0 && newX < bombLayout[i].length && newY >= 0 && newY < bombLayout.length) {
                            if (bombLayout[newY][newX] != "*") {
                                if (bombLayout[newY][newX] == " ") {
                                    bombLayout[newY][newX] = "1";
                                } else {
                                    int count = Integer.parseInt(bombLayout[newY][newX]);
                                    count++;
                                    bombLayout[newY][newX] = Integer.toString(count);
                                }
                            }
                        }
                    }
                }
            }
        }

        return bombLayout;
    }

    public static boolean containsPosition(List<int[]> list, int[] position) {
        for (int[] pos : list) {
            if (Arrays.equals(pos, position)) {
                return true;
            }
        }
        return false;
    }

    public static boolean isInt(String str) {
        try {
            Integer.parseInt(str);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }

    public static void clear() {
        System.out.print("\033[H\033[2J");
        System.out.flush();
    }
}
