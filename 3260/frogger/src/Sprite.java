import java.awt.Graphics2D;
import java.awt.GraphicsConfiguration;
import java.awt.GraphicsEnvironment;
import java.awt.Transparency;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.net.URL;

import javax.imageio.ImageIO;

/**
 * Sprite containing picture and position of objects
 * @author trevor
 * 
 */
public class Sprite {
	public double rot = 0;
	public int posX = 0;
	public int posY = 0;
	public int gridX = 0;
	public int gridY = 0;
	public boolean onGrid = true;
	public BufferedImage pic;

	/**
	 * creates a sprite with a specified picture
	 */
	public Sprite(URL im) {
		try {
			pic = ImageIO.read(im);
		} catch (IOException e) {
			System.out.println("cant open pic");
		}
	}
	
	/**
	 * Sets position of the sprite
	 */
	public void setPos(int[] x){
		posX=x[0];
		posY=x[1];
	}

	/**
	 * Checks if posx and posy are on the grid
	 */
	public void calcGrid() {
		/*int[] test = Board.board.getGridCo(this.posX, this.posY);
    	if(test[2]==0){
    		onGrid=true;
    		this.gridX=test[0];
    		this.gridY=test[1];
    	}else{
    		onGrid=false;
    	}*/
	}
	
	/**
	 * Rotates the image of the sprite to a certain degree
	 */
	public void rotate(double degree) {
		double angle = (rot-degree) / 180 * Math.PI;
		rot=degree;
		double sin = Math.abs(Math.sin(angle)), cos = Math.abs(Math.cos(angle));
		int w = pic.getWidth(), h = pic.getHeight();
		int neww = (int) Math.floor(w * cos + h * sin), newh = (int) Math
				.floor(h * cos + w * sin);
		GraphicsConfiguration gc = GraphicsEnvironment
				.getLocalGraphicsEnvironment().getDefaultScreenDevice()
				.getDefaultConfiguration();
		BufferedImage result = gc.createCompatibleImage(neww, newh,
				Transparency.TRANSLUCENT);
		Graphics2D g = result.createGraphics();
		g.translate((neww - w) / 2, (newh - h) / 2);
		g.rotate(angle, w / 2, h / 2);
		g.drawRenderedImage(pic, null);
		g.dispose();
		this.pic = result;
	}
}
