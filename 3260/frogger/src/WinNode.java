

public class WinNode extends Sprite{
	public Map map;
	public int counter = 0;
	public WinNode(Map m,int x,int y){
		super(Frogger.class.getResource("exit.png"),x,y,m.parentFrame.getHeight()/m.gridHeight,m.parentFrame.getWidth()/m.gridWidth);
		map = m;
		
	}
}
