
public abstract class Spawn {
	public Map map;
	public int x;
	public int y;
	public int counter = 0;
	boolean left=true;
	public Spawn(Map map,int x,int y,boolean left){
		this.map = map;
		this.x=x;
		this.y=y;
		this.left=left;
		resetCounter();
	}
	public void resetCounter(){
		this.counter = (int)(Math.random()*100);
	}
	public void run(){
		
	}
}
