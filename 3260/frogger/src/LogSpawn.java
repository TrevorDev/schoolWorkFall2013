import java.util.ArrayList;


public class LogSpawn extends Spawn {
	public ArrayList<Log> logs = new ArrayList<Log>();
	public int creating = 0;
	public LogSpawn(Map map,int x,int y,boolean left){
		super(map,x,y,left);
	}
	public void run(){
		counter++;
		for(int i=0;i<logs.size();i++){
			if(logs.get(i).run(left)){
				map.grid[logs.get(i).posY][logs.get(i).posX].contents.remove(logs.get(i));
				logs.remove(logs.get(i));
				i--;
			}
		}
		
		if((counter%10==0)||creating%2!=0){
			Log l = new Log(map, x, y);
			map.grid[y][x].contents.add(l);
			logs.add(l);
			creating++;
			if(creating%2==0){
				this.resetCounter();
			}
		}
		
	}
}
