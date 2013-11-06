

public class Car extends Sprite{
	public Map map;
	public int counter = 0;
	public Car(Map m,int x,int y){
		super(Frogger.class.getResource("path.png"),x,y,m.parentFrame.getHeight()/m.gridHeight,m.parentFrame.getWidth()/m.gridWidth);
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
		if(Player.player.checkDead()){
			map.gameOver();
		}
		this.map.grid[posY][posX].contents.add(this);
		//this.map.parentFrame.repaint();
		return fail;
	}
	
	public boolean run(boolean left){
		counter++;
		return this.move(left?-1:1, 0);
	}
}
