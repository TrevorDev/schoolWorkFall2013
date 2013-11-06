

public class Log extends Sprite{
	public Map map;
	public int counter = 0;
	public Log(Map m,int x,int y){
		super(Frogger.class.getResource(x>5?"dot.png":"log.png"),x,y,m.parentFrame.getHeight()/m.gridHeight,m.parentFrame.getWidth()/m.gridWidth);
		map = m;
		
	}
	
	public boolean move(int x,int y) {
		boolean fail=false;
		this.map.grid[posY][posX].contents.remove(this);
		this.posX+=x;
		this.posY+=y;
		if(posX<0||posX>=map.gridWidth||posY<0||posY>=map.gridHeight){
			fail=true;
		}
		if(fail){
			this.posX-=x;
			this.posY-=y;
		}
		
		
		
		this.map.grid[posY][posX].contents.add(this);
		
		if(map.grid[posY-y][posX-x].contents.contains(Player.player)){
			Player.player.move(x, y);
		}
		//this.map.parentFrame.repaint();
		return fail;
	}
	
	public boolean run(boolean left){
		counter++;
		return this.move(left?-1:1, 0);
	}
}
