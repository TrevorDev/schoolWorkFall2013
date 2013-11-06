

public class Player extends Sprite{
	public Map map;
	public static Player player;
	public Player(Map m,int x,int y){
		super(Frogger.class.getResource("pac.png"),x,y,m.parentFrame.getHeight()/m.gridHeight,m.parentFrame.getWidth()/m.gridWidth);
		map = m;
		player = this;
		
	}
	
	public void move(int x,int y) {
		boolean fail=false;
		player.map.grid[posY][posX].contents.remove(player);
		player.posX+=x;
		player.posY+=y;
		if(posX<0||posX>=map.gridWidth||posY<0||posY>=map.gridHeight){
			fail=true;
		}
		if(fail){
			player.posX-=x;
			player.posY-=y;
		}
		player.map.grid[posY][posX].contents.add(player);
		player.map.parentFrame.repaint();
		if(checkDead()){
			map.gameOver();
		}
	}
	
	public boolean checkDead(){
		boolean dead = false;
		for(int i=0;i<map.grid[this.posY][this.posX].contents.size();i++){
			Sprite x =map.grid[this.posY][this.posX].contents.get(i);
			
			if(x.getClass()==Car.class){
				dead=true;
			}
		}
		if(!dead){
			
			if(this.posY>=1&&this.posY<=3){
				dead=true;
				for(int i=0;i<map.grid[this.posY][this.posX].contents.size();i++){
					Sprite x =map.grid[this.posY][this.posX].contents.get(i);
					if(x.getClass()==Log.class){
						dead=false;
						break;
					}
				}
			}
		}
		return dead;
	}
}
