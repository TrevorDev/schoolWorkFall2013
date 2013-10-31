import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;


/**
	 * Gets the input from the keyboard
	 */
public class Input extends KeyAdapter {
	public static boolean up,down,left,right;
	public void keyPressed(KeyEvent e) {
		int key = e.getKeyCode();
		if ((key == KeyEvent.VK_LEFT)) {
			System.out.println("hit left");
			left = true;
			up = false;
			down = false;
			right = false;
		}

		if ((key == KeyEvent.VK_RIGHT)) {
			right = true;
			up = false;
			down = false;
			left = false;
		}

		if ((key == KeyEvent.VK_UP)) {
			up = true;
			right = false;
			left = false;
			down = false;
		}

		if ((key == KeyEvent.VK_DOWN)) {
			down = true;
			right = false;
			left = false;
			up = false;
		}
	}
	public void keyRelease(KeyEvent e) {
		int key = e.getKeyCode();
		System.out.println("hit");
		if ((key == KeyEvent.VK_LEFT)) {
			System.out.println("hit up");
			left = true;
			up = false;
			down = false;
			right = false;
		}

		if ((key == KeyEvent.VK_RIGHT)) {
			right = true;
			up = false;
			down = false;
			left = false;
		}

		if ((key == KeyEvent.VK_UP)) {
			up = true;
			right = false;
			left = false;
			down = false;
		}

		if ((key == KeyEvent.VK_DOWN)) {
			down = true;
			right = false;
			left = false;
			up = false;
		}
	}
}
