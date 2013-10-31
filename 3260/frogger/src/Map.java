import java.awt.Graphics;
import java.io.BufferedReader;
import java.io.FileReader;


public class Map implements Drawable{
	public char[][] grid;
	public Map(int x, int y){
		grid = new char[y][x];
		try {
			String strLine;
			BufferedReader in = new BufferedReader(new FileReader("map"));
			int i = 0;
			while ((strLine = in.readLine()) != null) {
				for (int j = 0; j < strLine.length(); j++) {
					grid[j][i] = strLine.charAt(j);
				}
				i++;
			}
			in.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	@Override
	public void draw(Graphics g) {
		System.out.println("hit");
	}
}
